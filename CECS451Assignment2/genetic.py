from board import Board
import random
import numpy as np

def crossover(parent1, parent2):
    # Randomly select a crossover point
    crossover_point = random.randint(1, parent1.n_queen - 1)

    # Create the first child by combining the first part of parent1 and the second part of parent2
    child1_map = parent1.map[:crossover_point] + parent2.map[crossover_point:]
    child1 = Board(parent1.n_queen)
    child1.map = child1_map

    # Create the second child by combining the first part of parent2 and the second part of parent1
    child2_map = parent2.map[:crossover_point] + parent1.map[crossover_point:]
    child2 = Board(parent2.n_queen)
    child2.map = child2_map

    return child1, child2

def mutate(board, mutation_rate):
    for i in range(board.n_queen):
        for j in range(board.n_queen):
            if random.random() < mutation_rate:
                board.flip(i, j)

def selection(population):
    # Randomly select two parents from the population
    parent1, parent2 = random.sample(population, 2)

    return parent1, parent2

def geneticAlgo(population_size, mutation_rate, max_generations):
    # Initialize population with random boards
    population = [Board(parent1.n_queen) for _ in range(population_size)]

    for generation in range(max_generations):
        new_population = []

        for _ in range(population_size // 2):
            # Selection
            parent1, parent2 = selection(population)

            # Crossover
            child1, child2 = crossover(parent1, parent2)

            # Mutation
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)

            new_population.extend([child1, child2])

        # Update population
        population = new_population

        # Get the best board in the population
        best_board = max(population, key=lambda board: board.get_fitness())

        print("Generation:", generation + 1, "Best fitness:", best_board.get_fitness())

    return best_board

test = Board(5)
print("Initial fitness:", test.get_fitness())
print("Initial map:")
for row in test.get_map():
    print(row)

test_board_size = 5
population_size = 50
mutation_rate = 0.1
max_generations = 5

print(f"Running genetic algorithm with a board size of {test_board_size}...")
best_board = geneticAlgo(test_board_size, population_size, mutation_rate, max_generations)

print("\nFinal fitness after genetic algorithm:", best_board.get_fitness())
print("Final map after genetic algorithm:")
for row in best_board.get_map():
    print(row)