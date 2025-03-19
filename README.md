# Genetic Algorithm Project

## Overview

This project is a flexible and generic genetic algorithm framework designed to solve any optimization problem by defining three key functions:

1. **Chromosome Construction**
2. **Fitness Evaluation**
3. **Crossover Mechanism**

The algorithm is implemented using a graphical user interface (GUI) that allows users to define these functions interactively.

## Project Structure

The project consists of two main Python files:

- ``: Contains the `GASolver` class, which implements the core genetic algorithm, including selection, mutation, and evolution functions.
- ``: Defines the `GAProblem` class, which manages user-defined genetic functions through a GUI, allowing users to customize the algorithm for different problems.

## Features

- **User-defined Genetic Functions**: The user provides Python implementations for chromosome creation, fitness evaluation, and crossover.
- **Graphical User Interface (GUI)**: Users can input their functions interactively.
- **Flexible Genetic Algorithm**: Supports adjustable selection rates, mutation rates, and termination criteria.

## Installation

Ensure Python is installed along with the necessary dependencies. You can install required packages using:

```bash
pip install -r genetic.zip
```

## Usage

### Running the Algorithm

1. **Launch the script**
   ```bash
   python ga_solver.py
   ```
2. **Define Genetic Functions**
   - A GUI will prompt you to enter Python code for:
     - **Building a chromosome**
     - **Evaluating fitness**
     - **Crossing two chromosomes**
3. **Run the Evolutionary Process**
   - The algorithm will optimize the problem over multiple generations.

## Function Details

Users must define the following functions:

### 1. Chromosome Construction (`build_chromosome`)

This function should generate a random chromosome. Example:

```python
def build_chromosome():
    return [random.randint(0, 1) for _ in range(10)]
```

### 2. Fitness Evaluation (`fitness`)

This function should return a numerical fitness score for a given chromosome. Example:

```python
def fitness(chromosome):
    return sum(chromosome)  # Maximizing the number of 1s
```

### 3. Crossover Mechanism (`cross_chromosome`)

This function combines two parent chromosomes to produce offspring. Example:

```python
def cross_chromosome(parent1, parent2):
    midpoint = len(parent1) // 2
    return parent1[:midpoint] + parent2[midpoint:]
```

## Customization

You can modify the following parameters in `GASolver`:

- **Population size**
- **Selection rate**
- **Mutation rate**
- **Number of generations**
- **Fitness threshold**

## Contributing

Feel free to improve the project by adding new features or optimizing the algorithm.

## Licence 

Don't know about it but everybody can use and share my code, he is prety shitie tbh 
