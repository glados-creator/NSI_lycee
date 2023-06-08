from __future__ import print_function
import json
import os
import inspect
import types
import random

ASK_FOR_MODULE = False
HARD_ERROR = False
DEBUG = False
__all__ = ['ASK_FOR_MODULE', 'DEBUG', 'build_reverse_index', 'colorama',
           'default_main', 'dispatch', 'gstate', 'handy_backbtn', 'handy_clear', 'handy_config', 'handy_grid', 'handy_show_grid',
           'menu_debug', 'menu_demo', 'menu_list', 'menu_main', 'menu_main_make', 'menu_option', 'quick_ask', 'get_open_window', 'quick_dir', 'quick_eval', 'textU', 'tk', 'tk_colorchooser', 'tk_filedialog', 'tk_font', 'tk_messagebox', 'tk_scrolledtext', 'tk_simpledialog', 'tk_ttk', 'try_find_module', "pretty_error"]

# compatibility python 2.X raw_input -> python 3.X input()
# In Python 2.x, use raw_input for compatibility with Python 3.x input
# avoid python 2.X hack with simple input
if "raw_input" in dir(globals()):
    globals()["input"] = raw_input

try:
    # python 2.X
    import Tkinter as tk
    import Tkinter.messagebox as tk_messagebox
    import Tkinter.filedialog as tk_filedialog
    import Tkinter.colorchooser as tk_colorchooser
    import Tkinter.font as tk_font
    import Tkinter.scrolledtext as tk_scrolledtext
    import Tkinter.ttk as tk_ttk
    import Tkinter.simpledialog as tk_simpledialog
except Exception:
    try:
        # python 3.X
        import tkinter as tk
        import tkinter.messagebox as tk_messagebox
        import tkinter.filedialog as tk_filedialog
        import tkinter.colorchooser as tk_colorchooser
        import tkinter.font as tk_font
        import tkinter.scrolledtext as tk_scrolledtext
        import tkinter.ttk as tk_ttk
        import tkinter.simpledialog as tk_simpledialog
    except Exception as ec:
        print("[ERROR] : could not resolve tkinter default lib")
        print("'Tkinter' python 2.x")
        print("'tkinter' python 3.x")
        print("please fix at least one of them")
        raise ec


def try_find_module(module_name, nickname=None, exit_if_not_found=True, ask=True):
    """
    Tente de trouver et importer un module spécifié par son nom.

    Args:
    module_name (str): Le nom du module à trouver et importer.
    nickname (str, optionnel): Le surnom à utiliser pour le module importé.
    exit_if_not_found (bool, optionnel): Indique s'il faut quitter le programme si le module n'est pas trouvé.
    ask (bool, optionnel): Indique s'il faut demander une confirmation à l'utilisateur avant d'importer le module.

    Returns:
    int: 1 si le module est trouvé et importé avec succès, 0 sinon.

    Raises:
    None

    Exemple:
    ```
    try_find_module("math", "m", exit_if_not_found=True, ask=True)
    ```
    """
    # try to see if module is already imported
    if nickname is not None and nickname and isinstance(nickname, str) and nickname in globals():
        # maybe nickname is present
        if isinstance(globals()[nickname], types.ModuleType):
            return 1
    # maybe it's not a module
        print("[WARNGING] : '{}' in globals() but not '{}' module".format(
            nickname, module_name))
    if module_name in globals() and isinstance(globals()[module_name], types.ModuleType):
        # module imported but nickname not set (if nickname)
        if nickname is None:
            return 1
        globals()[nickname] = globals()[module_name]
        return 1
    try:
        # try to import module
        _module = __import__(module_name)
        while True:
            # ask for confirmation
            if ask:
                if nickname is not None and nickname and isinstance(nickname, str):
                    _ask = input(
                        "use '{}' as '{}' ? y/n : ".format(module_name, nickname))
                else:
                    _ask = input("use '{}' ? y/n : ".format(module_name))
            else:
                _ask = "y"
            if _ask.lower() == "y":
                if nickname is not None and nickname and isinstance(nickname, str):
                    globals()[nickname] = _module
                    return 1
                globals()[module_name] = _module
                return 1
            elif _ask.lower() == "n":
                if exit_if_not_found:
                    print("[ERROR] : could not found library '{}'".format(
                        module_name))
                    exit(1)
                return 0
    except Exception as ex:
        print("[WARNING] : '{}' disabled".format(module_name))
        print(ex)
        if exit_if_not_found:
            print("[ERROR] : could not found library '{}'".format(module_name))
            exit(1)
        return 0


try_find_module("customtkinter", "ctk", False, ASK_FOR_MODULE)
try_find_module("colorama", None, False, ASK_FOR_MODULE)

