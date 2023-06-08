import myc
import my_parser
import os
import sys
import resolver
try:
    import gen
except Exception as ex:
    print(ex)
    gen = None


def create_new_project():
    print("default folder for save .\\")
    print(os.path.abspath("."))
    confirmed = False
    path = ""
    # path must be valid and confirm
    while not confirmed:
        try:
            path = input("> where should the project be stored ? :")
            if not path:
                print("using default ./")
                path = "./"
            if not os.path.exists(path):
                print("le fichier n'éxiste pas")
                print("voici les possibilité : ")
                for x in os.listdir():
                    print("\t-'", x, "'")
            if os.path.isdir(path):
                os.chdir(path)
                print(os.path.abspath(path))
                path = os.path.abspath(path) + "/"
                confirmed = myc.handy_cmd_prompt("confirmed ? :")
        except Exception as ex:
            print(ex)
    myc.project().save_file_path = path
    my_parser.quick_cache_save()


def choice_project():
    # arg may or may not set the project obj
    # so look at save_file_path set
    # if set than good
    # else see if quit or create new
    if not myc.project().save_file_path:
        print("no args proj file data")

        if os.path.exists("./Save_Project.xml"):
            r = myc.handy_cmd_prompt(
                "local save project file found use this one")
            if r:
                # load local old save proj file
                my_parser.quick_cache_load()
        if not myc.project().save_file_path:
            while True:
                r = myc.handy_cmd_prompt("load path ?")
                if not r:
                    t = myc.handy_cmd_prompt("begin new ?")
                    if not t:
                        print("exiting")
                        exit(0)
                    else:
                        create_new_project()
                else:
                    my_parser.parse_Project_file(input("path >"))


def print_cmd():
    # this will do for now
    if myc.project().DATA_W:
        for k,v in myc.project().DATA.items():
            print(k,":",v)
    else:
        for row in myc.project().DATA:
            for element in row:
                print(element,end="")
            print()
    

def resolve_choice():
    print("resolve menu :")
    while True:
        inp_str = input("0 - BFS\n1 - DFS\n2 - Dijkstra\n10 - return\n")
        if inp_str == "10":
            return
        print("start point x,y / empty for edge")
        start = input(">")
        if start == "":
            start = None
        print("end point x,y / empty for edge")
        end = input(">")
        if end == "":
            end = None
        if inp_str == "0":
            print(resolver.BFS(start=start,end=end))
            return 
        elif inp_str == "1":
            print(resolver.DFS(start=start,end=end))
            return
        elif inp_str == "2":
            print(resolver.Dijkstra(start=start,end=end))
            return


def load_csv():
    my_parser.parse_cvs_DATA()


def load_json():
    my_parser.parse_json_DATA()


def save_csv():
    my_parser.save_cvs_DATA()


def save_json():
    my_parser.save_json_DATA()


def save_img():
    # basicaly the same as pretty print in cmd command
    raise


def cmd_gen():
    if gen is None:
        print("generation module is not imported")
        return
    myc.project().DATA_W = False
    myc.project().DATA = gen.generator()


def cmd_debug():
    print(myc.project())


def init():
    choice_project()
    inp_str = [(1, "see data", print_cmd), (2, "resolve", resolve_choice), (3, "load csv", load_csv), (4, "load json", load_json), (5, "save csv", save_csv),
               (6, "save json", save_json), (7, "save image", save_img), (8, "generate", cmd_gen), (9, "debug print project", cmd_debug), (10, "quit", lambda: exit(0))]
    while True:
        print()
        r = input(
            "".join([str(x[0])+" - "+x[1]+"\n" for x in inp_str])).lower()
        for x in inp_str:
            if r == str(x[0]) or r == x[1]:
                x[2]()


def main():
    print("starting command line")
    myc.project().tkinter = False
    myc.project().pygame = False
    init()


if __name__ == "__main__":
    main()
