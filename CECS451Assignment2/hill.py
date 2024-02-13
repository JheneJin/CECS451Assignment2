from board import Board

def hillClimbAlgo(board, runs):
    #gets the intial fitness
    fitness = board.get_fitness()
    for loop in range(runs):
        #runs the algorithm until it finds the best move
        bestMove = None
        bestFitness = fitness
        #intializes best move as None
        for i in range(board.n_queen):
            for j in range(board.n_queen):
                #on the board, if a part of the matrix equals 0
                if board.map[i][j] == 0:
                    #changes the value to 1  or a queen
                    board.flip(i, j)
                    newFitness = board.get_fitness()
                    #compares the fitness or h to see if it is higher or lower
                    if newFitness < bestFitness:
                        #updates the best Fitness if it is lower
                        bestFitness = newFitness
                        #saves the best move
                        bestMove = (i,j)
                    #fixes the board back tot he nromal
                    board.flip(i, j)
        
        #better move found, applies and updates the fitness
        if bestMove:
            board.flip(bestMove[0], bestMove[1])
            fitness = board.get_fitness()
        #break the loop if no better move is found
        else:
            break

test = Board(5)
print("Initial fitness:", test.get_fitness())
print("Initial map:")
for row in test.get_map():
    print(row)

hillClimbAlgo(test, 50)

print("\nFinal fitness after hill climbing:", test.get_fitness())
print("Final map after hill climbing:")
for row in test.get_map():
    print(row)