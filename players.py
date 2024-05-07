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
    
    def expand(self, board, utility, move, c_change, r_change):
        cost = 0
        i = move[0] + c_change
        j = move[1] + r_change
        while(board.is_in_bounds(i,j) and board.get_cell(i,j) == self.oppSym):
            cost += 1
            i += c_change
            j += r_change
        if board.get_cell(i,j) == self.symbol:
            utility[move] = cost
        return utility

    def utility(self, board, successor):
        utility = {}

        for move in successor:
            c = move[0]
            r = move[1]
            # if opponent has pieces to the left and of the move and player has one to the left of that
            if(board.is_in_bounds(c-1, r)):
                if(board.get_cell(c-1, r) == self.oppSym):
                    utility = self.expand(board, utility, move, -1, 0)

            # if opponent has pieces to the right and of the move and player has one to the right of that
            if(board.is_in_bounds(c+1, r)):
                if(board.get_cell(c+1, r) == self.oppSym):
                    utility = self.expand(board, utility, move, 1, 0)
                
            # if opponent has pieces below the move and player has one below that
            if(board.is_in_bounds(c, r+1)):
                if(board.get_cell(c, r+1) == self.oppSym):
                    utility = self.expand(board, utility, move, 0, 1)

            # if opponent has pieces above the move and player has one above that
            if(board.is_in_bounds(c, r-1)):
                if(board.get_cell(c, r-1) == self.oppSym):
                    utility = self.expand(board, utility, move, 0, -1)

            # if opponent has pieces left-up-diagonal the move and player has one left-up-diagonal that
            if(board.is_in_bounds(c-1, r-1)):
                if(board.get_cell(c-1, r-1) == self.oppSym):
                    utility = self.expand(board, utility, move, -1, -1)

            # if opponent has pieces right-up-diagonal the move and player has one right-up-diagonal that
            if(board.is_in_bounds(c+1, r-1)):
                if(board.get_cell(c+1, r-1) == self.oppSym):
                    utility = self.expand(board, utility, move, 1, -1)
                
            # if opponent has pieces left-down-diagonal the move and player has one left-down-diagonal that
            if(board.is_in_bounds(c-1, r+1)):
                if(board.get_cell(c-1, r+1) == self.oppSym):
                    utility = self.expand(board, utility, move, -1, 1)

            # if opponent has pieces right-down-diagonal the move and player has one right-down-diagonal that
            if(board.is_in_bounds(c+1, r+1)):
                if(board.get_cell(c+1, r+1) == self.oppSym):
                    utility = self.expand(board, utility, move, 1, 1)
                
        return utility

    def heuristic(self, min_or_max):
        # https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf
        # 100 * (Max Players coins - Min Players coins) / (Max Players coins + Min Players coins)
        final_move_val = -1000000
        final_move = None
        for move in self.successor:
            move[1] = 100 * (move[1] - self.tot_time) / (move[1] + self.tot_time)
            if min_or_max == "max":
                if move[1] > final_move[1]:
                    final_move = move
            else:
                if move[1] < final_move[1]:
                    final_move = move
        return final_move[0]
    
    def overtime(self, init_time):
        return time.time() - init_time > self.MAXTIME
    
    def minimax(self):
        # Have heuristic function to make decision if past depth limit (2 sec)
        # override player class get_move inorder to produce a move through minimax
        init_time = time.time()
        final_move = None

        if(self.overtime(init_time)):
            return self.heuristic("max")
        
        # Maximizing player
        if(self.symbol == 'X'):
            # Find max move from successor states
            for move in self.successor:
                if(self.overtime(init_time)):
                    return self.heuristic("max")
                if move[1] > final_move[1]:
                    final_move = move
            return final_move[0]
        else:
            for move in self.successor:
                if(self.overtime(init_time)):
                    return self.heuristic("min")
                if move[1] < final_move[1]:
                    final_move = move
            # Find min move from successor states
            return final_move[0]

    def get_move(self, board):
        # Get successor states
        successor = self.successor(board)
        utility = self.utility(successor)
        return self.minimax()





