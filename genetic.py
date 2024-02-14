from board import Board
import random
import numpy as np

# def state(board):
#     stateDic = {}
#     stringState = ""
#     stateFitness = board.get_fitness()
#     for i in range(board.n_queen):
#         for j in range(board.n_queen):
#             if board.map[i][j] == 1:
#                 stringState += str(j + 1)
#     stateDic[stringState] = stateFitness
#     return stateDic

def population(board):
    stateDic = {}
    stateFitness = board.get_fitness()
    for i in range(8):
        stringState = "".join(str(random.randint(0, 4)) for _ in range(5))
        stateDic[stringState] = stateFitness
    return stateDic

def crossover(parent1, parent2):
   pass

def mutation(board, mutation_rate):
    pass

def geneticAlgo(population_size, mutation_rate, max_generations):
   pass

test = Board(5)
print("Initial map:")
for row in test.get_map():
    print(row)
# print(test.get_map())
print(population(test))
