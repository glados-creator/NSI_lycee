# Créé par florian.jean-louis1, le 15/12/2022 en Python 3.7
import random

def gen_list():
    ptx = []
    with open('paire.txt', 'w') as f:
        for i in range(int(input("Quelle taille de liste souhaitez vous ?"))):
            x = random.randint(0,100000)
            z = ptx.append(x)
        c = ptx.sort()
        # print(ptx)
        f.write("0\n")
        for x in ptx:
            y = random.randint(100000,200000)
            f.write(f"{x},{y}\n")

