import copy
import dataclasses
import enum
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

def alpha_to_position(position):
    """
    Maps a chess game position (e.g. 'e1') to a zero-indexed (x, y) tuple,
    where (0, 0) is the top left corner of the board.
    """
    file_names = 'abcdefgh'
    file_index = file_names.index(position[0])
    rank_index = int(position[1]) - 1
    return (file_index, rank_index)

class piece_t(enum.Enum):
    K = "K",  # King
    Q = "Q",  # Queen
    R = "R",  # Rook (also known as a castle)
    B = "B",  # Bishop
    N = "N",  # Knight (also known as a horse)
    P = "P"  # Pawn


class player_t(enum.Enum):
    W = "W",  # White
    B = "B"  # Black


@dataclasses.dataclass
class piece:
    __slots__ = ["player","type","position"]
    player: player_t
    type: piece_t
    position: tuple


piece_value_win = {
    piece_t.K: 99,
    piece_t.Q: 20,
    piece_t.R: 15,
    piece_t.B: 10,
    piece_t.N: 5,
    piece_t.P: 3
}

default_board = [
    piece(player_t.W, piece_t.K, (4, 0)),
    piece(player_t.W, piece_t.Q, (3, 0)),
    piece(player_t.W, piece_t.R, (0, 0)),
    piece(player_t.W, piece_t.R, (7, 0)),
    piece(player_t.W, piece_t.B, (2, 0)),
    piece(player_t.W, piece_t.B, (5, 0)),
    piece(player_t.W, piece_t.N, (1, 0)),
    piece(player_t.W, piece_t.N, (6, 0)),
    piece(player_t.W, piece_t.P, (0, 1)),
    piece(player_t.W, piece_t.P, (1, 1)),
    piece(player_t.W, piece_t.P, (2, 1)),
    piece(player_t.W, piece_t.P, (3, 1)),
    piece(player_t.W, piece_t.P, (4, 1)),
    piece(player_t.W, piece_t.P, (5, 1)),
    piece(player_t.W, piece_t.P, (6, 1)),
    piece(player_t.W, piece_t.P, (7, 1)),
    piece(player_t.B, piece_t.K, (4, 7)),
    piece(player_t.B, piece_t.Q, (3, 7)),
    piece(player_t.B, piece_t.R, (0, 7)),
    piece(player_t.B, piece_t.R, (7, 7)),
    piece(player_t.B, piece_t.B, (2, 7)),
    piece(player_t.B, piece_t.B, (5, 7)),
    piece(player_t.B, piece_t.N, (1, 7)),
    piece(player_t.B, piece_t.N, (6, 7)),
    piece(player_t.B, piece_t.P, (0, 6)),
    piece(player_t.B, piece_t.P, (1, 6)),
    piece(player_t.B, piece_t.P, (2, 6)),
    piece(player_t.B, piece_t.P, (3, 6)),
    piece(player_t.B, piece_t.P, (4, 6)),
    piece(player_t.B, piece_t.P, (5, 6)),
    piece(player_t.B, piece_t.P, (6, 6)),
    piece(player_t.B, piece_t.P, (7, 6))
]

