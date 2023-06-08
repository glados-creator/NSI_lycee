import os
import tkinter as tk
import myc
import my_parser
import resolver
import time
try:
    import gen
except Exception as ex:
    print(ex)
    gen = None


def handy_create_grid_N(master):
    def _left_click_handler(button, i, j):
        def _left_click(*event):
            c = myc.project().DATA[i][j]
            if c == 3:
                # green -> whitec = 3
                c = True
                button.configure(background="#ffffff")
            elif c == 2:
                # red (start) -> green (goal)
                c = 3
                button.configure(background="#00ff00")
            elif c:
                # black -> red
                c = 2
                button.configure(background="#ff0000")
            elif not c:
                # white -> red
                c = 2
                button.configure(background="#ff0000")
            else:
                print("how did we get here")
                c = True
                button.configure(background="#ffffff")
            myc.project().DATA[i][j] = c
            my_parser.quick_cache_save()
        return _left_click

    def _change(button, i, j):
        def inner():
            c = myc.project().DATA[i][j]
            c = not c
            myc.project().DATA[i][j] = c
            button.configure(background=("#000000" if c else "#ffffff"))
            my_parser.quick_cache_save()
        return inner
    if myc.project().DATA_W:
        raise RuntimeError("handy_create_grid with weighted data")
    if myc.project().DATA is None or myc.project.get_size()[0] == 0:
        # by the default load there is no data
        print("no data so default one")
        myc.project().DATA = [[1, 0, 1], [0, 0, 1], [1, 1, 1]]
    lab = myc.project().DATA
    # myc.project().GLOBAL["grid_nboutton"] = []
    for i, row in enumerate(lab):
        # myc.project().GLOBAL["grid_nboutton"].append([])
        for j, element in enumerate(row):
            color = "#000000"
            if element == 4:
                myc.project().DATA[i][j] = 0
                color = "#ffffff"
            elif element == 3:
                # green
                color = "#00ff00"
            elif element == 2:
                # red (start)
                color = "#ff0000"
            elif not element:
                # white False || 0
                color = "#ffffff"
            button = tk.Button(master, height=1, width=1, text=" ",
                               highlightcolor="#b8860b", activebackground="#ffd700", background=color)
            button.configure(command=_change(button, i, j))
            button.bind("<Button-3>", _left_click_handler(button, i, j))
            button.grid(row=i, column=j)
            # myc.project().GLOBAL["grid_nboutton"][i].append(button)
            my_parser.quick_cache_save()


def handy_empty_grid():
    w = myc.project().GLOBAL["tk_window"]
    for wig in w.winfo_children():
        wig.destroy()


def handy_back_button(master):
    def _inner():
        myc.project().menu_stack.pop()
        dispatch()
    tk.Button(master, text="back", command=_inner).grid(row=0, column=0)


###! def nwswap():
###!     p = myc.project().menu_stack
###!     x = p.pop()
###!     if x == "main_n":
###!         p.append("main_w")
###!     else:
###!         p.append("main_n")


###! def main_w():
###!     # TODO
###!     print("main_w")
###!     print(myc.project())
###!     if not myc.project().DATA_W:
###!         nwswap()
###!         dispatch()
###!     window = myc.project().GLOBAL["tk_window"]
###!     handy_back_button(window)
###!     cframe = tk.Frame(window)
###!     canvas = tk.Canvas(cframe)
###!     raise


