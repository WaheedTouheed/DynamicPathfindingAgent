# Dynamic Pathfinding Agent

## Project Overview

The Dynamic Pathfinding Agent project implements an intelligent navigation system capable of finding an optimal path inside a grid-based environment using Informed Search Algorithms. The agent travels from a predefined Start node to a Goal node while avoiding obstacles that may dynamically appear during execution.

Unlike static pathfinding systems, this project supports real-time obstacle generation and automatic path re-planning, simulating real-world navigation problems such as autonomous robots and self-driving systems.

---

## Objectives

* Implement informed search algorithms for pathfinding.
* Visualize search exploration in real time.
* Allow dynamic obstacle creation during agent movement.
* Enable automatic path recalculation when paths become blocked.
* Compare performance of different informed search strategies.

---

## Implemented Algorithms

### Greedy Best First Search (GBFS)

Greedy Best First Search selects nodes based only on heuristic value.

Evaluation Function:
f(n) = h(n)

Characteristics:

* Fast execution
* Low computation cost
* Does not guarantee optimal solution

---

### A* Search Algorithm

A* Search combines path cost and heuristic estimate.

Evaluation Function:
f(n) = g(n) + h(n)

Where:

* g(n) = cost from start node
* h(n) = estimated distance to goal

Characteristics:

* Complete algorithm
* Optimal path generation
* Efficient exploration

---

## Heuristic Functions

The project supports the following heuristic methods:

* Manhattan Distance
  h(n) = |x1 − x2| + |y1 − y2|

* Euclidean Distance
  h(n) = √((x1 − x2)² + (y1 − y2)²)

---

## Features

* Dynamic grid generation
* User-defined obstacle placement
* Interactive graphical interface
* Real-time path visualization
* Agent movement animation
* Dynamic obstacle spawning
* Automatic path re-planning
* Algorithm comparison capability
* Execution visualization

---

## Visualization Legend

| Element    | Color |
| ---------- | ----- |
| Empty Cell | White |
| Obstacle   | Black |
| Agent      | Red   |
| Final Path | Green |
| Grid Lines | Gray  |

---

## Controls

| Action           | Function               |
| ---------------- | ---------------------- |
| Mouse Left Click | Add or Remove Obstacle |
| SPACE Key        | Start Pathfinding      |
| Close Window     | Exit Application       |

---

## Project Structure

DynamicPathfindingAgent/

main.py – Program entry point
grid.py – Grid environment management
astar.py – A* search implementation
gbfs.py – Greedy Best First Search implementation
heuristics.py – Heuristic calculations
agent.py – Agent movement logic
dynamic_obstacles.py – Dynamic obstacle spawning
gui.py – Graphical User Interface
README.md – Project documentation

---

## Installation Instructions

### Step 1: Clone Repository

git clone https://github.com/WaheedTouheed/DynamicPathfindingAgent.git

---

### Step 2: Open Project

Open the project folder using PyCharm or any Python IDE.

---

### Step 3: Install Dependencies

Install required Python library:

pip install pygame

---

## Running the Project

Run using terminal:

python main.py

OR

Run main.py directly from PyCharm.

---

## System Requirements

* Python 3.8 or higher
* PyCharm / VS Code
* Pygame Library
* Windows / Linux / macOS

---

## Experimental Analysis Goals

* Compare GBFS and A* performance
* Analyze node expansion behavior
* Evaluate optimal path generation
* Observe dynamic obstacle handling
* Study re-planning efficiency

---

## Future Improvements

* GUI-based algorithm selection
* Multiple heuristic switching
* Diagonal movement support
* Weighted movement cost
* Performance metrics dashboard
* Advanced dynamic re-planning optimization

---

## Author

Waheed Touheed
BS Computer Science
FAST National University of Computer & Emerging Sciences

---

## Academic Notice

This project is developed strictly for academic and educational purposes as part of an Artificial Intelligence course assignment.

---

## License

Free for educational use only.