if "colorama" not in globals():
    # work on windows
    globals()["colorama"] = type("colorama", (object,), {
        "Fore": type("Fore", (object,), {
            'BLACK': '\x1b[30m', 'BLUE': '\x1b[34m', 'CYAN': '\x1b[36m', 'GREEN': '\x1b[32m', 'LIGHTBLACK_EX': '\x1b[90m', 'LIGHTBLUE_EX': '\x1b[94m', 'LIGHTCYAN_EX': '\x1b[96m', 'LIGHTGREEN_EX': '\x1b[92m', 'LIGHTMAGENTA_EX': '\x1b[95m', 'LIGHTRED_EX': '\x1b[91m', 'LIGHTWHITE_EX': '\x1b[97m', 'LIGHTYELLOW_EX': '\x1b[93m', 'MAGENTA': '\x1b[35m', 'RED': '\x1b[31m', 'RESET': '\x1b[39m', 'WHITE': '\x1b[37m', 'YELLOW': '\x1b[33m'
        })
    })
    # globals()["colorama"] = type("colorama", (object,), {
    #     "Fore": type("Fore", (object,), {
    #         'BLACK': '', 'BLUE': '', 'CYAN': '', 'GREEN': '', 'LIGHTBLACK_EX': '', 'LIGHTBLUE_EX': '', 'LIGHTCYAN_EX': '', 'LIGHTGREEN_EX': '', 'LIGHTMAGENTA_EX': '', 'LIGHTRED_EX': '', 'LIGHTWHITE_EX': '', 'LIGHTYELLOW_EX': '', 'MAGENTA': '', 'RED': '', 'RESET': '', 'WHITE': '', 'YELLOW': ''
    #     })
    # })
    pass
else:
    colorama.init()


def textU(txt: str):
    """
    Utilise le dossier "language" pour traduire le texte en utilisant des fichiers de traduction.
    chaque text est associer un numéros et ;
    Chaque fichier de traduction est une liste de numéro correspondant à chaque text traduit.

    Args:
    txt (str): Le texte à traduire.

    Returns:
    str: Le texte traduit s'il existe une traduction correspondante dans le fichier de traduction.
    Si aucune traduction n'est disponible, le texte d'origine est renvoyé.

    Raises:
    ValueError: Si le paramètre `txt` n'est pas une chaîne de caractères.

    Example:
    ```
    translated_text = textU("Hello")
    ```
    """
    if not isinstance(txt, str):
        raise ValueError("not correct type textU")
    # use to translate text
    # isn't implement for now
    return txt


def build_reverse_index(dic: dict):
    """
    Construit un index inversé à partir d'un dictionnaire.

    Args:
    dic (dict): Le dictionnaire à partir duquel construire l'index inversé.

    Returns:
    dict: L'index inversé construit.

    Raises:
    ValueError: Si le paramètre `dic` n'est pas un dictionnaire.

    Example:
    ```
    dictionary = {'apple': ['fruit'], 'carrot': ['vegetable'], 'banana': ['fruit', 'yellow']}
    reverse_index = build_reverse_index(dictionary)
    ```
    """
    if not isinstance(dic, dict):
        raise ValueError("not correct type")

    reverse_index = {}
    for key, value_list in dic.items():
        for value in value_list:
            # If the value is not already in the reverse index
            if value not in reverse_index:
                reverse_index[value] = [key]
            elif key not in reverse_index[value]:
                # check if the key is already in its list of values
                reverse_index[value].append(key)

    # Convert the lists in the reverse index to tuples
    for value, key_list in reverse_index.items():
        reverse_index[value] = tuple(key_list)

    return reverse_index


def quick_ask(txt: str):
    """
    Pose une question à l'utilisateur qui nécessite une réponse rapide (oui ou non).

    Args:
    txt (str): Le texte de la question.

    Returns:
    int: 1 si la réponse de l'utilisateur est "y" (oui), 0 si la réponse est "n" (non).

    Example:
    ```
    answer = quick_ask("Do you want to continue? (y/n): ")
    ```
    """
    while True:
        r = input(txt)
        if r.lower() == "y":
            return 1
        elif r.lower() == "n":
            return 0


def quick_eval(_global=None, _local=None):
    """
    Évalue et affiche le résultat d'une expression Python saisie par l'utilisateur.

    Args:
    _global (dict, optionnel): Le dictionnaire global à utiliser pour l'évaluation de l'expression.
    _local (dict, optionnel): Le dictionnaire local à utiliser pour l'évaluation de l'expression.

    Returns:
    None

    Example:
    ```
    quick_eval(globals(), locals())
    ```
    """
    if not DEBUG:
        return
    while True:
        try:
            print(eval(input(">>> "), _global if _global else globals(),
                  _local if _local else locals()))
        except ZeroDivisionError:
            break
        except Exception as ex:
            print("ERROR")
            print(ex)


