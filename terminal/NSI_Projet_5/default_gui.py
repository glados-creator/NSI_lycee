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

if __name__ == "__main__":
    default_main()