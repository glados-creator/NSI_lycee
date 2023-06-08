import sys
import os

try:
    import my_parser
    import myc
    import resolver
    import graphic_cmd
except Exception as ex:
    print(ex)
    print("veuillez mettre le projet au complet")
    print("graphic_cmd default render is required")
    exit(1)

try:
    import gen
except Exception as ex:
    print(ex)
    print("gen of maze disabled")

# try:
# import pygame
# import graphic_pygame
# myc.project.pygame = True
# except Exception as ex:
# print(ex)
# print("interface graphic non importer(pygame)")

try:
    import tkinter as tk
    import graphic_tkinter
    myc.project().tkinter = True
except Exception as ex:
    print(ex)
    print("interface graphic non importer(tkinter)")


def main():
    print("launching")
    # use with args
    argfile = []
    if len(sys.argv) > 1:
        print("try to open argv", sys.argv[1])
        for x in sys.argv:
            argfile.append(my_parser.parse_file_all(x))
        print(argfile)

    # now we are sure that the project obj config is set properly
    # if myc.project().pygame:
    # r = myc.handy_cmd_prompt("use pygame ?")
    # if r:
    # return graphic_pygame.init()
    if myc.project().tkinter:
        r = myc.handy_cmd_prompt("use tkinter ?")
        if r:
            return graphic_tkinter.init()
        myc.project().tkinter = False

    # cmd mode
    return graphic_cmd.init()


if __name__ == "__main__":
    main()
