from PIL import Image
from copy import deepcopy
import numpy as np


def flip_h(img: Image):
    cop = np.asarray(deepcopy(img))
    h, v = img.size
    size = (h-1, v-1)
    subimg = np.asarray(img)
    ### print("print image copy shape", cop.shape)
    for v in range(size[1]):
        for h in range(size[0]):
            cop[h][size[1]-v] = subimg[h][v]
    return Image.fromarray(cop)


def flip_v(img: Image):
    cop = np.asarray(deepcopy(img))
    h, v = img.size
    size = (h-1, v-1)
    subimg = np.asarray(img)
    ### print("print image copy shape", cop.shape)
    for v in range(size[1]):
        for h in range(size[0]):
            cop[size[0]-h][v] = subimg[h][v]
    return Image.fromarray(cop)


def corner_fusion(pixarr: np.array):
    TL = pixarr[:][:]
    TR = pixarr[:][:]
    BL = pixarr[:][:]
    BR = pixarr[:][:]
    if pixarr.shape == (2, 2):
        return [BR, BL, TR, TL]
    else:
        return corner_fusion() + corner_fusion() + corner_fusion() + corner_fusion() 


def main():
    im = Image.open("joconde.jpg")  # ouvre l’image indiquée
    largeur, hauteur = im.size  # donne la taille de l’image
    px = im.load()  # charge les coordonnées de chaque pixel px[x,y]
    im.show()  # fait afficher l’image im

    flipv = flip_v(im)
    fliph = flip_h(im)

    fliph.show()
    flipv.show()


main()