def quick_dir(obj, _global=None, _local=None):
    """
    Affiche les attributs et les méthodes d'un objet donné, ainsi que leur valeur si l'objet est appelable.
    Permet ensuite à l'utilisateur d'évaluer des expressions Python à l'aide de la fonction `quick_eval`.

    Args:
    obj: L'objet dont les attributs et les méthodes doivent être affichés.
    _global (dict, optionnel): Le dictionnaire global à utiliser pour l'évaluation des expressions dans `quick_eval`.
    _local (dict, optionnel): Le dictionnaire local à utiliser pour l'évaluation des expressions dans `quick_eval`.

    Returns:
    None

    Example:
    ```
    quick_dir(obj, globals(), locals())
    ```
    """
    if not DEBUG:
        return
    print()
    print("---------------------- [quick_dir] ----------------------")
    print(type(obj), repr(obj))
    for attr in dir(obj):
        try:
            if callable(getattr(obj, attr)):
                try:
                    print(attr, getattr(obj, attr)())
                except Exception as ex:
                    print(attr, ex)
            else:
                print(attr, getattr(obj, attr))
        except Exception as ex:
            print(attr, ex)

    quick_eval(_global, _local)


def get_open_window():
    return tk.Button().winfo_toplevel()
###########################################################################


class Empty(object):
    def __init__(self): pass


class gstate(object):
    l_widget = ("Button", "Checkbutton", "Entry", "Frame", "Label", "LabelFrame", "Listbox", "Menu", "Canvas",
                "Menubutton", "Message", "PanedWindow", "Radiobutton", "Scale", "Scrollbar", "Spinbox", "Text")
    g_other = Empty()
    g_other.dict = {}

    def __init__(self, root, grid=None, stack=["menu_main"]):
        """
        Replace default tk widget, basically ttk/customtkinter.
        Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton, PanedWindow, Radiobutton, Scale, and Scrollbar.
        """

        self.root: any = root  # : tkinter.Tk()
        self.grid: any = grid  # : tkinter.Frame
        self._actual: str = ""
        self.stack: list = stack
        self.colortheme = {
            'borderwidth': 2,                  # Border width
            'background': 'gray',              # Background color
            'foreground': 'black',             # Foreground color
            'highlightbackground': 'grey',     # Highlight background color
            'highlightcolor': '#FFD700',       # Golden highlight color
            'activebackground': 'gray',        # Active background color
            'activeforeground': 'black',       # Active foreground color
            'disabledbackground': 'gray',      # Disabled background color
            'disabledforeground': 'gray50',    # Disabled foreground color
            'selectcolor': '#FFD700',           # Selection color
            'selectbackground': 'gray',        # Selection background color
            'selectforeground': 'black'        # Selection foreground color
            }


        def _reset_stack():
            self.stack = ["menu_main"]
            self.dispatch()

        self.root.bind("<Escape>", lambda e: exit(0))
        self.root.bind("<n>", lambda e: _reset_stack())

        def _inner():
            print("inner")
            quick_eval(globals())
        self.root.bind("<b>", lambda *args: _inner())

        self.other = Empty()

        def _valide(widget):
            valide_kwarg = widget(self.root).keys()
            def _inner(*args,**kwargs):
                ret = {}
                if not args:
                    ret["master"] = self.grid
                for k in valide_kwarg:
                    if k in kwargs:
                        ret[k] = kwargs[k]
                    elif k in self.colortheme:
                        ret[k] = self.colortheme[k]
                return widget(*args, **ret)
            return lambda *args,**kwargs : _inner(*args,**kwargs)
        
        for widget in gstate.l_widget:
            setattr(self, widget,  _valide(getattr(tk, widget)))

        if "ctk" in globals():
            trans = {
                "Button": "CTkButton", "Checkbutton": "CTkCheckBox", "Entry": "CTkEntry", "Frame": "CTkFrame", "Label": "CTkLabel", "Radiobutton": "CTkRadioButton", "Scrollbar": "CTkScrollbar"
            }
            def _filter(w,f):
                def _inner(*args,**kwargs):
                    for x in f:
                        kwargs.pop(x,None)
                    return w(*args,**kwargs)
                return lambda *args,**kwargs: _inner(*args,**kwargs)
            for k, v in trans.items():
                setattr(self, k, _filter(getattr(ctk, v),["relief"]))


###########################################################################

def handy_clear(state: gstate):
    """
    Efface le contenu de la grille dans l'objet `gstate` donné.

    Args:
    state (gstate / widget): L'objet `gstate` représentant l'état global.

    Raises:
    ValueError: Si l'objet `state` fourni n'est pas de type `gstate`.

    Example:
    ```
    state = gstate(root, grid=grid)
    handy_clear(state)
    ```
    """
    if not isinstance(state, gstate):
        for x in list(state.children):
            state.children[x].destroy()
        return
    state.grid.destroy()
    state.grid = state.Frame(state.root)
    state.grid.place(relheight=1, relwidth=1)


