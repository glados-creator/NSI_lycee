from math import *
from tkinter import *

class ArbreBinaire:
    def __init__(self, valeur, gauche=None, droite=None):
        self.cle = valeur
        self.gauche = gauche
        self.droite = droite

        self.racine = self

    def append(self, value):
        if value < self.cle:
            if self.droite == None:
                self.droite = ArbreBinaire(value)
            else:
                self.droite.append(value)
        else:
            if self.gauche == None:
                self.gauche = ArbreBinaire(value)
            else:
                self.gauche.append(value)

    def insert_gauche(self, valeur):
        if self.gauche == None:
            self.gauche = ArbreBinaire(valeur)
        else:
            new_node = ArbreBinaire(valeur)
            new_node.gauche = self.gauche
            self.gauche = new_node

    def insert_droit(self, valeur):
        if self.droite == None:
            self.droite = ArbreBinaire(valeur)
        else:
            new_node = ArbreBinaire(valeur)
            new_node.droit = self.droite
            self.droite = new_node

    """
    ### def get_valeur(self):
    ###     return self.cle

    ### def get_gauche(self):
    ###     return self.gauche

    ### def get_droit(self):
    ###     return self.droite
    """

    def __str__(self):
        return self.cle + " : " + (self.gauche.cle if self.gauche is not None else "None") + " " + (self.droite.cle if self.droite is not None else "None") + " "
    
    def estFeuille(self):
        if self.gauche is None and self.droite is None:
            return True
        else:
            return False

    """
    À faire vous-même 5
    """
    @staticmethod
    def hauteur(T):
        if T != None:
            x = T.racine
            return 1 + max(ArbreBinaire.hauteur(x.gauche), ArbreBinaire.hauteur(x.droite))
        return 0

    """
    À faire vous-même 6
    """
    @staticmethod
    def taille(T):
        if T != None:
            x = T.racine
            return 1 + ArbreBinaire.taille(x.gauche) + ArbreBinaire.taille(x.droite)
        return 0

    """
    À faire vous-même 7
    """
    @staticmethod
    def par_infixe(T):
        if T != None:
            x = T.racine
            ArbreBinaire.par_infixe(x.gauche)
            print(x.cle,end=" ")
            ArbreBinaire.par_infixe(x.droite)

    """
    À faire vous-même 8
    """
    @staticmethod
    def par_prefixe(T):
        if T != None:
            x = T.racine
            print(x.cle,end=" ")
            ArbreBinaire.par_prefixe(x.gauche)
            ArbreBinaire.par_prefixe(x.droite)

    """
    À faire vous-même 9
    """
    @staticmethod
    def par_suffixe(T):
        if T != None:
            x = T.racine
            ArbreBinaire.par_suffixe(x.gauche)
            ArbreBinaire.par_suffixe(x.droite)
            print(x.cle,end=" ")

    @staticmethod
    def search(T, k):
        if T is None:
            return False
        x = T.racine
        if k == x.cle:
            return True
        if k < x.cle:
            return ArbreBinaire.search(x.gauche, k)
        else:
            return ArbreBinaire.search(x.droit, k)

    @staticmethod
    def insert(T, y):
        x = T.racine
        while T != None:
            x = T.racine
            if y.cle == x.cle:
                # safe garde if value already exist
                return
            if y.cle < x.cle:
                T = x.gauche
            else:
                T = x.droit
        if y.cle < x.cle:
            x.insert_gauche(y)
        else:
            x.insert_droit(y)
    
    """
    À faire vous-même 10
    """
    @staticmethod
    def par_largeur(T):
        l = [None,T]
        while l[-1] != None:
            x = l.pop(1)
            print(x.cle,end=" ")
            if x.gauche != None:
                l.append(x.gauche.racine)
            if x.droite != None:
                l.append(x.droite.racine)


# =============================================================================
# Représentation graphique
# =============================================================================
# ------------------- cercle-------------------#


def cercle(canv, x, y, r, col, colf):
    """dessine un cercle graphique sur le canvas de centre (x,y) de rayon r de
    couleur col et de couleur de fond colf"""
    canv.create_oval(x-r, y-r, x+r, y+r, outline=col, fill=colf)