def main_n_resolver():
    if myc.project().DATA_W:
        raise RuntimeError("really not suppose to be here")
    #################################################################################

    # check no multiple entry / exit
    start_pos = None
    end_pos = None
    flag = False
    for i, row in enumerate(myc.project().DATA):
        for j, element in enumerate(row):
            if element == 2:
                if start_pos:
                    flag = True
                start_pos = element
            elif element == 3:
                if end_pos:
                    flag = True
                end_pos = element

    if flag:
        def _ok_btt():
            myc.project().menu_stack.pop()
            dispatch()
        window = myc.project().GLOBAL["tk_window"]
        tk.Label(window, text="plusieur entré ou sortie impossible").grid()
        tk.Button(window, text="ok", command=_ok_btt).grid()
        return
    my_parser.quick_cache_save()

    def create_grid_N_inner(master):
        lab = myc.project().DATA
        # myc.project().GLOBAL["grid_nboutton"] = []
        for i, row in enumerate(lab):
            # myc.project().GLOBAL["grid_nboutton"].append([])
            for j, element in enumerate(row):
                color = "#000000"
                if element == 4:
                    # visited yellow
                    color = "#ffd700"
                elif element == 3:
                    # green
                    color = "#00ff00"
                elif element == 2:
                    # red (start)
                    color = "#ff0000"
                elif not element:
                    # white False || 0
                    color = "#ffffff"
                button = tk.Button(master, height=1, width=1,
                                   text=" ", state="disabled", background=color)
                button.grid(row=i, column=j)

    window = myc.project().GLOBAL["tk_window"]
    handy_back_button(window)
    bgridframe = tk.Frame(window)
    create_grid_N_inner(bgridframe)
    bgridframe.grid(row=0, column=1, rowspan=1, columnspan=1)

    resolv = resolver.BFS if myc.project().resolver_mode == "BFS" else resolver.DFS

    #################################################################################
    control = tk.Frame(window)

    legend = tk.Frame(control)
    tk.Button(legend, state="disabled", background="#00ff00").pack()
    tk.Label(legend, text="end (3)").pack()
    tk.Button(legend, state="disabled", background="#ff0000").pack()
    tk.Label(legend, text="start (2)").pack()
    tk.Button(legend, state="disabled", background="#000000").pack()
    tk.Label(legend, text="wall (1)").pack()
    tk.Button(legend, state="disabled", background="#ffffff").pack()
    tk.Label(legend, text="free (0)").pack()
    tk.Button(legend, state="disabled", background="#ffd700").pack()
    tk.Label(legend, text="visited (4)").pack()
    legend.pack()

    myc.project().GLOBAL["STEP_STRVR"] = tk.StringVar(
        window, "0", "STEP_STRVR")

    def _change_step():
        # reset lab
        myc.project().GLOBAL["STEP_STRVR"].set(
            str(myc.project().GLOBAL.get("STEP", 0)))
        for i,row in enumerate(myc.project().DATA):
            for j,element in enumerate(row):
                if element == 4:
                    myc.project().DATA[i][j] = 0
        step = myc.project().GLOBAL.get("STEP", 0)
        step = int(step)
        visited, path = resolv(T=step)
        if visited is None:
            # all path found
            for case in path:
                lab_case = myc.project().DATA[case[0]][case[1]]
                if lab_case == 0 or lab_case == False:
                    myc.project().DATA[case[0]][case[1]] = 4
        else:
            for case in visited:
                if myc.project().DATA[case[0]][case[1]] == 0 or myc.project().DATA[case[0]][case[1]] == False:
                    myc.project().DATA[case[0]][case[1]] = 4
        dispatch()

    def _com_far_back(*args):
        myc.project().GLOBAL["STEP"] = 0
        _change_step()

    def _com_back(*args):
        if myc.project().GLOBAL.get("STEP", 0)-1 >= 0:
            myc.project().GLOBAL["STEP"] = myc.project(
            ).GLOBAL.get("STEP", 0) - 1
            _change_step()

    def _com_advance(*args):
        myc.project().GLOBAL["STEP"] = myc.project().GLOBAL.get("STEP", 0) + 1
        _change_step()

    def _com_far_advance(*args):
        # diviser pour mieux regnier
        # step E [0 ; 200]
        # si ca prend + que 200 coup il y a une autre probleme quand meme
        # et on cherche que 50 fois max et encore c'est gros
        last_big = 2000
        last_min = 0
        last_mid = 0
        counter = 0
        while counter < 50:
            mid = (last_min + last_big)//2
            if mid == last_mid:
                break
            if resolv(T=mid)[0] is None:
                # path found
                last_big = mid
            else:
                # path not found
                last_min = mid
            last_mid = mid
            counter += 1
        myc.project().GLOBAL["STEP"] = last_mid
        _change_step()

    time_str = tk.Frame(control)
    tk.Label(time_str, text="étape").pack()
    tk.Label(time_str, textvariable=myc.project().GLOBAL["STEP_STRVR"]).pack()
    time_str.pack()

    time_f = tk.Frame(control)
    tk.Button(time_f, text="⇇", command=_com_far_back).pack(side=tk.LEFT)
    tk.Button(time_f, text="←", command=_com_back).pack(side=tk.LEFT)
    tk.Button(time_f, text="→", command=_com_advance).pack(side=tk.LEFT)
    tk.Button(time_f, text="⇉", command=_com_far_advance).pack(side=tk.LEFT)
    time_f.pack()

    def _save_img():
        row , col = myc.project().get_size()
        img = tk.PhotoImage("out.png",height=row*4,width=col*4)

        lab = myc.project().DATA
        # myc.project().GLOBAL["grid_nboutton"] = []
        for i, row in enumerate(lab):
            # myc.project().GLOBAL["grid_nboutton"].append([])
            for j, element in enumerate(row):
                color = "#000000"
                if element == 4:
                    # visited yellow
                    color = "#ffd700"
                elif element == 3:
                    # green
                    color = "#00ff00"
                elif element == 2:
                    # red (start)
                    color = "#ff0000"
                elif not element:
                    # white False || 0
                    color = "#ffffff"
                img.put(color,((i*4),(j*4)))
                img.put(color,((i*4),(j*4)+1))
                img.put(color,((i*4)+1,(j*4)))
                img.put(color,((i*4)+1,(j*4)+1))
        
        time_struc = time.gmtime()
        filename = os.path.abspath(myc.project().save_file_path + f"./outimage_{time_struc.tm_hour}_{time_struc.tm_min}_{time_struc.tm_sec}.png")

        img.write(filename,format="png")

    tk.Button(control,text="save image",command=_save_img).pack()
    
    control.grid(row=0, column=2)