def handy_backbtn(state: gstate):
    """
    Crée un bouton "Retour" dans la grille de l'objet `gstate` donné.

    Args:
    state (gstate): L'objet `gstate` représentant l'état global.

    Returns:
    tkinter.Button: Le bouton "Retour".

    Raises:
    ValueError: Si l'objet `state` fourni n'est pas de type `gstate`.

    Example:
    ```
    state = gstate(root, grid=grid)
    back_button = handy_backbtn(state)
    ```
    """
    if not isinstance(state, gstate):
        raise ValueError("not correct type")

    def _com(state):
        state.stack.pop()
        state.dispatch()
    return state.Button(state.grid, text=textU("précédent"), command=lambda *args: _com(state)).grid(row=0, column=0)


def handy_config(state: gstate, row: int, column: int = None):
    """
    Configure la disposition de la grille dans l'objet `gstate` donné avec le nombre spécifié de lignes et de colonnes.

    Args:
    state (gstate): L'objet `gstate` représentant l'état global.
    row (int): Le nombre de lignes dans la grille.
    column (int, optionnel): Le nombre de colonnes dans la grille. S'il n'est pas spécifié, il est par défaut égal à la valeur de `row`.

    Raises:
    ValueError: Si les valeurs de ligne ou de colonne fournies ne sont pas des entiers.

    Example:
    ```
    state = gstate(root, grid=grid)
    handy_config(state, 3, 4)
    ```
    """
    if not isinstance(state, gstate):
        class obj:
            pass
        _state = obj()
        setattr(_state, "grid", state)
        state = _state
    if not isinstance(row, int):
        raise ValueError("not correct type")
    if column is None:
        column = row
    if not isinstance(column, int):
        raise ValueError("not correct type")
    for i in range(column):
        state.grid.columnconfigure(i, weight=row-1)
    for i in range(row):
        state.grid.rowconfigure(i, weight=column-1)


def handy_show_grid(master):
    """
    Affiche la disposition de la grille en créant des frame dans la grille avec marqué la ligne et colone.

    Args:
    master (tk.Widget): Le widget maître représentant la grille.

    Raises:
    ValueError: Si l'objet `master` fourni n'est pas de type `tk.Widget`.

    Example:
    ```
    grid = tk.Frame(root)
    handy_show_grid(grid)
    ```
    """
    if not DEBUG:
        return
    if not isinstance(master, tk.Widget):
        raise ValueError("not correct type")
    rows = master.grid_size()[1]
    cols = master.grid_size()[0]
    print("["+colorama.Fore.YELLOW+"INFO" +
          colorama.Fore.RESET+"] : grid size", rows, cols)
    for i in range(rows):
        for j in range(cols):
            frame = tk.Frame(master, bd=10, relief=tk.SOLID)
            frame.grid(row=i, column=j)
            tk.Label(frame, text="Row {}, Col {}".format(i, j)).pack()


def handy_grid(master=None, repeatewidget=None, repeatewidget_func: callable = None, rows: int = 3, cols: int = None, binding=None, *args, **kwargs):
    """
    Crée une grille de widgets en fonction des paramètres fournis.

    Args:
    repeatewidget (function, optionnel): Une fonction qui crée un seul widget.
    repeatewidget_func (function, optionnel): Une fonction qui crée un widget en fonction des indices de ligne et de colonne.
    master: Le widget maître représentant la grille.
    rows (int): Le nombre de lignes dans la grille.
    cols (int, optionnel): Le nombre de colonnes dans la grille. S'il n'est pas spécifié, il est par défaut égal à la valeur de `rows`.
    binding (function): Une fonction pour lier des actions aux widgets créés.
    *args: Liste d'arguments de longueur variable transmise à la fonction de création de widget.
    **kwargs: Arguments arbitraires passés à la fonction de création de widget.

    Raises:
    ValueError: Si ni repeatewidget ni repeatewidget_func ne sont fournis.
    NotImplementedError: Si la fonction de liaison n'est pas définie.

    Returns:
    list: Une liste à 2 dimensions représentant la grille des widgets créés.

    Example:
    ```
    def create_label(master, row, col):
        label = tk.Label(master, text=f"Ligne {row}, Colonne {col}")
        return label

    grid = handy_grid(repeatewidget_func=create_label, master=frame, rows=3, cols=4, binding=bind_func)
    ```
    """
    if repeatewidget is None and repeatewidget_func is None:
        raise ValueError(
            "Either repeatewidget or repeatewidget_func must be provided.")

    if cols is None:
        cols = rows

    if binding is None:
        def _error(*args):
            raise NotImplementedError("handy_grid wiget binding not set")
        binding = _error

    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            # Create a new widget using the repeatewidget function and the given arguments
            widget = repeatewidget_func(
                master, i, j, * args, **kwargs) if repeatewidget_func else repeatewidget(master, *args, **kwargs)

            # Call the binding function with the new widget as argument
            binding(widget, i, j)
            widget.grid(row=i, column=j)

            grid[-1].append(widget)
    return grid

