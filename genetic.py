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

def population():
    stateList = []
    # stateFitness = board.get_fitness()
    for _ in range(8):
        stringState = "".join(str(random.randint(0, 4)) for _ in range(5))
        stateList.append(stringState)
    return stateList

# create boards based off the string state then find fitness and append to dic based on state
def generateBoard(board, stateList):
    stateDic = {}
    listIndex = 0
    for _ in range(8):
        stateBoard = emptyBoard(board)
        for i in range(board.n_queen):
            valueIndex = stateList[listIndex][i]
            valueIndex = int(valueIndex)
            stateBoard.map[i][valueIndex] = 1   
        fitness = stateBoard.get_fitness()
        stateDic[stateList[listIndex]] = fitness
        listIndex += 1
    return stateDic

def emptyBoard(board):
    tempBoard = board
    for i in range(board.n_queen):
        for j in range(board.n_queen):
            if tempBoard.map[i][j] == 1:
                tempBoard.map[i][j] = 0
    return tempBoard

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
print(test.get_fitness())
# print(state(test))
arr = population()
print(generateBoard(test, arr))
