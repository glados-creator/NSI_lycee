# type: ignore
import tkinter as tk
import tkinter.filedialog as tkdiag
import tkinter.simpledialog as tksimp
import projet_3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import os
import time
import random
import csv


def parser(file: str) -> list:
    def inner(x):
        if x[0] == "[":
            return None
        return (float(x[0].replace("(", "").replace(",", "").replace("[", "")), float(x[1].replace(")", "").replace(",", "").replace("]", "")))
    return [inner(x) for x in csv.reader(open(file, "r"), delimiter=',') if inner(x)]


def com_validate():
    global PATH
    path = PATH.get()
    if path == "generer":
        return (True,)
    if not os.path.exists(path):
        return (False, "le chemin n'éxiste pas")
    if not os.path.isfile(path):
        return (False, "le chemin n'est pas un fichier")
    if not (path[-4:] == ".csv" or path[-4:] == ".txt"):
        return (False, "extension de fichier non reconnu")
    return (True,)


def com_file():
    global PATH
    PATH.set(tkdiag.askopenfilename(initialdir=os.getcwd()))
    com_change_entry()


def com_gen():
    global PATH
    PATH.set("generer")
    com_change_entry()


def com_new():
    global PATH
    PATH.set(os.getcwd())
    com_change_entry()


def com_image(canvas):
    filename = tkdiag.asksaveasfilename(
        defaultextension=".ps", initialdir=os.getcwd(), initialfile="out.ps")
    if not filename:
        return
    canvas.get_tk_widget().postscript(file=filename, colormode='color')


def com_save(data, pareto):
    f = tkdiag.asksaveasfilename(initialdir=os.getcwd(
    ), initialfile="result.txt", defaultextension=".txt")
    if not f:
        return
    global PATH
    with open(f, "w") as fi:
        fi.write(f"input file name : {PATH.get()}")
        fi.write(f"\nnomber of points {len(data)}")
        fi.write(f"\nnumber of pareto point {len(pareto)}")
        fi.write("\n[")
        for point in pareto:
            fi.write("\n\t"+str(point)+",")
        fi.write("\n]")


def menu_map():
    global PATH, ROOT
    start = time.time()
    # clear off the grid
    for widget in ROOT.grid_slaves():
        widget.grid_forget()

    ROOT.grid_columnconfigure(tuple(range(5)), minsize=50, weight=1)
    ROOT.grid_rowconfigure(tuple(range(5)), minsize=50, weight=1)

    # get data
    data = []
    path = PATH.get()
    if path == "generer":
        np = tksimp.askinteger("Nombre de points a générer", "nombre de points a générer : ",
                               initialvalue=1000, minvalue=1, maxvalue=500000)
        if not np:
            com_change_entry()
            return
        data = [(random.randint(0, 100000), random.randint(0, 100000))
                for i in range(np)]
    else:
        if path[-4:] == ".csv":
            data = parser(path)
        elif path[-4:] == ".txt":
            data = projet_3.lirePoints(path)
        else:
            raise RuntimeError("how did we got here ?")
    # pareto
    data_S = projet_3.Trier(data)
    pareto = projet_3.EMPS(data_S)
    frame = tk.Frame(ROOT)
    figure = plt.Figure(figsize=(6, 5), dpi=100)
    ax = figure.add_subplot(111)
    canvas = FigureCanvasTkAgg(figure, frame)
    # trace all points
    ax.scatter(*zip(*data_S), marker="x")
    # trace pareto points
    ax.scatter(*zip(*pareto), c='r', marker="X")  # type: ignore
    for i, _ in enumerate(pareto[0:-1]):
        dx = pareto[i+1][0] - pareto[i][0]
        dy = pareto[i+1][1] - pareto[i][1]
        ax.arrow(pareto[i][0], pareto[i][1], dx,
                 dy, antialiased=True, color="r")
    toolbar = NavigationToolbar2Tk(canvas, frame)
    toolbar.update()
    end = time.time()
    # show
    tk.Label(text=os.path.basename(PATH.get().replace("\\", "/"))
             ).grid(sticky="news", column=0, row=0)
    tk.Button(justify="center", text="nouveau",
              command=com_new).grid(sticky="news", column=1, row=0)
    tk.Button(justify="center", text="générer",
              command=com_gen).grid(sticky="news", column=2, row=0)

    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
    toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    frame.grid(sticky="news", column=0, columnspan=5, row=1, rowspan=5)

    tk.Label(text=f"Time : {round(end - start,1)} s pour {len(data)} points").grid(
        sticky="news", column=99, row=1)
    tk.Label(text=f"Nombre de points de pareto {len(pareto)}").grid(
        sticky="news", column=99, row=2)
    Listb = tk.Listbox()
    for i, point in enumerate(pareto, 1):
        Listb.insert(i, str(point))
    Listb.grid(sticky="news", column=99, row=3)

    tk.Button(justify="center", text="save image", command=lambda: com_image(canvas)).grid(
        sticky="news", column=0, row=99)
    tk.Button(justify="center", text="save result", command=lambda: com_save(data,
                                                                             pareto)).grid(sticky="news", column=1, row=99)


def menu_entry():
    global PATH
    tk.Label(text="nom du fichier").grid(sticky="news", column=0, row=0)
    tk.Button(justify="center", text="nouveau",
              command=com_new).grid(sticky="news", column=1, row=0)
    tk.Button(justify="center", text="générer",
              command=com_gen).grid(sticky="news", column=2, row=0)
    e = tk.Entry(textvariable=PATH)
    e.grid(sticky="news", column=1, row=1)
    e.bind('<Leave>', lambda arg: com_change_entry())
    e.bind('<Return>', lambda arg: com_change_entry())
    tk.Button(justify="center", text="fichier", command=com_file).grid(
        sticky="news", column=2, row=1)


def menu_valid():
    menu_entry()
    tk.Button(text="continuer", command=menu_map).grid(
        sticky="news", column=1, row=2)


def menu_invalid(error):
    menu_entry()
    tk.Button(text="continuer ("+error+")",
              state="disabled").grid(sticky="news", column=1, row=2)


def com_change_entry():
    global ROOT
    # clear screen
    for widget in ROOT.grid_slaves():
        widget.grid_forget()

    ROOT.grid_columnconfigure(tuple(range(3)), minsize=50, weight=1)
    ROOT.grid_rowconfigure(tuple(range(3)), minsize=20, weight=1)
    r = com_validate()
    if r[0]:
        menu_valid()
    else:
        menu_invalid(r[1])


ROOT = tk.Tk()
PATH = tk.StringVar(value=os.getcwd())


def main():
    global ROOT
    # show main menu
    ROOT.geometry("640x480")
    ROOT.title("Projet - 3 Pareto front GUI")
    ROOT.resizable(True, True)

    # Projet - 3 Pareto front GUI
    # ----------------------------------------------
    #       0           1                   2
    # 0 || File Name | New           || Generate     ||
    # 1 || Navigate  | Entry         || askforpath   ||
    # 2 || MAP       | MAP / Submite || Info         ||
    # 3 || MAP       | MAP           || Info         ||
    # 4 || Save img  | Save json     || (build info) ||
    com_change_entry()
    tk.mainloop()


if __name__ == "__main__":
    main()
