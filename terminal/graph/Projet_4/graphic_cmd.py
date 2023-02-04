import myc
import my_parser
import os

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
                print("using default .\\")
                path = ".\\"
            if not os.path.exists(path):
                print("le fichier n'éxiste pas")
                print("voici les possibilité : ")
                for x in os.listdir():
                    print("\t-'", x, "'")
            if os.path.isdir(path):
                os.chdir(path)
                print(os.path.abspath(path))
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
            r = myc.handy_cmd_prompt("local save project file found use this one")
            if r:
                # load local old save proj file
                myc.project().save_file_path = ".\\"
                my_parser.quick_cache_load()
        if not myc.project().save_file_path:
            r = myc.handy_cmd_prompt("begin new ?")
            if not r:
                print("exiting")
                exit(0)
            else:
                create_new_project()

def init():
    choice_project()
    menu = [(9,"quit")]
    menu.sort(key=lambda x : x[0])
    inp_str = "".join([str(x[0]) + " - " + x[1] for x in menu])
    while True:
        r = input(inp_str).lower()
        if r == "" or len(r) > 1:
            pass
        elif r == "9":
            return 