###########################################################################


def menu_demo(state: gstate):
    """
    une simple démo pour démontrer l'apparence et les différente capabilité
    """
    # custome backbutton
    def _com(state):
        state.stack.pop()
        state.root.config(menu="")
        dispatch(state)
    state.Button(state.grid, text=textU("return"),
                 command=lambda *args: _com(state)).grid(row=0, column=0)

    f = state.Frame(state.grid)
    state.Button(f, text="Button").pack()
    state.Checkbutton(f, text="Checkbutton").pack()

    tmpframe = state.Frame(f, relief=tk.RIDGE)
    state.Label(tmpframe, text="Entry RIDGE", relief=tk.RIDGE).pack()
    state.Entry(tmpframe, relief=tk.RIDGE).pack()
    tmpframe.pack()

    x = state.LabelFrame(f, text="LabelFrame GROOVE", relief=tk.GROOVE)
    x.pack()
    state.Label(x, text="Label").pack()

    menubar = state.Menu(f)
    menu = state.Menu(menubar)
    menu.add_command(label="test")
    menu.add_command(label="exemple")
    menu.add_separator()
    menu.add_command(label="idk")
    menubar.add_cascade(label="Menu click me", menu=menu)
    # menu.add_command(label = "Menubutton")
    state.root.config(menu=menubar)

    x = state.PanedWindow(f, relief=tk.SUNKEN)
    x.pack()
    l = state.Label(x, text="PanedWindow 1 ->")
    x.add(l)
    l = state.Label(x, text="<- PanedWindow 2 SUNKEN")
    x.add(l)

    tmp = state.Frame(f, relief=tk.RAISED)
    var = tk.IntVar(state.grid, value=0)
    state.Radiobutton(tmp, text="Radiobutton1", variable=var,
                      value=0, relief=tk.RAISED).pack()
    state.Radiobutton(tmp, text="Radiobutton2 RAISED",
                      variable=var, value=1, relief=tk.RAISED).pack()
    tmp.pack()

    state.Scale(f, label="Scale").pack(side="left")

    tk.Canvas(f, bg="red", height=100).pack()

    scroll = state.Scrollbar(f)
    scroll.pack(side="right", fill="y")
    x = state.Listbox(f, yscrollcommand=scroll.set)
    for i in range(50):
        x.insert(1, "Listbox {}".format(i))
    x.pack(side="bottom")
    scroll.configure(command=x.yview)

    state.Message(f, text="Message1\nMessage2\nMessage3").pack(side="bottom")
    # state.PanedWindow(f).pack()
    state.Spinbox(f, from_=0, to=10).pack()

    f.grid(column=1, row=0, rowspan=3, columnspan=1)


def menu_debug(state: gstate):
    handy_backbtn(state)

    history = [0]
    # scroll = state.Scrollbar(state.grid)
    d = state.Frame(state.grid)
    f = state.Frame(d)
    l = state.Listbox(d, justify="left")  # ,yscrollcommand=scroll)
    e = tk.StringVar()
    state.Label(f, text=">>>").pack(side="left")
    entry = state.Entry(f, textvariable=e)
    entry.bind('<Return>', lambda *args: _com_handle(l, history, e, max_char))
    entry.pack(side="left", fill=tk.BOTH)
    max_char = state.Spinbox(state.grid, from_=10, to=1000)

    def _com_handle(l, history, i, max_char):
        history[0] += 1
        l.insert(history[0], "inp : " + i.get())
        try:
            r = str(eval(i.get()))
        except Exception as ex:
            r = str(ex)
        i.set("")
        rlis = r.split("\n")
        j = 0
        while j < len(rlis):
            if " " in rlis[j]:
                x = rlis[j].split(" ")
                rlis[j] = x[0]+" "
                for y in x[1:]:
                    rlis.insert(j+1, y)
                    j += 1
            j += 1
        rrlis = ["ret : "]
        while len(rlis):
            x = rlis.pop(0)
            if len(rrlis[-1]) + len(x) > int(max_char.get()):
                rrlis.append("")
            rrlis[-1] += x
        for x in rrlis:
            history[0] += 1
            l.insert(history[0], x)
    state.Button(f, text="send", command=lambda *args: _com_handle(l,
                 history, e, max_char)).pack(side="right")

    max_char.grid(row=0, column=1)
    # scroll.grid(column=2,row=1,rowspan=2)
    l.pack(side="top", fill=tk.BOTH)
    f.pack(side="bottom")
    d.grid(column=0, row=1, columnspan=3, rowspan=3)


