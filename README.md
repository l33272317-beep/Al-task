Task 2 – Romania Map Search Algorithms

File Name
Task2.py

Project Description

This project implements and compares two informed search algorithms: Greedy Best-First Search and A Search* using the Romania map problem.

The goal is to find a path from a starting city to Bucharest with the lowest possible cost.

Algorithms Used

1. Greedy Best-First Search

* Uses the heuristic value h(n) to select the next city.
* Chooses the city that appears closest to the goal.
* Does not consider the total path cost.

2. A* Search

* Uses the evaluation function:
    f(n) = g(n) + h(n)
* g(n): Actual cost from the starting city to the current city.
* h(n): Estimated cost from the current city to Bucharest.
* Selects the city with the lowest total estimated cost.

Project Features

* Uses the Romania map with distances between cities.
* Uses heuristic values for each city.
* Finds paths from different starting cities to Bucharest.
* Calculates the total path cost in kilometers.
* Counts the number of expanded nodes.
* Tracks the maximum frontier size.
* Displays the order in which nodes are expanded.

Test Cases

The program runs five test cases:

Case	Starting City	Algorithm
1	Timisoara	Greedy Best-First
2	Timisoara	A*
3	Sibiu	Greedy Best-First
4	Sibiu	A*
5	Timisoara	A* (h = 0)
6	Timisoara	A* (2h)

Performance Measurements

Each test case displays:

* Path: The route from the starting city to Bucharest.
* Path Cost: The total distance in kilometers.
* Nodes Expanded: The number of expanded nodes.
* Max Frontier: The maximum number of nodes stored in the frontier.
* Expansion Order: The order in which cities are expanded.

Special Heuristic Tests

* A (h = 0):* Runs A* without heuristic information.
* A (2h):* Runs A* using twice the original heuristic values.

These tests help compare how heuristic values affect the search algorithm.

How to Run

1. Make sure Python 3 is installed.
2. Open the project file.
3. Run the following command:

python Task2.py

4. The program displays the results of all test cases in the terminal.

Programming Language

Python 3
