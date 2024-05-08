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

    def __init__(self, symbol):
        Player.__init__(self, symbol)
        if symbol == 'X':
            self.oppSym = 'O'
        else:
            self.oppSym = 'X'
        self.symbol = symbol
        self.MAXTIME = 2 # seconds
        self.tot_time = 0
        self.num_moves = 0
    
    def successor(self, board):
        # Takes in a current state and generates all succcessor states within one move
        avaliable_moves = []
        
        # code taken from othello_board.py and modified
        for c in range (0, board.cols):
            for r in range (0, board.rows):
                if board.is_cell_empty(c, r) and board.is_legal_move(c, r, self.symbol):
                    avaliable_moves.append([c,r])
        return avaliable_moves
    
    def expand(self, board, move, c_change, r_change):
        cost = 1
        i = move[0] + c_change
        j = move[1] + r_change
        while(board.is_in_bounds(i,j) and board.get_cell(i,j) == self.oppSym):
            cost += 1
            i += c_change
            j += r_change
        if board.get_cell(i,j) == self.symbol:
            return cost
        return 0

    def utility(self, board, move):
#         #Ref: https://phoenixnap.com/kb/python-initialize-dictionary
#         # keys = []
#         # cost = []

        # for move in successor:
        c = move[0]
        r = move[1]

        best_cost = 0

#         # if opponent has pieces to the left and of the move and player has one to the left of that
        if(board.is_in_bounds(c-1, r)):
            if(board.get_cell(c-1, r) == self.oppSym):
                cost = self.expand(board, move, -1, 0)
                if cost > best_cost:
                    best_cost = cost
        return best_cost


    def heuristic(self,board, min_or_max):
        # https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf
        # 100 * (Max Players coins - Min Players coins) / (Max Players coins + Min Players coins)
        final_move = None
        for move in self.successor(board):
            if final_move == None:
                final_move = move
            else:
                if self.utility(board, move) > self.utility(board, final_move):
                    final_move = move
        return final_move

    def overtime(self, init_time):
        return time.time() - init_time > self.MAXTIME

    def minimax(self, board, depth):
        # Ref Artificial Intelligence: A Modern Approach (4th edition) by Russell and Norvig 
        if depth == 0 or board.has_legal_moves_remaining(self.symbol) or self.overtime(time.time()):
            return self.heuristic(board, self.symbol)

        value, move = self.max_value(board, depth)

        return move

    def max_value(self, board, depth):
        if depth == 0 or board.has_legal_moves_remaining(self.symbol) or self.overtime(time.time()):
            return self.heuristic(board, self.symbol), None

        v = float(-1000000)

        # edit because board doesn't have actions
        for a in self.successor(board):
            v2, a2 = self.min_value(board, depth-1)
            if v2 > v:
                v, move = v2, a

        return v, move

    def min_value(self, board, depth):
        if depth == 0 or board.has_legal_moves_remaining(self.symbol) or self.overtime(time.time()):
            return self.heuristic(board, self.symbol), None

        v = 1000000

        # edit because board doesn't have actions
        for a in self.successor(board):
            v2, a2 = self.max_value(board, depth-1)
            if v2 < v:
                v, move = v2, a

        return v, move

    def get_move(self, board):
        # Get successor states
        init_time = time.time()
        move = self.minimax(board, depth=2)
        self.num_moves += 1
        self.tot_time = time.time() - init_time
        avg_time = self.tot_time / self.num_moves
        print("time: ", time.time() - init_time, "s, num moves: ", self.num_moves, "avg time: ", avg_time, "s")
        return move[0], move[1]
