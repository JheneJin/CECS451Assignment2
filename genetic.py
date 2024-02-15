from board import Board
import random
import numpy as np

# def state(board):
#     stateDic = {}
#     stringState = ""
#     for i in range(board.n_queen):
#         for j in range(board.n_queen):
#             if board.map[i][j] == 1:
#                 stringState += str(j + 1)
#     stateDic[stringState] = stateFitness
#     return stateDic

def population():
    stateList = []
    for _ in range(8):
        stringState = "".join(str(random.randint(0, 4)) for _ in range(5))
        stateList.append(stringState)
    return stateList

# # create boards based off the string state then find fitness and append to dic based on state
# def generateBoard(board, stateList):
#     stateDic = {}
#     listIndex = 0
#     for _ in range(8):
#         stateBoard = emptyBoard(board)
#         for i in range(board.n_queen):
#             valueIndex = stateList[listIndex][i]
#             valueIndex = int(valueIndex)
#             stateBoard.map[i][valueIndex] = 1   
#         fitness = stateBoard.get_fitness()
#         stateDic[stateList[listIndex]] = fitness
#         listIndex += 1
#     return stateDic

def stateGen():
    stateList = []
    for _ in range(8):
        stringState = "".join(str(random.randint(0, 4)) for _ in range(5))
        stateList.append(stringState)
    return stateList

# create boards based off the string state then find fitness and append to dic based on state
def getStateFitness(board, stateStr):
    stateDic = {}
    columnIndex = 0
    stateBoard = emptyBoard(board)
    for i in stateStr:
        valueIndex = int(i)
        stateBoard.map[columnIndex][valueIndex] = 1   
        columnIndex += 1
    fitness = stateBoard.get_fitness()
    return fitness

def emptyBoard(board):
    #creates a copy of the generated board
    tempBoard = board
    for i in range(board.n_queen):
        for j in range(board.n_queen):
            if tempBoard.map[i][j] == 1:
                tempBoard.map[i][j] = 0
    return tempBoard

def selection(population):
    parent1, parent2 = random.sample(population, 2)
    return parent1, parent2

def crossover(parents):
   parent1, parent2 = parents
   parentLen = len(parent1)
   slicePoint = random.randint(1, parentLen - 1)
   #slices the string
   child1 = parent1[:slicePoint] + parent2[slicePoint:]
   child2 = parent2[:slicePoint] + parent1[slicePoint:]
   return child1, child2

def mutation(children):
    child1, child2 = children
    child1 = list(child1)
    child2 = list(child2)
    childLen = len(child1)

    randIndex1 = random.randint(0,childLen - 1)
    randIndex2 = random.randint(0,childLen - 1)

    randDigit1 = random.randint(0,childLen - 1)
    randDigit2 = random.randint(0,childLen - 1)

    child1[randIndex1] = str(randDigit1)
    child2[randIndex2] = str(randDigit2)

    child1 = "".join(child1)
    child2 = "".join(child2)
    return child1, child2

test = Board(5)
print("Initial map:")
for row in test.get_map():
    print(row)
print(test.get_fitness())
# print(state(test))
arr = population()
print(generateBoard(test, arr))