def main_n():
    ###! if myc.project().DATA_W:
    ###!     nwswap()
    ###!     dispatch()
    # print("main_n")
    # print(myc.project())

    #################################################################################

    window = myc.project().GLOBAL["tk_window"]
    handy_back_button(window)
    bgridframe = tk.Frame(window)
    handy_create_grid_N(bgridframe)
    bgridframe.grid(row=0, column=1, rowspan=1, columnspan=1)

    #################################################################################
    control = tk.Frame(window)

    legend = tk.Frame(control)
    tk.Button(legend, state="disabled", background="#00ff00").pack()
    tk.Label(legend, text="end (3 click droite)").pack()
    tk.Button(legend, state="disabled", background="#ff0000").pack()
    tk.Label(legend, text="start (2 click droite)").pack()
    tk.Button(legend, state="disabled", background="#000000").pack()
    tk.Label(legend, text="wall (1)").pack()
    tk.Button(legend, state="disabled", background="#ffffff").pack()
    tk.Label(legend, text="free (0)").pack()
    legend.pack()

    size_controle = tk.Frame(control)

    #################################################################################

    def _change_row_vstr():
        x = myc.project().GLOBAL["row_str"].get()
        myc.project().GLOBAL["row_str"].set(x)
        row, col = myc.project.get_size()
        try:
            x = int(x)
        except Exception as ex:
            print(ex)
            return
        if x < 0 or x == 0:
            myc.project().GLOBAL["col_str"].set("1")
            x = 1
        if x > 25:
            myc.project().GLOBAL["row_str"].set("25")
            x = 25
        if x == row:
            pass
        elif x > row:
            times = x - row
            last = myc.project().DATA[-1].copy()
            myc.project().DATA[-1] = [1, *[0 for _ in range(col-2)], 1]
            for _ in range(times - 1):
                myc.project().DATA.append([1, *[0 for _ in range(col-2)], 1])
            myc.project().DATA.append(last)
        elif x < row:
            times = row - x
            for _ in range(times):
                myc.project().DATA.pop()
        else:
            raise RuntimeError("unreachable")
        dispatch()

    def _change_col_vstr():
        x = myc.project().GLOBAL["col_str"].get()
        myc.project().GLOBAL["col_str"].set(x)
        row, col = myc.project.get_size()
        try:
            x = int(x)
        except Exception as ex:
            print(ex)
            return
        if x < 0 or x == 0:
            myc.project().GLOBAL["col_str"].set("1")
            x = 1
        if x > 25:
            myc.project().GLOBAL["col_str"].set("25")
            x = 25
        if x == col:
            pass
        elif x > col:
            times = x - col
            # idk idc i don't want to know it work
            times += 1
            last_col = []
            for row in myc.project().DATA:
                last_col.append(row.pop())
            # pop the corner because it's going to be black
            last_col.pop()
            last_col.pop(0)
            for i in range(len(myc.project().DATA)):
                row = myc.project().DATA[i]
                if i == 0 or i == len(myc.project().DATA)-1:
                    # first or last row
                    for j in range(times):
                        row.append(1)
                    continue
                for j in range(times):
                    if j == times-1:
                        row.append(last_col.pop(0))
                    else:
                        row.append(0)
        elif x < col:
            times = col - x
            for row in myc.project().DATA:
                for _ in range(times):
                    row.pop()
        else:
            raise RuntimeError("unreachable")
        dispatch()

    def _com_add_row():
        x = myc.project().GLOBAL["row_str"].get()
        try:
            x = int(x)
        except Exception as ex:
            print(ex)
            return
        if x+1 > 25:
            return
        x += 1
        x = str(x)
        myc.project().GLOBAL["row_str"].set(x)

    def _com_min_row():
        x = myc.project().GLOBAL["row_str"].get()
        try:
            x = int(x)
        except Exception as ex:
            print(ex)
            return
        if x-1 < 0:
            return
        x -= 1
        x = str(x)
        myc.project().GLOBAL["row_str"].set(x)

    def _com_add_col():
        x = myc.project().GLOBAL["col_str"].get()
        try:
            x = int(x)
        except Exception as ex:
            print(ex)
            return
        if x+1 > 25:
            return
        x += 1
        x = str(x)
        myc.project().GLOBAL["col_str"].set(x)

    def _com_min_col():
        x = myc.project().GLOBAL["col_str"].get()
        try:
            x = int(x)
        except Exception as ex:
            print(ex)
            return
        if x-1 < 0:
            return
        x -= 1
        x = str(x)
        myc.project().GLOBAL["col_str"].set(x)

    tk.Label(size_controle, text="row").grid(row=0, column=0)
    tk.Label(size_controle, text="column").grid(row=0, column=1)

    tk.Button(size_controle, text="↑",
              command=_com_add_row).grid(row=1, column=0)
    tk.Button(size_controle, text="↑",
              command=_com_add_col).grid(row=1, column=1)

    row_str = tk.StringVar(size_controle, myc.project.get_size()[0])
    col_str = tk.StringVar(size_controle, myc.project.get_size()[1])
    myc.project().GLOBAL["row_str"] = row_str
    myc.project().GLOBAL["col_str"] = col_str
    row_str.trace_add("write", lambda *args: _change_row_vstr())
    col_str.trace_add("write", lambda *args: _change_col_vstr())

    tk.Entry(size_controle, textvariable=row_str).grid(row=2, column=0)
    tk.Entry(size_controle, textvariable=col_str).grid(row=2, column=1)

    tk.Button(size_controle, text="↓",
              command=_com_min_row).grid(row=3, column=0)
    tk.Button(size_controle, text="↓",
              command=_com_min_col).grid(row=3, column=1)
    size_controle.pack(anchor="center")

    #################################################################################

    start_end = tk.Frame(control)

    def _com_auto_start_end(*args):
        myc.project().GLOBAL["start_pos"], myc.project(
        ).GLOBAL["end_pos"] = resolver.find_start_end_N(myc.project().DATA, False)
        if myc.project().GLOBAL["start_pos"] is None or myc.project().GLOBAL["end_pos"] is None:
            try:
                myc.project().GLOBAL["start_pos"], myc.project(
                ).GLOBAL["end_pos"] = resolver.find_start_end_N(myc.project().DATA)
            except Exception as ex:
                print(ex)
        dispatch()

    myc.project().GLOBAL["start_pos"], myc.project(
    ).GLOBAL["end_pos"] = resolver.find_start_end_N(myc.project().DATA, False)

    tk.Label(start_end, text="start at {}".format(
        myc.project().GLOBAL["start_pos"])).pack(side=tk.LEFT)
    tk.Label(start_end, text="end at {}".format(
        myc.project().GLOBAL["end_pos"])).pack(side=tk.RIGHT)
    tk.Button(start_end, text="auto",
              command=_com_auto_start_end).pack(side=tk.BOTTOM)

    start_end.pack()

    #################################################################################

    resolver_f = tk.Frame(control)

    def _com_resolve_BFS(*args):
        myc.project().menu_stack.append("main_n_resolver")
        myc.project().resolver_mode = "BFS"
        dispatch()

    def _com_resolver_DFS(*args):
        myc.project().menu_stack.append("main_n_resolver")
        myc.project().resolver_mode = "DFS"
        dispatch()

    tk.Button(resolver_f, text="resolver BFS",
              command=_com_resolve_BFS).pack(side=tk.LEFT)
    tk.Button(resolver_f, text="resolver DFS",
              command=_com_resolver_DFS).pack(side=tk.RIGHT)

    resolver_f.pack()

    #################################################################################

    def _com_gen(*args):
        gen.generator()
        dispatch()

    gen_frame = tk.Frame(control)
    global gen
    if gen is None:
        tk.Label(gen_frame, text="generation is not imported").pack()
    else:
        tk.Button(gen_frame, text="generate", command=_com_gen).pack()
    gen_frame.pack()

    control.grid(row=0, column=2)