# ------------------- dessinenoeud-------------------#


def dessinenoeud(canv, x, y, r, noeud):
    """ dessine un noeud graphique : un cercle rempli avec la valeur du noeud"""
    cercle(canv, x, y, r, "black", "white")
    canv.create_text(x, y, text=noeud.cle, fill="black")
# ------------------- centresuivant-------------------#


def centresuivant(x, y, r, m, dir, ouverture):
    # ouverture permet d'ajuster l'angle d'ouverture des noeuds
    """ calcule la position de noeud suivant :
    on calcule a et b les décalages par rapport à la position actuelle x,y
    dir permet de spécifier:
    si c'est un fils gauche on retranche le a
    si c'est un fils droit on ajoute le a à x
    pour y on ajoute toujours b dans les deux cas.
    m la distance entre les cercles : le nœud et ses descendants.
    """
    a = (2*r+m)*sin(pi/(ouverture)
                    )  # calcule le décalage sur l'axe des x : coordonnées polaire vers
    # cordonnées cartésiennes
    # de même pour le décalage sur y. l'angle d'ouverture est 45 ° pour ouverture = 4
    b = (2*r+m)*cos(pi/(ouverture))
    if dir == "l":  # dir pour left ou right c.à.d. fils gauche ou fils droit
        x1, y1 = x-a, y+b  # on décale vers la gauche donc on retranche a de x et
    # on ajoute b à y on descend vers le bas
    else:
        x1, y1 = x+a, y+b  # on décale vers la droite donc on ajoute a à x
    ouverture += 3  # en augmentant ouverture, on diminue l'angle pour la ligne suivante
    return x1, y1, ouverture

# ------------------- tracearbre-------------------#


def tracearbre(canv, x, y, r, m, noeud, ouverture):
    """ trace l'arbre graphique récursivement"""
    pas = 50  # pas ajustable permettant de réduire la distance entre les noeuds
    # pour éviter que des noeuds se superposent
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

# ------------------- graphicarbre-------------------#


def graphicarbre(noeud):
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
    tracearbre(canv, cwidth//2, 100, 12, 200, noeud, 3)
    # actualisation de l'affichage graphique
    fen.mainloop()

if __name__ == "__main__":
    """
    À faire vous-même 3
    Vérifiez que "graphicarbre(racine)" renvoie bien :
    """
    arbre = ArbreBinaire("a",
                 ArbreBinaire("b",
                              ArbreBinaire("c",
                                           ArbreBinaire("e")
                                           ),
                              ArbreBinaire("d")
                              ),
                 ArbreBinaire("f",
                              ArbreBinaire("g",
                                           ArbreBinaire("i")
                                           ),
                              ArbreBinaire("h",
                                           ArbreBinaire("j")
                                           )
                              )
                 )
    graphicarbre(arbre)


    """
    À faire vous-même 4
    """
    b = ArbreBinaire("a",
        ArbreBinaire("b",
            ArbreBinaire("d"),
            ArbreBinaire("e")
        )
        ,ArbreBinaire("c")
    )
    graphicarbre(b)

    arbre3 = ArbreBinaire("15",
    ArbreBinaire("6",
        ArbreBinaire("3",
            ArbreBinaire("2"),
            ArbreBinaire("4")
            ),
        ArbreBinaire("7",
            droite=ArbreBinaire("13",ArbreBinaire("9"))
            )
    ),
    ArbreBinaire("18",
        ArbreBinaire("17"),
        ArbreBinaire("20")
        )
    )

    graphicarbre(arbre3)
    print("droite",arbre3.droite)
    print("estFeuille",arbre3.estFeuille())
    print("hauteur",ArbreBinaire.hauteur(arbre3))
    print("par_infixe",ArbreBinaire.par_infixe(arbre3))
    print("par_largeur",ArbreBinaire.par_largeur(arbre3))
    print("par_prefixe",ArbreBinaire.par_prefixe(arbre3))
    print("par_suffixe",ArbreBinaire.par_suffixe(arbre3))
    print("taille",ArbreBinaire.taille(arbre3))