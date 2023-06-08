try:
    import algorithm as algo
except Exception as ex:
    try:
        ex.add_note("algorithm.py fichier manquant")
        ex.add_note("merci d'avoir tout le projet pour une collection valide")
    except:
        print("algorithm.py fichier manquant")
        print("merci d'avoir tout le projet pour une collection valide")
    raise ex

def coord_to_index(x, y, n=3):
    return x * n + y

def index_to_coord(i, n=3):
    x = i // n
    y = i % n
    return x, y

class MorpionBoard(algo.board):
    """
    Simple example MorpionBoard
    Implements .get_move, .is_win, .apply
    """
    X = 'X'
    O = 'O'

    def __init__(self, n=3):
        super().__init__()
        self.board = [None] * (n * n)
        self.current_player = self.X
        self.size = n

    def apply(self, index):
        x, y = index_to_coord(index, self.size)
        self.board[index] = self.current_player
        if self.is_win():
            return 100
        futur_win_pattern = []
        n = self.size

        # Generate patterns around each cell like a king in chess

        # Horizontal pattern: Check left and right cells
        futur_win_pattern.append([
            coord_to_index(x, y-1, n),
            coord_to_index(x, y+1, n)
        ])

        # Vertical pattern: Check above and below cells
        futur_win_pattern.append([
            coord_to_index(x-1, y, n),
            coord_to_index(x+1, y, n)
        ])

        # Diagonal pattern 1: Top-left and bottom-right cells
        futur_win_pattern.append([
            coord_to_index(x-1, y-1, n),
            coord_to_index(x+1, y+1, n)
        ])

        # Diagonal pattern 2: Top-right and bottom-left cells
        futur_win_pattern.append([
            coord_to_index(x-1, y+1, n),
            coord_to_index(x+1, y-1, n)
        ])

        # Check if any of the patterns result in a win
        for pattern in futur_win_pattern:
            if (
                pattern[0] >= 0 and pattern[0] < len(self.board) and
                pattern[1] >= 0 and pattern[1] < len(self.board) and
                self.board[pattern[0]] is not None and
                self.board[pattern[1]] is not None and
                self.board[pattern[0]] == self.board[pattern[1]] == self.current_player
            ):
                self.current_player = self.X if self.current_player == self.O else self.O
                return 5
        self.current_player = self.X if self.current_player == self.O else self.O
        return 1



    def is_win(self):
        n = int(len(self.board) ** 0.5)

        # Check horizontal lines
        for row in range(n):
            for col in range(n - 2):
                index = row * n + col
                if (
                    self.board[index] is not None
                    and self.board[index] == self.board[index + 1] == self.board[index + 2]
                ):
                    return self.board[index]

        # Check vertical lines
        for col in range(n):
            for row in range(n - 2):
                index = row * n + col
                if (
                    self.board[index] is not None
                    and self.board[index] == self.board[index + n] == self.board[index + 2 * n]
                ):
                    return self.board[index]

        # Check diagonal lines (top-left to bottom-right)
        for row in range(n - 2):
            for col in range(n - 2):
                index = row * n + col
                if (
                    self.board[index] is not None
                    and self.board[index] == self.board[index + n + 1] == self.board[index + 2 * n + 2]
                ):
                    return self.board[index]

        # Check diagonal lines (top-right to bottom-left)
        for row in range(n - 2):
            for col in range(2, n):
                index = row * n + col
                if (
                    self.board[index] is not None
                    and self.board[index] == self.board[index + n - 1] == self.board[index + 2 * n - 2]
                ):
                    return self.board[index]

        return False




    def get_moves(self):
        moves = []
        for i in range(len(self.board)):
            if self.board[i] is None:
                moves.append(i)
        return moves


    def __str__(self):
        n = self.size
        rows = []
        for i in range(0, len(self.board), n):
            row = " | ".join(str(self.board[i + j]) if self.board[i + j] is not None else " " for j in range(n))
            rows.append(row)
        return "\n".join(rows)



if __name__ == "__main__":
    # play Morpion dans le terminal
    board = MorpionBoard()
    cache = {key : (None,False,None) for key in board.get_moves()}
    scorex = 0
    scoreo = 0
    while True:
        # player tour
        print("-"*20)
        print("au tour du joueur X:")
        print(board) 
        poss = board.get_moves()
        b = True
        while b:
            inp = input("coups : ")
            for x in poss:
                if inp == str(x):
                    b = 0
                    break
            else:
                print("invalide")
        add = board.apply(x)
        print("score X :",scorex,"+",add,"=",scorex + add)
        scorex = scorex + add
        if scorex > 99:
            break
        print("-"*20)
        print("au tour de l'ordinateur")
        # print(cache)
        cache , move = algo.minmax(board,cache[x][2])
        add = board.apply(move)
        print("score O :",scoreo,"+",add,"=",scoreo + add)
        scoreo = scoreo + add
        cache = cache[move][2]
        if scoreo > 99:
            break
    print("-"*20)
    print("fini")
    print("score X :",scorex)
    print("score O :",scoreo)
    print(board)