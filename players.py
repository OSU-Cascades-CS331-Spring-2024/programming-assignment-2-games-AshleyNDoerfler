'''
    Defines Player class, and subclasses Human and Minimax Player.
'''
import time
from othello_board import OthelloBoard

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    #PYTHON: use obj.symbol instead
    def get_symbol(self):
        return self.symbol
    
    #parent get_move should not be called
    def get_move(self, board):
        raise NotImplementedError()


class HumanPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol)

    def clone(self):
        return HumanPlayer(self.symbol)
        
#PYTHON: return tuple instead of change reference as in C++
    def get_move(self, board):
        col = int(input("Enter col:"))
        row = int(input("Enter row:"))
        return col, row


class MinimaxPlayer(Player):

    def __init__(self, symbol, othello_board):
        Player.__init__(self, symbol)
        if symbol == 'X':
            self.oppSym = 'O'
        else:
            self.oppSym = 'X'
        self.symbol = symbol
        self.MAXTIME = 2 # seconds
        self.tot_time = 0
    
    def successor(self, board):
        # Takes in a current state and generates all succcessor states within one move
        avaliable_moves = []
        
        # code taken from othello_board.py and modified
        for c in range (0, board.cols):
            for r in range (0, board.rows):
                if board.is_cell_empty(c, r) and board.is_legal_move(c, r, self.symbol):
                    avaliable_moves.append([c,r])
        return avaliable_moves
    
    # def iterative_deepening_search(self):
    #     # This is the utility function
    #     # Ref1: https://stacks.stanford.edu/file/druid:wk764yw7162/wk764yw7162.pdf idk how tf they did this as a utility, probably read it wrong
    #     # Ref2: https://chatgpt.com/c/35d89200-0d2b-4af6-b88f-6adc363f3b0e
    #     # Adapted from previous assignment

    #     # Use time as depth according to the assignment's terms
    #     init_time = time.time()

    #     for depth in range(1, 100):
    #         score, move = self.dls(depth, init_time, run_time) # Ref2: Added score and move instead of result
    #         run_time = time.time() - init_time
    #         if init_time > self.MAXTIME:
    #             self.tot_time += run_time
    #             # If it goes over two seconds, call the heuristic function to pick an answer
    #             result = self.heuristic()
    #             return result
            
    #         return [score, move]
            
    # def dls(self, depth, init_time, run_time):
    #     #Ref: https://chatgpt.com/c/35d89200-0d2b-4af6-b88f-6adc363f3b0e

    #     frontier = [self.start]
    #     path = []
    #     count = 0
    #     visited = []

    #     if init_time > self.MAXTIME:
    #             self.tot_time += run_time
    #             # If it goes over two seconds, call the heuristic function to pick an answer
    #             result = self.heuristic()
    #             return result

    #     while frontier:
    #         node = self.mapping.get_city_object(frontier.pop(0))
    #         visited.append(node.name)

    #         print("Depth: ", depth, "Node: ", node.name, ", Frontier: ", frontier)

    #         path.append(node.name)
    #         count += 1

    #         # Success
    #         if node.name == self.end:
    #             return path

    #         if depth > count:
    #             for child_name, _ in self.mapping.get_citys_connections(node.name).items():
    #                 if child_name not in visited:
    #                     frontier.append(child_name)
    #                 # print("Node: ", node.name, ",Frontier: ", frontier)

    #     return "cutoff"

    def utility(self, board, successor):
        utility = {}

        for move in successor:
            # if opponent has pieces to the left and of the move and player has one to the left of that

            # if opponent has pieces to the right and of the move and player has one to the right of that

            # if opponent has pieces below the move and player has one below that

            # if opponent has pieces above the move and player has one above that

            # if opponent has pieces left-up-diagonal the move and player has one left-up-diagonal that

            # if opponent has pieces right-up-diagonal the move and player has one right-up-diagonal that

            # if opponent has pieces left-down-diagonal the move and player has one left-down-diagonal that

                        # if opponent has pieces right-down-diagonal the move and player has one right-down-diagonal that




    def heuristic(self):
        # https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf
        # 100 * (Max Players coins - Min Players coins) / (Max Players coins + Min Players coins)
        return
    
    def minimax(depth):
        # Have heuristic function to make decision if past depth limit (2 sec)
        # override player class get_move inorder to produce a move through minimax
        return

    def get_move(self, board):
        # Get successor states
        successor = self.successor(board)
        utility = self.utility(successor)