def menu_option(state: gstate):
    """
    le menu de base pour les option renvoie a API.option
    """
    handy_config(state, 4, 4)

    def _com(state):
        state.stack.pop()
        dispatch(state)

    def _com_debug(state):
        state.stack.append(menu_debug)
        dispatch(state)

    # return / DEBUG

    f0 = state.Frame(state.grid)
    state.Button(f0, text=textU("précédent"),
                 command=lambda *args: _com(state)).pack(side="left")
    state.Button(f0, text="DEBUG",
                 command=lambda *args: _com_debug(state)).pack(side="right")
    f0.grid(row=0, column=0)

    def _com_load(state, strvar):
        state.colortheme = json.load(open(strvar.get(),"r"))
        state.dispatch()

    def _com_pick_load(strvar):
        strvar.set(tk_filedialog.askopenfilename(filetypes=(
            ("Json File", "*.json"), ("All Files", "*.*")), title="Choose a file."))

    # path Entry pick load

    f = state.Frame(state.grid)
    state.Label(f, text=textU("chemin charger")).pack(side="left")
    load_var = tk.StringVar()
    load_var.set("default.json")
    state.Entry(f, textvariable=load_var).pack()
    state.Button(f, text=textU("choisir un fichier"),
                 command=lambda *args: _com_pick_load(load_var)).pack()
    state.Button(f, text=textU("charger"), command=lambda *args: _com_load(state,
                 load_var)).pack(side="right")
    f.grid(row=0, column=1)

    def _com_save(state, strvar):
        json.dump(state.colortheme,open(strvar.get(),"w"))

    def _com_pick_save(strvar):
        strvar.set(tk_filedialog.asksaveasfilename(
            confirmoverwrite=True, defaultextension=".json"))

    # save path Entry pick save

    f = state.Frame(state.grid)
    state.Label(f, text=textU("chemin sauvegarder")).pack(side="left")
    save_var = tk.StringVar()
    save_var.set("default.json")
    state.Entry(f, textvariable=save_var).pack()
    state.Button(f, text=textU("choisir un fichier"),
                 command=lambda *args: _com_pick_save(save_var)).pack()
    state.Button(f, text=textU("sauvegarder"), command=lambda *args: _com_save(state,
                 save_var)).pack(side="right")
    f.grid(row=1, column=1)

    def _com_add_dispatch(state):
        state.stack.append(menu_demo)
        state.dispatch()

    state.Button(state.grid, text="demo",
                 command=lambda *args: _com_add_dispatch(state)).grid(row=2, column=1)

    def selector(state: gstate, master, name):
        def _update_color(value, name):
            state.colortheme[name] = value
            state._actual = ""
            dispatch(state)

        def _inner(state: gstate, name):
            f0 = state.Frame(master)
            state.Label(f0, text=name).pack(side="left")

            scale_var = tk.IntVar()
            scale_var.set(state.colortheme[name])

            scale = state.Scale(f0, from_=0, to=255, variable=scale_var, orient="horizontal")
            scale.pack(side="left")

            scale.bind("<Leave>", lambda event: _update_color(scale_var.get(), name))

            f0.pack()

        _inner(state, name)

    
    def colorchooser(state: gstate, master, name):
        def _inner(state: gstate, name):
            chooser = tk_colorchooser.Chooser()
            x = chooser.show()
            if x is None:
                return

            state.colortheme[name] = x[1]
            state._actual = ""
            dispatch(state)

        f0 = state.Frame(master)
        state.Label(f0, text=name).pack(side="left")
        state.Button(f0, text=textU("choisir"),
                     command=lambda *args: _inner(state, name)).pack()
        state.Canvas(f0, width=20, height=20, bg=state.colortheme[name]).pack(side="right")
        f0.pack()

    f = state.Frame(state.grid)
    f1 = state.Frame(f)
    selector(state,f1,"borderwidth")
    colorchooser(state,f1,"background")
    colorchooser(state,f1,"foreground")
    colorchooser(state,f1,"highlightbackground")
    colorchooser(state,f1,"highlightcolor")
    colorchooser(state,f1,"activebackground")
    f2 = state.Frame(f)
    colorchooser(state,f2,"activeforeground")
    colorchooser(state,f2,"disabledbackground")
    colorchooser(state,f2,"disabledforeground")
    colorchooser(state,f2,"selectcolor")
    colorchooser(state,f2,"selectbackground")
    colorchooser(state,f2,"selectforeground")
    
    f1.pack(side="left")
    f2.pack(side="right")
    f.grid(row=1, column=0)

    
