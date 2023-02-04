from math import *
from tkinter import *

class graph:

    def __init__(self,data : dict):
        self.data = data

    @classmethod
    def build_list(cls,data,vertex):
        data  = dict.fromkeys(data)
        for i in data.keys():
            data[i] = []
        for i in vertex:
            data[i[0]].append(i[1:]) 
        return cls(data)
    
    def show_data(self):

        circle_buffer = []

        def dessinenoeud(canv, x, y, r, noeud):
            canv.create_oval(x-r, y-r, x+r, y+r, outline="black", fill="white")
            canv.create_text(x, y, text=noeud.cle, fill="black")

        """ def tracearbre(canv, x, y, r, m, noeud, ouverture):
        #      trace l'arbre graphique récursivement
        #     pas = 50  # pas ajustable permettant de réduire la distance entre les noeuds
        #     # pour éviter que des noeuds se superposent
        #     if noeud.estFeuille() == False:  # si le noeud n'est pas une feuille
        #         # s'il a un fils gauche mais pas de fils droit
        #         if noeud.droite is None and noeud.gauche is not None:
        #             # récupération de la position du noeud fils
        #             x1, y1, ouverture = centresuivant(x, y, r, m, "l", ouverture)
        #             # tracé d'une droite entre x,y et x1,y1
        #             canv.create_line(x, y, x1, y1, fill="black")
        #             # cette fonction est dans la bibilothèque tkinter
        #             tracearbre(canv, x1, y1, r, m-pas, noeud.gauche,
        #                        ouverture)  # appel récursif pour traiter ce fils
        #         # s'il a un fils droit mais pas de fils gauche
        #         elif noeud.droite != None and noeud.gauche == None:
        #             # récupération de la position du noeud fils
        #             x1, y1, ouverture = centresuivant(x, y, r, m, "r", ouverture)
        #             # tracé d'une droite entre x,y et x1,y1
        #             canv.create_line(x, y, x1, y1, fill="black")
        #             tracearbre(canv, x1, y1, r, m-pas, noeud.droite,
        #                        ouverture)  # appel récursif pour traiter ce fils
        #         else:  # si il a un fils gauche et un fils droit
        #             # récupération de la position du noeud fils gauche
        #             x1, y1, ouverture = centresuivant(x, y, r, m, "l", ouverture)
        #             # tracé d'une droite entre x,y et x1,y1
        #             canv.create_line(x, y, x1, y1, fill="black")
        #             # appel récursif pour traiter ce fils gauche
        #             tracearbre(canv, x1, y1, r, m-pas, noeud.gauche, ouverture)
        #             # récupération de la position du noeud fils droit
        #             x1, y1, ouverture = centresuivant(x, y, r, m, "r", ouverture-3)
        #             # ouverture-3 pour compenser sur le noeud de droite
        #             # le +=3 dans centresuivant déjà appliqué
        #             # tracé d'une droite entre x,y et x1,y1
        #             canv.create_line(x, y, x1, y1, fill="black")
        #             # appel récursif pour traiter ce fils droit
        #             tracearbre(canv, x1, y1, r, m-pas, noeud.droite, ouverture)
        #     dessinenoeud(canv, x, y, r, noeud)  # tracé du noeud courant"""

        def tracearbre(canv, x, y, r, m, noeud, ouverture,first=False):
            """ trace l'arbre graphique récursivement"""
            pas = 50  # pas ajustable permettant de réduire la distance entre les noeuds
            # pour éviter que des noeuds se superposent
            max_per_node = 8
            
            circle_buffer.append(0,0)
            center = len(circle_buffer)-1
            for x in range(max_per_node):
                circle_buffer.append(centresuivant(center[0],center[1],))

            for i,point in enumerate(noeud):
                
                circle_buffer.append(point)

            if noeud.estFeuille() == False:  # si le noeud n'est pas une feuille
                # s'il a un fils gauche mais pas de fils droit
                if noeud.droite is None and noeud.gauche is not None:
                    # récupération de la position du noeud fils
                    x1, y1, ouverture = centresuivant(x, y, r, m, "l", ouverture)
                    # tracé d'une droite entre x,y et x1,y1
                    canv.create_line(x, y, x1, y1, fill="black")
                    # cette fonction est dans la bibilothèque tkinter
                    tracearbre(canv, x1, y1, r, m-pas, noeud.gauche,
                            ouverture)  # appel récursif pour traiter ce fils
                # s'il a un fils droit mais pas de fils gauche
                elif noeud.droite != None and noeud.gauche == None:
                    # récupération de la position du noeud fils
                    x1, y1, ouverture = centresuivant(x, y, r, m, "r", ouverture)
                    # tracé d'une droite entre x,y et x1,y1
                    canv.create_line(x, y, x1, y1, fill="black")
                    tracearbre(canv, x1, y1, r, m-pas, noeud.droite,
                            ouverture)  # appel récursif pour traiter ce fils
                else:  # si il a un fils gauche et un fils droit
                    # récupération de la position du noeud fils gauche
                    x1, y1, ouverture = centresuivant(x, y, r, m, "l", ouverture)
                    # tracé d'une droite entre x,y et x1,y1
                    canv.create_line(x, y, x1, y1, fill="black")
                    # appel récursif pour traiter ce fils gauche
                    tracearbre(canv, x1, y1, r, m-pas, noeud.gauche, ouverture)
                    # récupération de la position du noeud fils droit
                    x1, y1, ouverture = centresuivant(x, y, r, m, "r", ouverture-3)
                    # ouverture-3 pour compenser sur le noeud de droite
                    # le +=3 dans centresuivant déjà appliqué
                    # tracé d'une droite entre x,y et x1,y1
                    canv.create_line(x, y, x1, y1, fill="black")
                    # appel récursif pour traiter ce fils droit
                    tracearbre(canv, x1, y1, r, m-pas, noeud.droite, ouverture)
            dessinenoeud(canv, x, y, r, noeud)  # tracé du noeud courant



    """ fonction de tracé graphique d'un arbre """
    cwidth = 1000  # la largeur du canvas graphique
    cheight = 700  # la hauteur du canvas
    couleurs = ["red", "green", "bleu", "white",
                "black", "cyan", "magenta", "yellow"]
    # fen est l'objet fenêtre héritée de la bibliothèque tkinter
    fen = Tk()
    # création d'un bouton avec la commande fermer(quit) attachée à la fenêtre
    btn = Button(fen, text="Quitter", command=fen.destroy)
    # placement du bouton en bas de la fenêtre
    btn.pack(side="bottom")
    # création d'un panneau dans lequel on affichera l'arbre
    pan = LabelFrame(fen)
    # placement de ce panneau en faut de la fenêtre
    pan.pack(side="top")
    # creation du canva graphique dans ce panneau
    canv = Canvas(pan, width=cwidth, height=cheight)
    # placement de ce canva en haut du panneau graphique
    canv.pack(side="top")
    # appel de la fonction de tracé graphique de l'arbre créé ci haut
    tracearbre(canv, cwidth//2, 100, 12, 200, self.data, 8,first=True)
    # actualisation de l'affichage graphique
    fen.mainloop()
