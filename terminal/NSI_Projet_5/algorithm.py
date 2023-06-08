import time
import copy
import random

if "raw_input" in dir(globals()):
    globals()["input"] = raw_input

class Singleton(type):
    """
    Metaclass that enforces the singleton pattern, allowing only one instance of a class.

    Usage:
    - Define a class and set the metaclass to Singleton to ensure only one instance of that class exists.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        else:
            # Modify the existing instance's attributes
            # calling
            # project(save_file_path='', menu_stack=[], GLOBAL={}, DATA_W=False)
            # with existing instance will cause
            # cls._instances[cls] = super().__call__(*args, **kwargs)
            #                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            # TypeError: project.__init__() got an unexpected keyword argument 'gen'
            # because dataclasse instance don't expect arg/kwarg
            # (thx chat GPT) (i could have done it be myself but it's so obscure)
            instance = cls._instances[cls]
            for key, value in kwargs.items():
                if hasattr(instance, key):
                    setattr(instance, key, value)
        return cls._instances[cls]

class board(object):
    """
    Represents a board object.

    Attributes:
    board (list): The current state of the board.
    size (tuple): the size of the board

    Methods:
    __init__(self): Initializes the board object.
    is_win(self): Checks if the current board state represents a win.
    get_moves(self): Returns a list of possible moves on the board.
    apply(self, move): Applies a move to the board, updating its state.

    Note:
    This class is meant to be subclassed, and the methods `is_win`, `get_moves`, and `apply`
    should be implemented in the subclasses.
    """

    def __init__(self):
        super()
        self.board = []
        self.size = (1,1)

    def is_win(self):
        raise NotImplementedError()

    def get_moves(self):
        raise NotImplementedError()

    def apply(self,move):
        raise NotImplementedError()

###############################################

def search_empty(tree, queue, lv, max_depth):
    """
    Recursively find all empty path values in the tree.
    """
    if max_depth > 0 and len(lv) > max_depth:
        return
    for k, v in tree.items():
        if v[2] is None:
            queue.append((*lv,k))
        else:
            search_empty(v[2], queue, (*lv,k), max_depth)


def recursive_search(tree, depth):
    """
    Recursively searches through the tree and returns a list of winning moves.

    Args:
    tree (tuple): The search tree in the format (value, is_win, sub_tree).
    depth (int): The current depth in the search tree.

    Returns:
    hash : winning moves.
    """
    value, is_win, sub_tree = list(tree)
    if sub_tree is None:
        return value,is_win , None # leaf node
    
    best_mov = None
    for x in sub_tree.keys():
        m = recursive_search(sub_tree[x], depth+1)
        if m is None:
            continue
        sub_v , win , move = list(m)
        if move is None and win and depth %2 ==0:
            # leaf node case
            best_mov = (sub_v,win,x)
            break
    if depth == 0:
        if best_mov is not None:
            return best_mov[2]
        else:
            return random.choice(list(sub_tree.keys()))
    else:
        return best_mov



def minmax_s(_board : board,cache=None, max_depth=3, max_time=5):
    """
    Performs a minimax search on a given board object to find the optimal move.

    Args:
    _board (board): The board object representing the current state of the game.
    cache (dict, optional): A dictionary to store the search tree for caching purposes. Defaults to None.
    max_depth (int, optional): The maximum depth of the search tree. Defaults to 3.
    max_time (int, optional): The maximum time in seconds allowed for the search. Defaults to 5.

    Returns:
    dict: The search tree representing the optimal moves and their values.
    """
    
    start_time = time.time()
    
    # Initialize the queue with the initial state
    t_board = copy.deepcopy(_board)
    tree = {key : (None,False,None) for key in t_board.get_moves()} if cache is None else cache
    queu = []
    search_empty(tree,queu,(),max_depth)
    
    while (max_time > 0 or time.time() - start_time >= max_time) and queu: # not not faster to conv to bool
        # go to queu board
        # print(len(queu),queu[0])
        board = copy.deepcopy(_board)
        moves = queu.pop(0)
        for x in moves[:-1]:
            board.apply(x)
        v = board.apply(moves[-1])
        win = board.is_win()
        # print(board)
        t = tree
        for k in moves[:-1]:
            t = t[k][2]
        # Check if the maximum depth has been reached
        if max_depth > 0 and len(moves)+1 > max_depth :
            # print(t,moves)
            t[moves[-1]] = (v,win,None)
            # print("max_depth")
            continue
        if not win:
            # calculate poss and add to queu
            keys = board.get_moves()
            t[moves[-1]] = (v,win, {key : (None,False,None) for key in keys})
            for key in keys:
                queu.append((*moves,key))
    
    return (tree,recursive_search((0,False,tree),0))

minmax = minmax_s