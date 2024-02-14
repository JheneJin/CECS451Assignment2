from board import Board

def hillClimbAlgo(board, runs):
    #gets the intial fitness
    fitness = board.get_fitness()
    for loop in range(runs):
        for i in range(board.n_queen):
            bestFitness = board.get_fitness()
            bestMove = (None, None)
            for j in range(board.n_queen):
                if board.map[i][j] == 1:
                    bestMove = (i,j)
            for j in range(board.n_queen):
                board.map[i] = [0 for _ in range(board.n_queen)]
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

            board.map[i] = [0 for _ in range(board.n_queen)]
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

hillClimbAlgo(test, 1000)

print("\nFinal fitness after hill climbing:", test.get_fitness())
print("Final map after hill climbing:")
for row in test.get_map():
    print(row)
