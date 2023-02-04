"""
VARIABLE
T : arbre x : noeud

DEBUT HAUTEUR(T) :
si T != NIL :
    x = T.racine
    renvoyer 1 + max(HAUTEUR(x.gauche), HAUTEUR(x.droit))
sinon :
    renvoyer 0

Quelle est la particularité de la fonction HAUTEUR() ?

l'algo renvoie la plus grande profondeur d'un arbre
l'algorithm est récursif

Appliquer l’algorithme ci-dessus sur l’arbre binaire du paragraphe ci-dessous afin de calculer sa hauteur en détaillant votre raisonnement

a : 1 + max(B : 1 + max 1 + max(0, 1 + max(0,0)), 1 + max(0,0),F : 1 + max( 1 + max(1 + max(0,0), 0), 1 + max(0, 1 + max(0,0)))) = 4

VARIABLE
T : arbre x : noeud

DEBUT TAILLE(T) :
si T != NIL :
    x = T.racine
    renvoyer 1 + TAILLE(x.gauche) + TAILLE(x.droit)
sinon :
    renvoyer 0 fin si

a) Quelle est la particularité de la fonction TAILLE() ?

l'algo renvoie le nombre de node dans l'arbre
l'algo est récursif

b) En vous inspirant du paragraphe précédent, appliquer l’algorithme
ci-dessus sur l’arbre binaire du paragraphe précédent afin de calculer sa taille en détaillant votre raisonnement.

a : 1 + (b : 1 + (c : 1 + (e : 1 ) + () ) + (d : 1 ) ) + (f : 1 + (g : 1 + (i : 1 ) ) + (h : 1 + (j : 1 )))


DEBUT
PARCOURS-INFIXE(T) :
si T != NIL :
    x = T.racine
    PARCOURS-INFIXE(x.gauche)
    print(x.clé)
    PARCOURS-INFIXE(x.droit)
fin si

a) Quelle est la particularité de la fonction PARCOURS-INFIXE() ?

récursif

b) Dans quel ordre est parcouru l’arbre binaire du paragraphe précédent par la fonction PARCOURS-INFIXE() ?

G R D
E C B D A I G F H J

DEBUT
PARCOURS-PREFIXE(T) :
si T != NIL :
    x = T.racine print(x.clé)
    PARCOURS-PREFIXE(x.gauche) PARCOURS-PREFIXE(x.droit)
fin si

a) Quelle est la particularité de la fonction PARCOURS-PREFIXE() ?

recursif

b) Dans quel ordre est parcouru l’arbre binaire du paragraphe précédent par la fonction PARCOURS-PREFIXE() ?

R G D
a (b (c e) d) (f (g i) (h j))

DEBUT
PARCOURS-SUFFIXE(T) :
si T != NIL :
    x = T.racine
    PARCOURS-SUFFIXE(x.gauche) PARCOURS-SUFFIXE(x.droit)
    print(x.clé)
fin si

a) Quelle est la particularité de la fonction PARCOURS-SUFFIXE() ?

recursif

b) Dans quel ordre est parcouru l’arbre binaire du paragraphe précédent par la fonction PARCOURS-SUFFIXE() ?

G D R
((c e) d b) ((g i) (h j) f) a

I) PARCOURS EN LARGEUR D’UN ARBRE BINAIRE :

a) Dans quel ordre est parcouru l’arbre binaire du paragraphe précédent par la fonction PARCOURS-LARGEUR() ?

a b f c d g h e i j

b) Selon vous, pourquoi parle-t-on de parcours en largeur ?

par ce que l'algo parcourt par tranche / sa largeur en une profondeur


II) ARBRE BINAIRE DE RECHERCHE :

a) 15 6 18 3 7 17 20 2 4 13 9

b) {Gaufrette, Augustin, Bubulle, Charlie, Flipper, Médor}

c) non car le node gauche !< droite l'ordre est casser

2°) Parcours infixe d’un arbre binaire de recherche :

a)oui

b) g r d on remarque que les clé sont dans l'ordre

3°) Recherche d’une clé dans un arbre binaire de recherche :

VARIABLE
T : arbre
x : noeud
k : entier

DEBUT
ARBRE-RECHERCHE(T,k) :
 si T == NIL :
 renvoyer False
 fin si
 x = T.racine
 si k == x.clé :
 renvoyer True
 fin si
 si k < x.clé :
 renvoyer ARBRE-RECHERCHE(x.gauche,k)
 sinon :
 renvoyer ARBRE-RECHERCHE(x.droit,k)
 fin si

a) Quelle est la particularité de la fonction ARBRE-RECHERCHE() ?

recursif

b) Appliquez l'algorithme de recherche d'une clé dans un arbre binaire de recherche sur l'arbre binaire de recherche de la question V) 1°) a). On prendra k = 13.

on prend un arbre et une valeur
la valeur est la racine de l'arbre -> trouvé
la valeur est plus grand -> recherche avec la node droite comme racine
(sinon) la valeur est plus petit -> recherche avec la node gauche comme racine

r=15
13 != 15
13 < 15
G
r=6
13 != 6
13 > 6
D
r=7
13 != 7 && 13 > 7
D
r=13
13 == 13 return

index 0011


c) Appliquez l'algorithme de recherche d'une clé dans un arbre binaire de recherche sur l'arbre binaire de recherche de la question V) 1°) a). On prendra k = 16

r=15
16 != 15 && 16 > 15
D
r=18
16 != 18 && 16 < 18
G
r=17
16 != 17 && node fieulle pas d'enfant
index non trouvé
index possible par ajout
index = 0100

4°) Insertion d’une clé dans un arbre binaire de recherche :

VARIABLE
T : arbre
x : noeud
y : noeud
DEBUT
ARBRE-INSERTION(T,y) :
 x = T.racine
 tant que T != NIL :
 x = T.racine
 si y.clé < x.clé :
 T = x.gauche
 sinon :
 T = x.droit
 fin si
 fin tant que
 si y.clé < x.clé :
 insérer y à gauche de x
 sinon :
 insérer y à droite de x
 fin si
FIN

a) Appliquez l'algorithme d'insertion d'un nœud « y » dans un arbre binaire de recherche sur l'arbre de la question V)
1°) a). On prendra y.clé = 16.

voire question precédente
index = 0100

VI) IMPLEMENTATIONS PYTHON :
1°) Implémentation d’un arbre binaire en POO :
"""


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

    def estFeuille(self):
        if self.gauche is None and self.droite is None:
            return True
        else:
            return False

    @staticmethod
    def hauteur(T):
        if T != None:
            x = T.racine
            return 1 + max(ArbreBinaire.hauteur(x.gauche), ArbreBinaire.hauteur(x.droit))
        else:
            return 0

    @staticmethod
    def taille(T):
        if T != None:
            x = T.racine
            return 1 + ArbreBinaire.taille(x.gauche) + ArbreBinaire.taille(x.droit)
        else:
            return 0

    @staticmethod
    def par_infixe(T):
        if T != None:
            x = T.racine
            ArbreBinaire.par_infixe(x.gauche)
            print(x.cle)
            ArbreBinaire.par_infixe(x.droit)

    @staticmethod
    def par_prefixe(T):
        if T != None:
            x = T.racine
            print(x.cle)
            ArbreBinaire.par_prefixe(x.gauche)
            ArbreBinaire.par_prefixe(x.droit)

    @staticmethod
    def par_suffixe(T):
        if T != None:
            x = T.racine
            ArbreBinaire.par_suffixe(x.gauche)
            ArbreBinaire.par_suffixe(x.droit)
            print(x.cle)

    @staticmethod
    def search(T, k):
        if T == None:
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
a) Complétez le programme précédent afin qu’il puisse construire l’arbre suivant à l’aide de la classe « ArbreBinaire
». On instanciera pour cela l’objet « racine » appartenant à la classe « ArbreBinaire »
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

"""
2°) Affichage d’un arbre binaire dans la console Python :
"""

from math import *
from tkinter import *

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

graphicarbre(arbre)