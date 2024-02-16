from board import Board
import random
import time

#creates an array of 8 random states
def population():
    stateList = []
    #do it 8 times
    for _ in range(8):
        #create random states
        stringState = "".join(str(random.randint(0, 4)) for _ in range(5))
        #append the string to an array of states
        stateList.append(stringState)
    return stateList

#based on the state string generates a board with the respective queen layout
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

#creates empty board, helper function for generate board
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


# create boards based off the string state then extract fitness 
def getStateFitness(board, stateStr):
    stateBoard = generateBoard(board, stateStr)
    fitness = stateBoard.get_fitness()
    return fitness

#make a dictionary of states and their fitness value
def fitnessDic(board, population):
    fitnessDic = {}
    for i in population:
        fitness = getStateFitness(board, i)
        fitnessDic[i] = fitness
    return fitnessDic

# generate empty ,matrixc of "-" and then by using stateStr with the best fitness, place queens in the best spot 
# then print out ever row in the format of matrix 
def formatBoard(board, stateStr):
    format = [["-"] * board.n_queen for i in range(board.n_queen)]
    rowIndex = 0
    for i in stateStr:
        #gets a part of the string
        valueIndex = int(i)
        #change the empty spot to queen based on state string
        format[rowIndex][valueIndex] = "1"   
        #increases to next row after every iteration
        rowIndex += 1

    # Print the matrix
    for row in format:
        print(" ".join(row))

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

def geneticAlgo(board):
    startTime = time.time()
    #populate the parent
    parentGeneration = population()
    counter = 0
    while True:
        #create an array to hold a children, resets everytime it goes back to the loop
        newGeneration = []

        #runs at the length of half the states
        for _ in range(len(parentGeneration) // 2):
            #select two random parents
            selected = selection(parentGeneration)
            #create a tuple of two children that are crossed
            crossed = crossover(selected)
            #mutate the two children tuple 
            mutated = mutation(crossed, .50)
            #extract from the tuple
            child1, child2 = mutated
            #append both kids to the array
            newGeneration.append(child1)
            newGeneration.append(child2)
        
        #call fitnnessDic function to append new Generation states with their respected fitness
        fitnessValues = fitnessDic(board, newGeneration)
        # sort the values within the dictionary from smallest to highest
        sortedValues = {state: value for state, value in sorted(fitnessValues.items(), key=lambda state: state[1])}
        #create an array of keys from sortedValues, then extract the first item
        bestState =  list(sortedValues.keys())[0]
        #use the first key to extract its respected firness from sortedValues dic
        bestFitness = sortedValues[bestState]

        #when best fitness equals 0 return best state and run time
        if bestFitness == 0:
            endTime = time.time()
            runTime = endTime - startTime
            ms = round(runTime * 1000)
            return bestState, str(ms)
        #repopulates the parent gen with the new gen, so that we can create a diverse incestual family tree
        for i in range(len(newGeneration)):
            parentGeneration[i] = newGeneration[i]
    
test = Board(5)
optimalState, timed = (geneticAlgo(test))
# print(getStateFitness(test, optimalState))
print("Running time:", timed + "ms")
formatBoard(test, optimalState)
