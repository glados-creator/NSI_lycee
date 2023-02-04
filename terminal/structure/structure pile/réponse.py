from copy import deepcopy


def pile():
    # retourne une liste vide
    return []

# vide


def vide(p):
    '''renvoie True si la pile est vide
    et False sinon'''
    return p == []

# empiler


def empiler(p, x):
    "Ajoute l'élément x à la pile p"
    p.append(x)

# dépiler


def depiler(p):
    "dépile et renvoie l'élément au sommet de la pile p"
    assert not vide(p), "Pile vide"
    return p.pop()


"""
À faire 1 :
"""
p = pile()
for i in range(5):
    empiler(p, 2*i)
a = depiler(p)
print("a : ", a)
print("vide(p) : ", vide(p))
print("")

"""
a :  8
vide(p) :  False
"""

"""
Exercice 1 :
"""

# function d'aide pour inverser une pile


def Pinverse(p1):
    p = deepcopy(p1)
    o = []
    while not vide(p):
        o.append(p.pop())
    return o


def taille(p1):
    p = deepcopy(p1)
    n = -1
    while not vide(p):
        n += 1
        p.pop()
    return n


def sommet(p1):
    p = deepcopy(p1)
    return depiler(p)
    # return p[-1]


print("taille(p) : ", taille(p))
print("sommet(p) : ", sommet(p))
print("Pinverse(p) : ", Pinverse(p))
print("p : ", p)
print("")

"""
taille(p) :  3
sommet(p) :  6
Pinverse(p) :  [6, 4, 2, 0]
p :  [0, 2, 4, 6]
"""

"""
II) IMPLEMENTATION - METHODE 2 :
"""


class Pile:
    ''' classe Pile
    création d'une instance Pile avec une liste
    '''

    def __init__(self):
        "Initialisation d'une pile vide"
        self.L = []

    def vide(self):
        "teste si la pile est vide"
        return self.L == []

    def depiler(self):
        "dépile"
        assert not self.vide(), "Pile vide"
        return self.L.pop()

    def empiler(self, x):
        "empile"
        self.L.append(x)

    # Exercice 2
    def taille(self):
        # return len(self.L)
        p = deepcopy(self)
        n = -1
        while not p.vide():
            n += 1
            p.depiler()
        return n

    # Exercice 2
    def sommet(self):
        # return p[-1]
        p = deepcopy(self)
        return p.depiler()

    def __str__(self):
        ch = ''
        for x in self.L:
            ch = "|\t" + str(x) + "\t|" + "\n" + ch
        ch = "\nEtat de la pile:\n" + ch
        return ch


"""
À faire 2 :
"""

p = Pile()
for i in range(5):
    p.empiler(2*i)
print("p.L : ", p.L)
a = p.depiler()
print("a : ", a)
print("p.L : ", p.L)
print("p.vide() : ", p.vide())
print("")

"""
p.L :  [0, 2, 4, 6, 8]
a :  8
p.L :  [0, 2, 4, 6]
p.vide() :  False
"""

"""
III) UN PREMIER EXEMPLE - CONTROLE DU PARENTHESAGE D’UNE EXPRESSION :

L’algorithme :
On crée une pile.
On parcourt l’expression de gauche à droite.
À chaque fois que l’on rencontre une parenthèse ouvrante "( " on l’empile.
Si on rencontre une parenthèse fermante " ) " et que la pile n’est pas vide on dépile (sinon on retourne faux).
À la fin la pile doit être vide...
"""

"""
À faire 3 :
crée pile Pile,eXit (px)
pour chaque caratère de l'expression:
    if c'est le caratère ( :
        empiler un element a px
    sinon:
        si c'est le caratère ):
            si px est vide:
                # prématurément vide + de ) que de (
                retourné faux
            sinon:
                démpiler un element a px
    # pour tout autre caratère on s'en fiche
à la fin si il ne reste rien dans la pile
alors les parentèses sont balancer
sinon retourné faux
"""


def verification(expr):
    px = pile()
    for x in expr:
        if x == "(":
            px.append("(")
        elif x == ")":
            if vide(px):
                # prématurément vide + de ) que de (
                return False
            px.pop()
    if vide(px):
        # balance
        return True
    # reste (
    return False


print('verification("(..(..)..) ") : ', verification("(..(..)..) "))
print('verification("(...(..(..)...)") : ', verification("(...(..(..)...)"))
print("")

"""
verification("(..(..)..) ") :  True
verification("(...(..(..)...)") :  False
"""

"""
Exercice 4 :
"""

def verification(expr):
    px = pile()
    pp = pile()
    for x in expr:
        if x == "(":
            px.append("(")
        elif x == ")":
            if vide(px):
                # prématurément vide + de ) que de (
                return False
            px.pop()
        elif x == "[":
            pp.append("[")
        elif x == "]":
            if vide(pp):
                # prématurément vide + de ) que de (
                return False
            pp.pop()
    if vide(px) and vide(pp):
        # balance
        return True
    # reste ( ou [
    return False

# Prolongement possible
def verification2(expr):
    # autre version prend + en compte l'emboitage 
    # pour que [(]) ne marche pas
    case = {")":"(","]":"["}
    px = pile()
    for x in expr:
        if x == "(":
            px.append("(")
        elif x == "[":
            px.append("[")
        elif x == ")" or x == "]":
            if vide(px):
                return False
            if px.pop() != case[x]:
                raise RuntimeError("[(]) case , please balance inner parentheses")
    if vide(px):
        return True
    return False


