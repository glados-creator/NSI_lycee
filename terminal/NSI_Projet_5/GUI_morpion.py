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
    import morpion as mor
except Exception as ex:
    try:
        ex.add_note("morpion.py fichier manquant")
        ex.add_note("merci d'avoir tout le projet pour une collection valide")
    except:
        print("morpion.py fichier manquant")
        print("merci d'avoir tout le projet pour une collection valide")
    raise ex

__all__ = ["jouer_morpion"]


def jouer_morpion(state: gstate):
    handy_backbtn(state)

    if not "morpion_size" in dir(state.other):
        state.other.morpion_size = tk.IntVar(master=state.grid, value=3)

    if "board" not in state.g_other.dict:
        state.g_other.dict["board"] = mor.MorpionBoard(state.other.morpion_size.get())
    globals()["cache"] = {key: (None, False, None) for key in state.g_other.dict["board"].get_moves()}
    state.g_other.dict["morpion_grid"] = [[None] * state.other.morpion_size.get() for _ in range(state.other.morpion_size.get())]
    scorex = tk.IntVar(state.grid, value=0)
    scoreo = tk.IntVar(state.grid, value=0)
    state.g_other.dict["poss"] = state.g_other.dict["board"].get_moves()

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
        state.g_other.dict.pop("board",None)
        state.dispatch()

    state.Button(master=state.grid, command=lambda: state.dispatch(),text="actualiser").grid(row=2,column=0)
    state.Button(master=state.grid, command=lambda: _reset(),text="reset").grid(row=2,column=2)
    
    # score
    m = state.Frame(state.grid)
    l = state.Frame(m)
    state.Label(l, text="Score X").pack(side="left")
    state.Label(l, textvariable=scorex).pack(side="right")
    l.pack()

    l = state.Frame(m)
    state.Label(l, text="Score O").pack(side="left")
    state.Label(l, textvariable=scoreo).pack(side="right")
    l.pack()
    m.grid(row=0, column=2)

    think = tk.IntVar(master=state.grid, value=0)
    num_players = tk.IntVar(master=state.grid, value=2)

    def _win():
        state.Label(master=state.grid, text=textU("la partie est finie")).grid(row=0,rowspan=2,column=1)
        if scorex.get() > 99:
            state.Label(master=state.grid, text=textU("X gagne")).grid(row=1,column=1)
        else:
            state.Label(master=state.grid, text=textU("O gagne")).grid(row=1,column=1)
        state.g_other.dict.pop("board",None)

    def _click(i: int, j: int, can):
        if num_players.get() == 0:
            num_players.set(1)
        x = mor.coord_to_index(i, j,state.other.morpion_size.get())
        try:
            board = state.g_other.dict["board"]
        except:
            for row in state.g_other.dict["morpion_grid"]:
                for cell in row:
                    _draw(cell)
            return
        poss = board.get_moves()
        state.g_other.dict["poss"] = poss
        if not poss:
            think.set(1)
        if think.get() == 0 and x in poss:
            think.set(1)
            if num_players.get() == 1:  # Player vs Bot mode
                scorex.set(scorex.get() + board.apply(x))
                if not board.is_win():
                    cache, move = mor.algo.minmax(board, globals()["cache"][x][2])
                    scoreo.set(scoreo.get() + board.apply(move))
                    cache = cache[move][2]
                    globals()["cache"] = cache

                if not board.is_win():
                    think.set(0)
            elif num_players.get() == 2:  # Player vs Player mode
                if board.current_player == "X":
                    scorex.set(scorex.get() + board.apply(x))
                    num_players_spinbox.configure(state="disable")
                elif board.current_player == "O":
                    scoreo.set(scoreo.get() + board.apply(x))
                    num_players_spinbox.configure(state="normal")
                else:
                    raise Exception("Invalid player")
                if not board.is_win():
                    think.set(0)

        for row in state.g_other.dict["morpion_grid"]:
            for cell in row:
                _draw(cell)

        if think.get() == 1:
            return _win()

    def _draw(cell):
        i, j, can = cell
        # redraw
        try:
            w = can.winfo_width()
            h = can.winfo_height()
            can.create_rectangle(0, 0, w, h, fill="grey")
            x = state.g_other.dict["board"].board[mor.coord_to_index(i, j,state.other.morpion_size.get())]
            if x == "X":
                can.create_line(0, 0, w, h, fill="red", width=15)
                can.create_line(w, 0, 0, h, fill="red", width=15)
            elif x == "O":
                # O
                can.create_oval(0, 0, w, h, width=15, outline="blue")
            elif mor.coord_to_index(i, j,state.other.morpion_size.get()) in state.g_other.dict["poss"]:
                can.create_oval(2 * w // 5, 2 * h // 5, 3 * w//5, 3 * h//5, width=10, outline="green")
            can.update()
        except Exception:
            pass

    def _handle_w(can, i: int, j: int): pass

    def _create(master, i, j, *args, **kwargs):
        f = state.Frame(master)
        c = state.Canvas(f, *args, **kwargs)
        c.bind("<ButtonPress>", lambda e: _click(i, j, c))
        # c.bind("<<draw>>", lambda e: _draw(i, j, c))
        # does not work with ctk :(
        c.pack()
        state.g_other.dict["morpion_grid"][i][j] = (i, j, c)
        return f


    grid_w = state.Frame(state.grid)
    grid_w.grid(row=1, column=1, rowspan=1, columnspan=1)

    def _handle_board():
        handy_config(grid_w, state.other.morpion_size.get())

        handy_grid(repeatewidget_func=_create, master=grid_w, rows=state.other.morpion_size.get(),
                   binding=_handle_w, bg="yellow", width=100, height=100)
        for row in state.g_other.dict["morpion_grid"]:
            for cell in row:
                _draw(cell)
        grid_w.update()
        for row in state.g_other.dict["morpion_grid"]:
            for cell in row:
                _draw(cell)
        grid_w.update()
        # print(state.g_other.dict["board"].board)
    _handle_board()

    def _change_grid():
        board = state.g_other.dict["board"]
        old_size = board.size
        new_size = state.other.morpion_size.get()
        board.size = new_size
        new_board = [None] * (new_size ** 2)

        if new_size < old_size:
            # Calculate the new board
            for i in range(new_size):
                for j in range(new_size):
                    if i < old_size and j < old_size:
                        new_board[mor.coord_to_index(i, j, new_size)] = board.board[mor.coord_to_index(i, j, old_size)]

        elif new_size > old_size:
            # Calculate the new board
            for i in range(old_size):
                for j in range(old_size):
                    new_i = i + (i // old_size)  # Adjust the row index for the new size
                    new_j = j + (j // old_size)  # Adjust the column index for the new size
                    new_board[new_i * new_size + new_j] = board.board[mor.coord_to_index(i, j, old_size)]

        board.board = new_board
        state.dispatch()

    boxes = state.Frame(state.grid)
    state.Label(boxes, text="taille").pack()
    board_size_spinbox = state.Spinbox(boxes, from_=3, to=6, textvariable=state.other.morpion_size, command=_change_grid)
    board_size_spinbox.pack()
    state.Label(boxes, text="nb joueur").pack()
    num_players_spinbox = state.Spinbox(boxes, from_=1, to=2, textvariable=num_players)
    num_players_spinbox.pack()
    boxes.grid(row=1, column=2)



if __name__ == "__main__":
    default_main(jouer_morpion)