def menu_init():

    def com_load_project_q():
        def _succes():
            # just in case
            if len(myc.project().menu_stack) < 2:
                myc.project().menu_stack.insert(1, "main_n")
            dispatch()
        my_parser.quick_cache_load()
        handy_empty_grid()
        f = tk.Frame(myc.project().GLOBAL["tk_window"])
        if myc.project().save_file_path or myc.project().DATA is not None:
            tk.Label(f, text="default path project loaded").pack(side=tk.TOP)
            tk.Button(f, text="ok", command=_succes, highlightcolor="#b8860b",
                      activebackground="#ffd700").pack(side=tk.BOTTOM)
        else:
            tk.Label(f, text="fail to load default project file").pack(
                side=tk.TOP)
            tk.Button(f, text="ok", command=dispatch, highlightcolor="#b8860b",
                      activebackground="#ffd700").pack(side=tk.BOTTOM)
        f.grid(column=1, row=1)

    def com_load_project_p():
        def _succes():
            if len(myc.project().menu_stack) < 2:
                myc.project().menu_stack.insert(1, "main_n")
            dispatch()
        my_parser.parse_Project_file(
            myc.project().GLOBAL["load_project_path"].get())
        handy_empty_grid()
        f = tk.Frame(myc.project().GLOBAL["tk_window"])
        if myc.project().save_file_path:
            tk.Label(f, text="{} path project loaded".format(
                myc.project().GLOBAL["load_project_path"].get())).pack(side=tk.TOP)
            tk.Button(f, text="ok", command=_succes, highlightcolor="#b8860b",
                      activebackground="#ffd700").pack(side=tk.BOTTOM)
        else:
            tk.Label(f, text="fail to load project file at path {}".format(
                myc.project().GLOBAL["load_project_path"].get())).pack(side=tk.TOP)
            tk.Button(f, text="ok", command=dispatch, highlightcolor="#b8860b",
                      activebackground="#ffd700").pack(side=tk.BOTTOM)
        f.grid(column=1, row=1)

    window = myc.project().GLOBAL["tk_window"]
    handy_back_button(window)
    f_left = tk.Frame(window)

    tk.Label(f_left, text="charger un projet").pack(side="top", anchor="n")
    tk.Button(f_left, text="auto", command=com_load_project_q,
              highlightcolor="#b8860b", activebackground="#ffd700").pack(anchor="center")
    myc.project().GLOBAL["load_project_path"] = tk.StringVar(f_left)
    tk.Entry(f_left, textvariable=myc.project(
    ).GLOBAL["load_project_path"]).pack()
    tk.Button(f_left, text="confirm", command=com_load_project_p,
              highlightcolor="#b8860b", activebackground="#ffd700").pack()

    f_left.grid(column=0, columnspan=1, row=1, rowspan=1, sticky="ns")

    ####################

    def com_submit_json_csv():
        def _succes():
            myc.project().menu_stack.insert(1, "main_n")
            dispatch()
        my_parser.parse_file_all(
            myc.project().GLOBAL["load_project_path"].get())
        handy_empty_grid()
        f = tk.Frame(myc.project().GLOBAL["tk_window"])
        if myc.project().DATA is not None:
            tk.Label(f, text="{} path DATA loaded".format(
                myc.project().GLOBAL["load_project_path"].get())).pack(side=tk.TOP)
            tk.Button(f, text="ok", command=_succes, highlightcolor="#b8860b",
                      activebackground="#ffd700").pack(side=tk.BOTTOM)
        else:
            tk.Label(f, text="fail to load file DATA at path {}".format(
                myc.project().GLOBAL["load_project_path"].get())).pack(side=tk.TOP)
            tk.Button(f, text="ok", command=dispatch, highlightcolor="#b8860b",
                      activebackground="#ffd700").pack(side=tk.BOTTOM)
        f.grid(column=1, row=1)

    f_center = tk.Frame(window)
    tk.Label(f_center, text="crée un projet par des données").pack(
        side="top", anchor="n")
    tk.Label(f_center, text="entré un chemin ou est le json ou csv").pack(
        side="top", anchor="n")
    tk.Entry(f_center, textvariable=myc.project(
    ).GLOBAL["load_project_path"]).pack()
    tk.Button(f_center, text="submit", command=com_submit_json_csv,
              highlightcolor="#b8860b", activebackground="#ffd700").pack(anchor="center")

    f_center.grid(column=1, columnspan=1, row=1, rowspan=1, sticky="ns")

    ####################
    def com_create():
        def _succes():
            myc.project().menu_stack.insert(1, "main_n")
            dispatch()
        my_parser.quick_cache_save(
            myc.project().GLOBAL["load_project_path"].get())
        handy_empty_grid()
        f = tk.Frame(myc.project().GLOBAL["tk_window"])
        tk.Label(f, text="new project saved at {}".format(
            myc.project().GLOBAL["load_project_path"].get())).pack(side=tk.TOP)
        tk.Label(f, text="loading default DATA").pack(side=tk.TOP)
        tk.Button(f, text="ok", command=_succes, highlightcolor="#b8860b",
                  activebackground="#ffd700").pack(side=tk.BOTTOM)
        f.grid(column=1, row=1)

    f_right = tk.Frame(window)

    tk.Label(f_right, text="crée un projet par défault").pack(
        side="top", anchor="n")
    tk.Label(f_right, text="entré un chemin").pack(side="top", anchor="n")
    tk.Entry(f_right, textvariable=myc.project(
    ).GLOBAL["load_project_path"]).pack()
    tk.Button(f_right, text="submit", command=com_create,
              highlightcolor="#b8860b", activebackground="#ffd700").pack(anchor="center")

    f_right.grid(column=2, columnspan=1, row=1, rowspan=1, sticky="ns")

    # tk.Label(window,text="ok").grid(column=0,row=2)
    # tk.Label(window,text="ok").grid(column=1,row=2)
    # tk.Label(window,text="ok").grid(column=2,row=2)


