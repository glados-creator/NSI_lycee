import tkinter as tk
import tkinter.filedialog as tkdiag
import tkinter.simpledialog as tksimp
import myc
import my_parser

def tryexcept_return(func,*arg,**kwarg):
    try:
        return (0,func(*arg,**kwarg))
    except Exception as ex:
        print(ex)
        return (1,myc.project().menu_stack[0]())

def handy_create_grid(elem, lab : list):
    pass

def menu_main():
    pass

def com_load_project():
    r = tryexcept_return(my_parser.quick_cache_load)
    if r[0]:return
    menu_main()

def com_start_scratch():
    my_parser.quick_cache_save()

def create_project():
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
                myc.create_new_project()

def init():
    window = tk.Tk()
    myc.project().GLOBAL["tk_window"] = window
    window.title("Graph")
    tk.Button(text="load project", command=com_load_project)
    window.mainloop()

if __name__ == "__main__":
    print("launching raw tkinter")
    init()