import importlib.util
import sys
import os
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

__all__ = []

def find():
    ret = []
    for file in os.listdir(os.getcwd()):
        if file[:4] == "GUI_" and file[-3:] == ".py" and file != "GUI_helper.py":
            module_name = os.path.splitext(os.path.basename(file))[0]
            try:
                spec = importlib.util.spec_from_file_location(module_name, file)
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)
            except Exception as ex:
                print(ex, file=sys.stderr)
            else:
                for func in getattr(module,"__all__"):
                    ret.append(getattr(module,func))
    return ret

def game_list(state : gstate):
    handy_backbtn(state)
    menu_list(state,*find())


if __name__ == "__main__":
    default_main(game_list)