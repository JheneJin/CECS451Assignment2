from board import Board
import random
import numpy as np

def population():
    stateList = []
    for _ in range(8):
        stringState = "".join(str(random.randint(0, 4)) for _ in range(5))
        stateList.append(stringState)
    return stateList

def generateBoard(board, stateStr):
    columnIndex = 0
    stateBoard = emptyBoard(board)
    for i in stateStr:
        valueIndex = int(i)
        stateBoard.map[columnIndex][valueIndex] = 1   
        columnIndex += 1
    return stateBoard

# create boards based off the string state then find fitness and append to dic based on state
def getStateFitness(board, stateStr):
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

def mutation(children, mutationRate):
    child1, child2 = children
    child1 = list(child1)
    child2 = list(child2)
    childLen = len(child1)

    randDigit1 = random.randint(0, childLen - 1)
    randDigit2 = random.randint(0, childLen - 1)

    for i in range(childLen):
        if random.random() < mutationRate:
            child1[i] = str(randDigit1)
        if random.random() < mutationRate:
            child2[i] = str(randDigit2)

    child1 = "".join(child1)
    child2 = "".join(child2)
    return child1, child2

def fitnessDic(board, population):
    fitnessDic = {}
    for i in population:
        fitness = getStateFitness(board, i)
        fitnessDic[i] = fitness
    return fitnessDic

def geneticAlgo(board, generations):
    arr = population()
    for generation in range(generations):
        newGeneration = []

        for _ in range(len(arr) // 2):
            selected = selection(arr)
            crossed = crossover(selected)
            mutated = mutation(crossed, .50)
            child1, child2 = mutated
            newGeneration.append(child1)
            newGeneration.append(child2)
        
        fitnessValues = fitnessDic(board, newGeneration)
        sortedValues = {k: v for k, v in sorted(fitnessValues.items(), key=lambda item: item[1])}
        bestState =  list(sortedValues.keys())[0]
        bestFitness = sortedValues[bestState]

        if bestFitness == 0:
            return bestState, bestFitness
        # return bestState, bestFitness
    
test = Board(5)
optimalState, fitness = (geneticAlgo(test, 100000))
print(optimalState, fitness)
bestBoard = (generateBoard(test, optimalState))
for row in bestBoard.get_map():
    print(row)


