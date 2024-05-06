'''
    Defines Player class, and subclasses Human and Minimax Player.
'''
import time

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

    def __init__(self, symbol):
        Player.__init__(self, symbol)
        if symbol == 'X':
            self.oppSym = 'O'
        else:
            self.oppSym = 'X'
        self.MAXTIME = 2 # seconds
        self.tot_time = 0

    # Ref: https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf
    def utility(self):
        # Determines "Goodness" of a terminal state
        return
    
    def successor(self):
        # Takes in a current state and generates all succcessor states within one move
        return
    
    def iterative_deepening_search(self):
        # Ref: https://stacks.stanford.edu/file/druid:wk764yw7162/wk764yw7162.pdf
        # Adapted from previous assignment

        # Use time as depth according to the assignment's terms
        init_time = time.time()

        for depth in range(1, 100):
            result = self.dls(depth)
            run_time = time.time() - init_time
            if init_time > self.MAXTIME:
                self.tot_time += run_time
                # If it goes over two seconds, call the heuristic function to pick an answer
                result = self.heuristic()
                return result
            if result != "cutoff":
                return result
            
    def dls(self, depth):
        return

    def heuristic(self):
        # https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf
        # 100 * (Max Players coins - Min Players coins) / (Max Players coins + Min Players coins)
        return
    
    def minimax(depth):
        # Have heuristic function to make decision if past depth limit (2 sec)
        # override player class get_move inorder to produce a move through minimax
        return

        