def menu_main_make(*args):
    """
    Creates a custom `menu_main` function that generates a menu based on the provided arguments.

    Args:
    *args: Variable length argument list of callable objects.

    Raises:
    ValueError: If any argument in `args` is not callable.

    Returns:
    function: The generated `menu_main` function.
    """
    for x in args:
        if not callable(x):
            raise ValueError("not correct type {} {}".format(type(x), x))

    def menu_main(state: gstate):
        m = state.Frame(state.grid)

        def _com_add_state(state: gstate, t: str):
            state.stack.append(t)
            dispatch(state)
        for x in args:
            state.Button(m, text=textU(x.__name__.replace("menu_", "").replace("_", " ")),
                         command=lambda *args: _com_add_state(state, x)).pack()
        state.Button(m, text=textU("demo"),
                     command=lambda *args: _com_add_state(state, menu_demo)).pack()
        state.Button(m, text=textU("option"),
                     command=lambda *args: _com_add_state(state, menu_option)).pack()
        state.Button(m, text=textU("quitter"),
                     command=lambda *args: _com_add_state(state, lambda s: exit(0))).pack()
        m.grid(column=1, row=1)
    # replace global menu_main to this cutome menu_main for dispatch just in case
    globals()["menu_main"] = menu_main
    return menu_main


def menu_main(state: gstate):
    """
    Génère un menu principal à partir de l'objet `state` de type `gstate`.

    Args:
    state (gstate): L'objet `state` représentant l'état global.

    Raises:
    ValueError: Si l'objet `state` fourni n'est pas de type `gstate`.
    """
    if not isinstance(state, gstate):
        raise ValueError("not correct type")
    m = state.Frame(state.grid)

    def _com_add_state(state: gstate, t):
        state.stack.append(t)
        dispatch(state)

    state.Button(m, text=textU("jouer"),
                 command=lambda *args: _com_add_state(state, "game_play")).pack()
    state.Button(m, text=textU("demo"),
                 command=lambda *args: _com_add_state(state, menu_demo)).pack()
    state.Button(m, text=textU("option"),
                 command=lambda *args: _com_add_state(state, menu_option)).pack()
    state.Button(m, text=textU("quitter"),
                 command=lambda *args: _com_add_state(state, lambda s: exit(0))).pack()
    m.grid(column=1, row=1)


def default_main(*args):
    """
    Fonction main par défaut qui crée une fenêtre Tkinter et initialise l'état global.
    """
    root = tk.Tk()
    root.geometry("800x600")
    state = gstate(root=root, grid=tk.Frame(root))
    state.grid = state.Frame(state.root)
    state.grid.place(relheight=1, relwidth=1)
    if DEBUG:
        print(f"Hello from Tkinter version {tk.TkVersion}")
    menu_main_make(*args)
    dispatch(state)
    tk.mainloop()


def menu_list(state: gstate, *args):
    """
    Crée un menu à partir des arguments fournis et l'affiche dans l'état global.

    Args:
    state (gstate): L'état global représentant l'état de l'application.
    *args: Liste d'arguments variables contenant des fonctions.

    Raises:
    ValueError: Si l'un des arguments dans `args` n'est pas une fonction.

    Example:
    state = gstate(root, grid=grid)
    menu_list(state, function1, function2, function3)
    """
    for x in args:
        if not callable(x):
            raise ValueError("not correct type {} {}".format(type(x), x))
    handy_backbtn(state)
    m = state.Frame(state.grid)

    def _item(x):
        def _com_add_state():
            state.stack.append(x)
            dispatch(state)
        return lambda *args:_com_add_state()
    
    for x in args:
        state.Button(m, text=textU(x.__name__.replace("menu_", "").replace("_", " ")),
                     command=_item(x)).pack()
    m.grid(row=0,column=1,rowspan=3,columnspan=2)

###########################################################################


