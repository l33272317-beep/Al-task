H = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Eforie': 161,
    'Fagaras': 178,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 98,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374,
}

ROMANIA_CODE= {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Craiova': {'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Eforie': {'Hirsova': 86},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Giurgiu': {'Bucharest': 90},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Neamt': {'Iasi': 87},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'Craiova': 138, 'Rimnicu Vilcea': 97, 'Bucharest': 101},
    'Rimnicu Vilcea': {'Craiova': 146, 'Sibiu': 80, 'Pitesti': 97},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Zerind': {'Arad': 75, 'Oradea': 71},
}


def search(graph, start, goal, h, algorithm='astar'):
    if algorithm != 'astar' and algorithm != 'greedy':
        raise ValueError('algorithm must be astar or greedy')

    frontier = [{
        'city': start,
        'cost': 0,
        'priority': h[start]
    }]

    best_cost = {start: 0}
    parent = {start: None}
    expanded = []
    max_frontier = 1

    while len(frontier) > 0:
        best_index = 0

        for i in range(1, len(frontier)):
            if frontier[i]['priority'] < frontier[best_index]['priority']:
                best_index = i

        item = frontier.pop(best_index)
        city = item['city']
        cost = item['cost']

        if city == goal:
            path = []
            current = goal

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            return {
                'path': path,
                'cost': cost,
                'nodes_expanded': len(expanded),
                'max_frontier': max_frontier,
                'expanded_order': expanded
            }

        expanded.append(city)

        if algorithm == 'greedy':
            for neighbor in sorted(graph[city]):
                if neighbor == goal:
                    parent[neighbor] = city
                    goal_cost = cost + graph[city][neighbor]

                    path = []
                    current = goal

                    while current is not None:
                        path.append(current)
                        current = parent[current]

                    path.reverse()

                    return {
                        'path': path,
                        'cost': goal_cost,
                        'nodes_expanded': len(expanded),
                        'max_frontier': max_frontier,
                        'expanded_order': expanded
                    }

        for neighbor in sorted(graph[city]):
            new_cost = cost + graph[city][neighbor]

            if algorithm == 'greedy':
                if neighbor in best_cost:
                    continue
            else:
                if neighbor in best_cost:
                    if new_cost >= best_cost[neighbor]:
                        continue

            best_cost[neighbor] = new_cost
            parent[neighbor] = city

            if algorithm == 'greedy':
                priority = h[neighbor]
            else:
                priority = new_cost + h[neighbor]

            for i in range(len(frontier)):
                if frontier[i]['city'] == neighbor:
                    frontier.pop(i)
                    break

            frontier.append({
                'city': neighbor,
                'cost': new_cost,
                'priority': priority
            })

        if len(frontier) > max_frontier:
            max_frontier = len(frontier)

    return {
        'path': [],
        'cost': None,
        'nodes_expanded': len(expanded),
        'max_frontier': max_frontier,
        'expanded_order': expanded
    }


def run_case(rows, start, name, h, mode):
    result = search(ROMANIA_CODE, start, 'Bucharest', h, mode)

    result['start'] = start
    result['algorithm'] = name
    rows.append(result)

    print('\n' + '*' * 65)
    print('case: ' + str(len(rows)))
    print('Start city     : ' + start)
    print('Goal city      : Bucharest')
    print('Algorithm      : ' + name)
    print('Path           : ' + ' -> '.join(result['path']))
    print('Path cost      : ' + str(result['cost']) + ' km')
    print('Nodes expanded : ' + str(result['nodes_expanded']))
    print('Max frontier   : ' + str(result['max_frontier']))
    print('Expansion order: ' + ' -> '.join(result['expanded_order']))


def main():
    start_cities = ['Timisoara', 'Sibiu']
    rows = []

    for start in start_cities:
        run_case(rows, start, 'Greedy Best-first', H, 'greedy')
        run_case(rows, start, 'A*', H, 'astar')

    zero_h = {city: 0 for city in H}
    double_h = {city: 2 * H[city] for city in H}

    run_case(rows, 'Timisoara', 'A* (h = 0)', zero_h, 'astar')
    run_case(rows, 'Timisoara', 'A* (2h)', double_h, 'astar')
    print('\n' + '=' * 55)
    print('           RESULTS SUMMARY')
    print('=' * 55)

    print(f"{'No.':<5}{'Algorithm':<22}{'Cost':<10}{'Expanded'}")
    print('-' * 55)

    for i, row in enumerate(rows, 1):
        print(f"{i:<5}{row['algorithm']:<22}"
              f"{row['cost']:<10}{row['nodes_expanded']}")

    print('=' * 55)

if __name__ == '__main__':
    main()