print('verification("(..(..)..) [[]] ") : ',verification("(..(..)..) [[]] "))
print('verification2("(..(..)..) [[]] ") : ',verification2("(..(..)..) [[]] "))
print('verification("[..(..(..)..)..]") : ',verification("[..(..(..)..)..]"))
print('verification2("[..(..(..)..)..]") : ',verification2("[..(..(..)..)..]"))

print('verification("[..(..(..]..)..]") : ',verification("[..(..(..]..)..]"))
try:
    print('verification2("[..(..(..]..)..)") : ',verification2("[..(..(..]..)..)"))
except Exception as e:
    print("e : ",e)
    print("error bien attraper")

print('verification("(...(..(.[].)...)") : ',verification("(...(..(.[].)...)"))
print('verification2("(...(..(.[].)...)") : ',verification2("(...(..(.[].)...)"))
print("")

"""
verification("(..(..)..) [[]] ") :  True
verification2("(..(..)..) [[]] ") :  True
verification("[..(..(..)..)..]") :  True
verification2("[..(..(..)..)..]") :  True
verification("[..(..(..]..)..]") :  False
e :  [(]) case , please balance inner parentheses
error bien attraper
verification("(...(..(.[].)...)") :  False
verification2("(...(..(.[].)...)") :  False
"""

laby=[[0,1,0,0,0,0],
[0,1,1,1,1,0],
[0,1,0,1,0,0],
[0,1,0,1,1,0],
[0,1,1,0,1,0],
[0,0,0,0,1,0]]

lignes=len(laby[0]) # ...
colonnes=len([x[0] for x in laby])

print('lignes : ',lignes)
print('colonnes : ',colonnes)
print("")

"""
lignes :  6
colonnes :  6
"""

"""
À faire 4 :
"""

laby=[[0,1,0,0,0,0],
[0,1,1,1,1,0],
[0,1,0,1,0,0],
[0,1,0,1,1,0],
[0,1,1,0,1,0],
[0,0,0,0,1,0]]
T=deepcopy(laby)
T[3][2]='hello'
for ligne in laby:
 print("",ligne)
print("----------------")
for ligne in T:
 print("",ligne)
print("")

"""
[0, 1, 0, 0, 0, 0]
[0, 1, 1, 1, 1, 0]
[0, 1, 0, 1, 0, 0]
[0, 1, 0, 1, 1, 0]
[0, 1, 1, 0, 1, 0]
[0, 0, 0, 0, 1, 0]
----------------
[0, 1, 0, 0, 0, 0]
[0, 1, 1, 1, 1, 0]
[0, 1, 0, 1, 0, 0]
[0, 1, 'hello', 1, 1, 0]
[0, 1, 1, 0, 1, 0]
[0, 0, 0, 0, 1, 0]
"""

"""
À faire 5 :
"""

def voisins(T,v):
    # T tableau
    # v posititon (x,y)
    # V retourn voisin POS
    V=[]
    i,j=v[0],v[1]
    for a in (-1,1):
        if 0<=i+a<lignes:
            if T[i+a][j]==1:
                V.append((i+a,j))
            if 0<=j+a<colonnes:
                if T[i][j+a]==1:
                    V.append((i,j+a))
    return V

"""
Question 2 :
Que retourne cette fonction ?
pour une position x , y elle retourn les position des voisin positif

Question 3 :
Expliquer l’affichage provoqué par cette instruction : print('voisins(laby,(0,1) : ',voisins(laby,(0,1)).
a la position x = 0 y = 1 regarde en haut,bas,gauche,droite et retourne le voisin positif , le seul étant en (1,1)
"""

print('voisins(laby,(0,1) : ',voisins(laby,(0,1)))
"""
voisins(laby,(0,1) :  [(1, 1)]
"""

"""
Étape 2 : parcours du labyrinthe
L’idée est de parcourir le labyrinthe depuis l’entrée, en utilisant une pile pour stocker le chemin, pour pouvoir dépiler
lorsque le chemin n’aboutit pas et redémarrer sur une autre voie.
Un schéma sera sans doute plus efficace qu’un long discours...
"""

def labyrinte(l):
    p = pile()
    p.append([(0,1)])
    r = []
    # quand les chemin bifurque ajouté une pile a p
    while len(p) != 0:
        v : list = voisins(l,p[-1][-1])
        # on enleve la / les nodes que on a déja visité
        for x in v:
            if x in p[-1]:
                v.remove(x)
        # si la liste est vide alors c'est le bout du tunnel
        print(p)
        print(v)
        print()
        if len(v) == 0:
            # on peut vérifier quand meme que c'est pas la fin du labyrinte
            print(p[-1][-1])
            if p[-1][1] == 6:
                # dernière lignes donc soluce
                r.append(p[-1])
            # du coup on enleve ce stack
            p.pop()
        else:
            # il y a un / pls chemin donc on créée des piles de piles
            # on ajoute une pile a p e, copiant le chemin que on a déja
            i = len(p)-1
            f = deepcopy(p[-1])
            for x in v:
                f.append(x)
                p.append(f)
            # on enleve d'ou on vien
            p.pop(i)
    return r
            
print(labyrinte(deepcopy(laby)))
# casser mais doit rendre