class ChessBoard(algo.board):
    def __init__(self):
        super()
        self.size = (8,8)
        self.board = copy.deepcopy(default_board)
        self.current_player_color = player_t.W

    def is_win(self):
        # Check for checkmate or stalemate

        # Step 1: Check if the current player is in check
        king_position = None
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece is not None and piece.type == piece_t.K and piece.color == self.current_player_color:
                    king_position = (i, j)
                    break
            if king_position is not None:
                break

        if king_position is None:
            # Unable to find the current player's king
            return False

        # Step 2: Check if the king can move to a safe position
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue

                new_x = king_position[0] + i
                new_y = king_position[1] + j

                if new_x < 0 or new_x > 7 or new_y < 0 or new_y > 7:
                    continue

                if self.board[new_x][new_y] is None or self.board[new_x][new_y].color != self.current_player_color:
                    # The king can move to a safe position, so it's not a checkmate
                    return False

        # Step 3: Check if any piece can capture the threatening piece
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece is not None and piece.color == self.current_player_color:
                    possible_moves = self.get_moves(board, i, j)
                    for move in possible_moves:
                        new_x, new_y = move
                        if board[new_x][new_y] is not None and board[new_x][new_y].color != current_player_color:
                            # There is at least one piece that can capture the threatening piece
                            return False

        # If none of the above conditions are met, it's a checkmate or stalemate
        return True

    def get_move_for_piece(self,x,y):
        piece = self.board[x][y]

        if piece.type == piece_t.K:
            # King
            moves = [
                [x-1, y+1], [x, y+1], [x+1, y+1],
                [x-1, y],             [x+1, y],
                [x-1, y-1], [x, y-1], [x+1, y-1]
            ]

            valid_moves = []
            for move in moves:
                new_x, new_y = move
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    if self.board[new_x][new_y] is None or self.board[new_x][new_y].color != piece.color:
                        valid_moves.append(move)
            return valid_move
        
        elif piece.type == piece_t.P:
            # Pawn
            moves = []

            if piece.color == color_t.WHITE:
                # Forward move
                if x - 1 >= 0 and self.board[x - 1][y] is None:
                    moves.append([x - 1, y])
                    # Double forward move from starting position
                    if x == 6 and self.board[4][y] is None:
                        moves.append([4, y])

                # Diagonal captures
                if x - 1 >= 0 and y - 1 >= 0:
                    if self.board[x - 1][y - 1] is not None and self.board[x - 1][y - 1].color == color_t.BLACK:
                        moves.append([x - 1, y - 1])
                    # En passant capture
                    if x - 1 == 3 and self.board[x][y - 1] is not None and self.board[x][y - 1].type == piece_t.P and self.board[x][y - 1].color == color_t.BLACK and self.board[x - 1][y - 1] is None:
                        moves.append([x - 1, y - 1])
                    if self.board[x - 1][y + 1] is not None and self.board[x - 1][y + 1].color == color_t.BLACK:
                        moves.append([x - 1, y + 1])
                    # En passant capture
                    if x - 1 == 3 and self.board[x][y + 1] is not None and self.board[x][y + 1].type == piece_t.P and self.board[x][y + 1].color == color_t.BLACK and self.board[x - 1][y + 1] is None:
                        moves.append([x - 1, y + 1])

            else:  # BLACK pawn
                # Forward move
                if x + 1 < 8 and self.board[x + 1][y] is None:
                    moves.append([x + 1, y])
                    # Double forward move from starting position
                    if x == 1 and self.board[3][y] is None:
                        moves.append([3, y])

                # Diagonal captures
                if x + 1 < 8 and y - 1 >= 0:
                    if self.board[x + 1][y - 1] is not None and self.board[x + 1][y - 1].color == color_t.WHITE:
                        moves.append([x + 1, y - 1])
                    # En passant capture
                    if x + 1 == 4 and self.board[x][y - 1] is not None and self.board[x][y - 1].type == piece_t.P and self.board[x][y - 1].color == color_t.WHITE and self.board[x + 1][y - 1] is None:
                        moves.append([x + 1, y - 1])
                    if self.board[x + 1][y + 1] is not None and self.board[x + 1][y + 1].color == color_t.WHITE:
                        moves.append([x + 1, y + 1])
                    # En passant capture
                    if x + 1 == 4 and self.board[x][y + 1] is not None and self.board[x][y + 1].type == piece_t.P and self.board[x][y + 1].color == color_t.WHITE and self.board[x + 1][y + 1] is None:
                        moves.append([x + 1, y + 1])

            return moves
        
        elif piece.type == piece_t.R:
            # Rook
            moves = []

            # Horizontal moves to the right
            for i in range(x + 1, 8):
                if self.board[i][y] is None:
                    moves.append([i, y])
                else:
                    if self.board[i][y].color != piece.color:
                        moves.append([i, y])
                    break

            # Horizontal moves to the left
            for i in range(x - 1, -1, -1):
                if self.board[i][y] is None:
                    moves.append([i, y])
                else:
                    if self.board[i][y].color != piece.color:
                        moves.append([i, y])
                    break

            # Vertical moves upwards
            for j in range(y + 1, 8):
                if self.board[x][j] is None:
                    moves.append([x, j])
                else:
                    if self.board[x][j].color != piece.color:
                        moves.append([x, j])
                    break

            # Vertical moves downwards
            for j in range(y - 1, -1, -1):
                if self.board[x][j] is None:
                    moves.append([x, j])
                else:
                    if self.board[x][j].color != piece.color:
                        moves.append([x, j])
                    break

            return moves
        
        elif piece.type == piece_t.B:
            # Bishop
            moves = []

            # Diagonal moves to the top-right
            i = x + 1
            j = y + 1
            while i < 8 and j < 8:
                if self.board[i][j] is None:
                    moves.append([i, j])
                else:
                    if self.board[i][j].color != piece.color:
                        moves.append([i, j])
                    break
                i += 1
                j += 1

            # Diagonal moves to the top-left
            i = x + 1
            j = y - 1
            while i < 8 and j >= 0:
                if self.board[i][j] is None:
                    moves.append([i, j])
                else:
                    if self.board[i][j].color != piece.color:
                        moves.append([i, j])
                    break
                i += 1
                j -= 1

            # Diagonal moves to the bottom-right
            i = x - 1
            j = y + 1
            while i >= 0 and j < 8:
                if self.board[i][j] is None:
                    moves.append([i, j])
                else:
                    if self.board[i][j].color != piece.color:
                        moves.append([i, j])
                    break
                i -= 1
                j += 1

            # Diagonal moves to the bottom-left
            i = x - 1
            j = y - 1
            while i >= 0 and j >= 0:
                if self.board[i][j] is None:
                    moves.append([i, j])
                else:
                    if self.board[i][j].color != piece.color:
                        moves.append([i, j])
                    break
                i -= 1
                j -= 1

            return moves
        
        elif piece.type == piece_t.N:
            # Knight
            moves = []

            possible_moves = [
                (x + 2, y + 1),
                (x + 2, y - 1),
                (x - 2, y + 1),
                (x - 2, y - 1),
                (x + 1, y + 2),
                (x + 1, y - 2),
                (x - 1, y + 2),
                (x - 1, y - 2),
            ]

            for move in possible_moves:
                i, j = move
                if 0 <= i < 8 and 0 <= j < 8:
                    if self.board[i][j] is None or self.board[i][j].color != piece.color:
                        moves.append([i, j])

            return moves
        
        elif piece.type == piece_t.Q:
            # Queen
            moves = []

            # Bishop-like moves (diagonal)
            for i in range(1, 8):
                if x + i < 8 and y + i < 8:
                    if self.board[x + i][y + i] is None or self.board[x + i][y + i].color != piece.color:
                        moves.append([x + i, y + i])
                        if self.board[x + i][y + i] is not None:
                            break
                else:
                    break

            for i in range(1, 8):
                if x + i < 8 and y - i >= 0:
                    if self.board[x + i][y - i] is None or self.board[x + i][y - i].color != piece.color:
                        moves.append([x + i, y - i])
                        if self.board[x + i][y - i] is not None:
                            break
                else:
                    break

            for i in range(1, 8):
                if x - i >= 0 and y + i < 8:
                    if self.board[x - i][y + i] is None or self.board[x - i][y + i].color != piece.color:
                        moves.append([x - i, y + i])
                        if self.board[x - i][y + i] is not None:
                            break
                else:
                    break

            for i in range(1, 8):
                if x - i >= 0 and y - i >= 0:
                    if self.board[x - i][y - i] is None or self.board[x - i][y - i].color != piece.color:
                        moves.append([x - i, y - i])
                        if self.board[x - i][y - i] is not None:
                            break
                else:
                    break

            # Rook-like moves (horizontal and vertical)
            for i in range(x + 1, 8):
                if self.board[i][y] is None or self.board[i][y].color != piece.color:
                    moves.append([i, y])
                    if self.board[i][y] is not None:
                        break
                else:
                    break

            for i in range(x - 1, -1, -1):
                if self.board[i][y] is None or self.board[i][y].color != piece.color:
                    moves.append([i, y])
                    if self.board[i][y] is not None:
                        break
                else:
                    break

            for j in range(y + 1, 8):
                if self.board[x][j] is None or self.board[x][j].color != piece.color:
                    moves.append([x, j])
                    if self.board[x][j] is not None:
                        break
                else:
                    break

            for j in range(y - 1, -1, -1):
                if self.board[x][j] is None or self.board[x][j].color != piece.color:
                    moves.append([x, j])
                    if self.board[x][j] is not None:
                        break
                else:
                    break

            return moves
        
        else:
            raise ValueError()

    def get_moves(self):
        return []

    def apply(self,move):
        raise NotImplementedError()