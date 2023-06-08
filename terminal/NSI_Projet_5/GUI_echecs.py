import time

try:
    from GUI_helper import *
except Exception as ex:
    try:
        ex.add_note("GUI_helper.py fichier manquant")
        ex.add_note("merci d'avoir tout le projet pour une collection valide")
    except:
        print("GUI_helper.py fichier manquant")
        print("merci d'avoir tout le projet pour une collection valide")
    raise ex

try:
    import echecs as ec
except Exception as ex:
    try:
        ex.add_note("echecs.py fichier manquant")
        ex.add_note("merci d'avoir tout le projet pour une collection valide")
    except:
        print("echecs.py fichier manquant")
        print("merci d'avoir tout le projet pour une collection valide")
    raise ex

__all__ = ["jouer_echecs"]


def jouer_echecs(state: gstate):
    handy_backbtn(state)

    if "board" not in state.g_other.dict:
        state.g_other.dict["board"] = ec.ChessBoard()
    globals()["cache"] = {key: (None, False, None) for key in state.g_other.dict["board"].get_moves()}

    state.g_other.dict["echecs_grid"] = [[None] * 8 for _ in range(8)]
    score1 = tk.IntVar(state.grid, value=0)
    score2 = tk.IntVar(state.grid, value=0)
    state.g_other.dict["poss"] = []

    # clock
    clock = tk.StringVar()
    start = time.perf_counter()
    clock.set("0")

    txt_clock = state.Label(master=state.grid, textvariable=clock)

    def _update_time():
        clock.set(f"chrono :{time.perf_counter()-start:.2f} sec")
        txt_clock.after(40, _update_time)

    txt_clock.after(20, _update_time)
    txt_clock.grid(row=0, column=1)

    def _reset():
        state.g_other.dict.pop("board", None)
        state.dispatch()

    state.Button(master=state.grid, command=lambda: state.dispatch(), text="actualiser").grid(row=2, column=0)
    state.Button(master=state.grid, command=lambda: _reset(), text="reset").grid(row=2, column=2)

    # score
    m = state.Frame(state.grid)
    l = state.Frame(m)
    state.Label(l, text="Score 1").pack(side="left")
    state.Label(l, textvariable=score1).pack(side="right")
    l.pack()

    l = state.Frame(m)
    state.Label(l, text="Score 2").pack(side="left")
    state.Label(l, textvariable=score2).pack(side="right")
    l.pack()
    m.grid(row=0, column=2)

    think = tk.IntVar(master=state.grid, value=0)
    num_players = tk.IntVar(master=state.grid, value=2)

    def _win():
        state.Label(master=state.grid, text=textU("la partie est finie")).grid(row=0, rowspan=2, column=1)
        if score1.get() > score2.get():
            state.Label(master=state.grid, text=textU("Joueur 1 gagne")).grid(row=1, column=1)
        elif score1.get() < score2.get():
            state.Label(master=state.grid, text=textU("Joueur 2 gagne")).grid(row=1, column=1)
        else:
            state.Label(master=state.grid, text=textU("Match nul")).grid(row=1, column=1)
        state.g_other.dict.pop("board", None)

    selected_piece = None

    def _click(i: int, j: int, can):
        print("click",[print(x) for x in state.g_other.dict["board"].board])
        if num_players.get() == 1:
            for row in state.g_other.dict["echecs_grid"]:
                for cell in row:
                    _draw(cell)

        try:
            board = state.g_other.dict["board"]
        except:
            for row in state.g_other.dict["echecs_grid"]:
                for cell in row:
                    _draw(cell)
            return

        if selected_piece is not None:
            poss = board.get_moves_for_piece(selected_piece)
            state.g_other.dict["poss"] = poss
            if not poss:
                think.set(1)
            if think.get() == 0 and (i, j) in poss:
                think.set(1)
                if num_players.get() == 1:  # Player vs Bot mode
                    score1.set(score1.get() + board.apply(selected_piece, (i, j)))
                    if not board.is_win():
                        cache, move = ec.algo.minmax(board, globals()["cache"][selected_piece][2])
                        score2.set(score2.get() + board.apply(move))
                        cache = cache[move][2]
                        globals()["cache"] = cache

                    if not board.is_win():
                        think.set(0)
                elif num_players.get() == 2:  # Player vs Player mode
                    score = board.apply(selected_piece, (i, j))
                    if score:
                        if score > 0:
                            score1.set(score1.get() + score)
                        else:
                            score2.set(score2.get() - score)
                        if not board.is_win():
                            think.set(0)
                    else:
                        return
                else:
                    raise Exception("Invalid player")
        else:
            poss = []
            state.g_other.dict["poss"] = poss

        for row in state.g_other.dict["echecs_grid"]:
            for cell in row:
                _draw(cell)

        if think.get() == 1:
            return _win()


    def _draw(cell):
        print("draw")
        i, j, can = cell
        try:
            w = can.winfo_width()
            h = can.winfo_height()
            can.create_rectangle(0, 0, w, h, fill="grey")

            piece = state.g_other.dict["board"].board[i][j]
            print(piece)
            possible_moves = state.g_other.dict.get("poss")

            # Highlight the selected piece and its possible moves
            if piece is not None:
                piece_label = f"{piece.piece_type}\n{piece.player_type}"
                if piece == selected_piece:
                    can.create_rectangle(0, 0, w, h, outline="blue", width=2)
                elif (i, j) in possible_moves:
                    can.create_rectangle(0, 0, w, h, outline="green", width=2)
                can.create_text(w/2, h/2, text=piece_label, font=("Arial", 12), fill="black")

            can.update()
        except Exception:
            pass


    
    def _handle_w(can, i: int, j: int): pass

    def _create(master, i, j, *args, **kwargs):
        f = state.Frame(master)
        c = state.Canvas(f, *args, **kwargs)
        c.bind("<ButtonPress>", lambda e: _click(i, j, c))
        c.pack()
        state.g_other.dict["echecs_grid"][i][j] = (i, j, c)
        return f

    grid_w = state.Frame(state.grid)
    grid_w.grid(row=1, column=1, rowspan=1, columnspan=1)

    def _handle_board():
        handy_config(grid_w, 8)

        handy_grid(repeatewidget_func=_create, master=grid_w, rows=8,
                binding=_handle_w, bg="yellow", width=50, height=50)
        for row in state.g_other.dict["echecs_grid"]:
            for cell in row:
                _draw(cell)
        grid_w.update()

    _handle_board()

    def _change_grid():
        board = state.g_other.dict["board"]
        old_size = 8
        new_size = 8
        board.size = new_size
        board.board = copy.deepcopy(ec.default_board)
        state.dispatch()

    boxes = state.Frame(state.grid)
    state.Label(boxes, text="nb joueur").pack()
    num_players_spinbox = state.Spinbox(boxes, from_=1, to=2, textvariable=num_players)
    num_players_spinbox.pack()
    boxes.grid(row=1, column=2)


if __name__ == "__main__":
    default_main(jouer_echecs)