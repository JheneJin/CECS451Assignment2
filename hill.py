from board import Board
import time

def formatBoard(board):
    #create an empty matrix of "-"
    format = [["-"] * board.n_queen for i in range(board.n_queen)]
    for i in range(board.n_queen):
        for j in range(board.n_queen):
            #changes the queen to a string in format Matrix
            if board.map[i][j] == 1:
                format[i][j] = "1"

    # Print the matrix
    for row in format:
        print(" ".join(row))

def hillClimbAlgo(board):
  startTime = time.time()
  #restart counter
  maxCounter = 0
  while True:
    for i in range(board.n_queen):
      #get the initial fitness value for every row(i)
      fitness = board.get_fitness()
      for j in range(board.n_queen):
        #when there is a queen
        if board.map[i][j] == 1:
          #save the queen's coordinates
          queenLoc = (i, j)
          #change the queen to a 0
          board.flip(i, j)
      for j in range(board.n_queen):
        #flip the 0 to a queen
        board.flip(i, j)
        #get it's fitness value
        newFitness = board.get_fitness()
        #if newFitness value is smaller than fitness
        #<= to be more dynamic and move objects in the board more often
        #not as dynamic as two if conditions, if it cant find the solution goes to maxCounter if Condition
        if newFitness <= fitness:
          #update fitness with newFitness
          fitness = newFitness
          #update the queenLoc with the respective best value
          queenLoc = (i, j)
        #revert the queen to a zero
        board.flip(i, j)
      #flip where the bestQueen(0 to queen)
      board.flip(queenLoc[0], queenLoc[1])
      #if fitness is equal to 0
      if fitness == 0:
        endTime = time.time()
        runTime = endTime - startTime
        #round ms
        ms = round(runTime * 1000)
        return board, str(ms)
    #add onto the maxCounter if it goes thru the board one and doesnt reach fitness 0 during the loop run
    maxCounter += 1
    #change back to 30, 2 for debugging purposes
    if maxCounter == 10:
      #restart the board
      board = Board(board.n_queen)
      maxCounter = 0

test = Board(5)
outputBoard, timed = hillClimbAlgo(test)
# print(outputBoard.get_fitness())
print("Running time:", timed + "ms")
formatBoard(outputBoard)