def dispatch():
    if not len(myc.project().menu_stack):
        exit(0)
    handy_empty_grid()
    p = myc.project().menu_stack[-1]
    if p == "init":
        menu_init()
    elif p == "main_n":
        main_n()
    elif p == "main_n_resolver":
        main_n_resolver()
    ###! elif p == "main_w":
    ###!     main_w()
    else:
        raise RuntimeError(f"unknown dispach {myc.project().menu_stack}")


def init():
    w = tk.Tk()
    window = tk.Frame(w)
    window.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
    myc.project().GLOBAL["tk_window"] = window
    myc.project().tkinter = True
    w.title("Graph")
    w.geometry("800x480")
    w.resizable(1, 1)
    window.grid_columnconfigure(0, weight=3)
    window.grid_columnconfigure(1, weight=3)
    window.grid_columnconfigure(2, weight=3)
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)
    myc.project().menu_stack.append("init")
    myc.project().GLOBAL["start_pos"] = None
    myc.project().GLOBAL["end_pos"] = None
    myc.project().GLOBAL["row_str"] = None
    myc.project().GLOBAL["col_str"] = None
    myc.project().GLOBAL["load_project_path"] = None
    myc.project().GLOBAL["grid_nboutton"] = None
    # myc.project().GLOBAL["resolver_mode"] = None
    # myc.project().GLOBAL["STEP"]
    dispatch()
    window.mainloop()


def main():
    init()


if __name__ == "__main__":
    print("launching raw tkinter")
    main()
