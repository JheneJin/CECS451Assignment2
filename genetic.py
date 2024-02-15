from board import Board
import random

def population():
    stateList = []
    #do it 8 times
    for _ in range(8):
        #create random states
        stringState = "".join(str(random.randint(0, 4)) for _ in range(5))
        #append the string to an array of states
        stateList.append(stringState)
    return stateList

def generateBoard(board, stateStr):
    rowIndex = 0
    #creates empty board
    stateBoard = emptyBoard(board)
    for i in stateStr:
        #gets a part of the string
        valueIndex = int(i)
        #change the empty spot to queen based on state string
        stateBoard.map[rowIndex][valueIndex] = 1   
        #increases to next row after every iteration
        rowIndex += 1
    return stateBoard

# create boards based off the string state then find fitness and append to dic based on state
def getStateFitness(board, stateStr):
    stateBoard = generateBoard(board, stateStr)
    fitness = stateBoard.get_fitness()
    return fitness

def fitnessDic(board, population):
    fitnessDic = {}
    for i in population:
        fitness = getStateFitness(board, i)
        fitnessDic[i] = fitness
    return fitnessDic

def emptyBoard(board):
    #creates a copy of the generated board
    tempBoard = board
    for i in range(board.n_queen):
        for j in range(board.n_queen):
            #changes the queen to a 0
            if tempBoard.map[i][j] == 1:
                tempBoard.map[i][j] = 0
    #returns an empty board
    return tempBoard

def selection(population):
    #extracts two items from population arr randomly
    parent1, parent2 = random.sample(population, 2)
    #returns tuple
    return parent1, parent2

def crossover(parents):
   #extracts each individual parent from parents tuple
   parent1, parent2 = parents
   parentLen = len(parent1)
   #creates a random point to slice the strings
   slicePoint = random.randint(1, parentLen - 1)
   #slices the string between the two parents and creates two children based off mixing
   child1 = parent1[:slicePoint] + parent2[slicePoint:]
   child2 = parent2[:slicePoint] + parent1[slicePoint:]
   #returns tuple
   return child1, child2

def mutation(children, mutationRate):
    #extracts each individula child from children tuple
    child1, child2 = children
    #convert the strings to arrays of letters
    child1 = list(child1)
    child2 = list(child2)
    childLen = len(child1)
    #generate two random digits for mutations
    randDigit1 = random.randint(0, childLen - 1)
    randDigit2 = random.randint(0, childLen - 1)
    #use random.random to create a digit from 0.0 to 1.0 and compare it to mutation rate
    #if less than a random number in state/child string will mutate
    for i in range(childLen):
        if random.random() < mutationRate:
            child1[i] = str(randDigit1)
        if random.random() < mutationRate:
            child2[i] = str(randDigit2)
    #recombine the array back to a string
    child1 = "".join(child1)
    child2 = "".join(child2)
    #returns tuple
    return child1, child2

def geneticAlgo(board, generations):
    arr = population()
    counter = 0
    for generation in range(generations):
        newGeneration = []
        counter += 1

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
            return bestState, bestFitness, counter
        # return bestState, bestFitness
    
test = Board(5)
# optimalState, fitness, generation = (geneticAlgo(test, 100000))
# for _ in range(50):
optimalState, fitness, generation = (geneticAlgo(test, 100000))
    # print(optimalState, fitness, generation)
bestBoard = (generateBoard(test, optimalState))
for row in bestBoard.get_map():
    print(row)



