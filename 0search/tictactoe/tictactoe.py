"""
Tic Tac Toe Player
"""

from cmath import inf
from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = {X: 0, O: 0}

    for row in board:
        for cell in row:
            if cell is X:
                count[X] += 1
            elif cell is O:
                count[O] += 1
    
    return O if count[X] > count[O] else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is EMPTY:
                actions.append((i, j))
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception

    result = deepcopy(board)

    result[action[0]][action[1]] = player(board)

    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] is not EMPTY: return board[0][0]
    if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] is not EMPTY: return board[1][0]
    if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] is not EMPTY: return board[2][0]

    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] is not EMPTY: return board[0][0]
    if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] is not EMPTY: return board[0][1]
    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] is not EMPTY: return board[0][2]

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] is not EMPTY: return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] is not EMPTY: return board[0][2]

    else: return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None: return True

    for row in board:
        for cell in row:
            if cell is EMPTY:
                return False
    
    else: return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return 1 if winner(board) is X else -1 if winner(board) is O else 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if player(board) == X:
        _, action = max_value(board)
    elif player(board) == O:
        _, action = min_value(board)
    
    return action

def max_value(board):
    if terminal(board):
        return utility(board), None
    
    v = -math.inf

    for action in actions(board):
        print(actions(board))
        min_val, _ = min_value(result(board, action))
        if min_val > v:
            act = action
            v = min_val

        if v == 1:
            return v, act
    
    return v, act

def min_value(board):
    if terminal(board):
        return utility(board), None
    
    v = math.inf

    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val < v:
            act = action
            v = max_val

        if v == -1:
            return v, act

    return v, act