def pretty_error(ex, exclude=["dispatch"]):
    tb = ex.__traceback__
    opens = {}
    # pretty error formating
    print("\n["+colorama.Fore.RED+"ERROR"+colorama.Fore.RESET +
          "] Traceback (most recent call last) :")
    # try:
    #     ex.add_note("[ERROR] : (NOTE) error in '{}' while being called by dispatch".format(
    #         function.__name__))
    # except:
    print("["+colorama.Fore.RED+"ERROR"+colorama.Fore.RESET +
          "] : (NOTE) error in function while being called by dispatch")
    # pretty print error

    while tb is not None:
        if tb.tb_frame.f_code.co_name not in exclude:
            fcode = tb.tb_frame.f_code
            print('\tFile "{}", line {}, in {}'.format(
                fcode.co_filename, tb.tb_frame.f_lineno, fcode.co_name))
            # read line of file
            if fcode.co_filename not in opens:
                opens[fcode.co_filename] = open(fcode.co_filename, "r")
            file = opens[fcode.co_filename]
            file.seek(0)
            i = 0
            assert fcode.co_firstlineno <= tb.tb_frame.f_lineno, "bad math"
            # func def
            while i < fcode.co_firstlineno-1:
                file.readline()
                i += 1
            print("\t >", file.readline().replace("\n", " ; "))
            i += 1
            # error call
            if fcode.co_firstlineno != tb.tb_frame.f_lineno:
                # If def and error are at the same line, don't print anything
                # Calculate the number of lines between def and error
                lines_apart = tb.tb_frame.f_lineno - fcode.co_firstlineno
                while i < tb.tb_frame.f_lineno-2:
                    file.readline()
                    i += 1
                if lines_apart > 1:
                    # If only one line apart, print the error line
                    print("\t\t...")
                    print("\t   ", file.readline().replace("\n", " ; "))
                print("\t ->", file.readline().replace("\n", " ; "))
                print("\t   ", file.readline().replace("\n", " ; "))
            iargs, ivarargs, ivarkws, ilocals = inspect.getargvalues(
                tb.tb_frame)
            if iargs:
                print("args : ")
                for i, x in enumerate(iargs):
                    try:
                        print(" {} {} -> {}".format(i, x, ilocals[x]))
                    except:
                        print(" {} {} ->".format(i, x))
            if ivarargs and ilocals[ivarargs]:
                print("var_args : ")
                for i, x in enumerate(ilocals[ivarargs]):
                    try:
                        print(" {} {} -> {}".format(i,
                              x, ilocals[ivarargs][x]))
                    except:
                        print(" {} {} ->".format(i, x))
            if ivarkws and ilocals[ivarkws]:
                print("kw : ")
                for i, x in enumerate(ilocals[ivarkws]):
                    try:
                        print(" {} {} -> {}".format(i, x, ilocals[ivarkws][x]))
                    except:
                        print(" {} {} ->".format(i, x))
            # print()
            print("locals : ", repr(ilocals))
            # print()
            # print("globals : ",repr(tb.tb_frame.f_globals))
            # print()
        tb = tb.tb_next
    for v in opens.values():
        v.close()
    print("["+colorama.Fore.RED+"ERROR"+colorama.Fore.RESET+"]",
          type(ex), ex.__doc__, ex)

# def _error(*args) : raise ValueError("no")
# t = type("gstate",(object,),{"stack" : [_error]})


def dispatch(state: gstate, *args):
    """
    Handles the state and executes the appropriate function based on the current state stack.

    Args:
    state (gstate): The state object representing the current state.
    *args: Variable length argument list.

    Raises:
    ValueError: If the provided state is not of type `gstate`.

    Example:
    state = gstate(...)
    dispatch(state)
    """
    if not isinstance(state, gstate):
        raise ValueError("not correct type")
    if args and DEBUG:
        frame = inspect.currentframe().f_back.f_code
        print("["+colorama.Fore.YELLOW+"INFO"+colorama.Fore.RESET +
              "] : dispatch extra args : {}".format(args))
        for attr in dir(frame):
            print("["+colorama.Fore.YELLOW+"INFO"+colorama.Fore.RESET +
                  "] caller : '{}' -> '{}'".format(attr, getattr(frame, attr)))
        print()
    # clear the screen
    handy_clear(state)
    # reset the grid config to default 3 x 3
    handy_config(state, 3, 3)

    ################
    # DEBUG
    if DEBUG:
        handy_show_grid(state.grid)
    ################

    function = None
    if callable(state.stack[-1]):
        function = state.stack[-1]
    elif state.stack[-1] in globals():
        # searching in global as function
        function = globals()[state.stack[-1]]
    else:
        # goes on to deep search the function
        # go throught each global frame
        try:
            frame = inspect.currentframe()
            while frame is not None:
                # print("[INFO] frame search",frame)
                # print()
                # print(frame.f_globals)
                if state.stack[-1] in frame.f_globals:
                    frame.f_globals[state.stack[-1]](state)
                    break
                frame = frame.f_back
        except Exception as ex:
            print("["+colorama.Fore.RED+"ERROR"+colorama.Fore.RESET +
                  "] : critical error in dispacth frame search")
            print("["+colorama.Fore.YELLOW+"INFO"+colorama.Fore.RESET +
                  "] : search crash at dispatch stack : '{}'".format(state.stack))
            print(ex)
        else:
            print("["+colorama.Fore.RED+"ERROR"+colorama.Fore.RESET +
                  "] : unknown dispatch : '{}'".format(state.stack))
        # back to previous state
        state.stack.pop()
        # recursive
        dispatch(state)
        return

    # try exe the function
    if function is None:
        print("["+colorama.Fore.YELLOW+"INFO"+colorama.Fore.RESET +
              "] : crash at dispatch stack : '{}'".format(state.stack))
        raise ValueError("["+colorama.Fore.RED+"ERROR" +
                         colorama.Fore.RESET+"] : 'function' is empty Unreachable")
    try:
        function(state)
    except Exception as ex:
        if globals()["HARD_ERROR"]:
            raise ex
        pretty_error(ex)
        # raise ex
        # exit(1)
        state.stack.pop()
        dispatch(state)
    
# handy add dispatch to gstate as class attr
gstate.dispatch = dispatch
