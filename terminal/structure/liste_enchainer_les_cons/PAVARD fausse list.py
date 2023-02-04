from copy import copy


def vide():
    return None


def cons(x, L):
    return (x, L)


def ajouteEnTete(L, x):
    return cons(x, L)


def supprEnTete(L):
    return (L[0], L[1])


def estVide(L):
    return L is None


def compte(L):
    if estVide(L):
        return 0
    return 1 + compte(L[1])


nil = vide()
print("estVide(nil) : ", estVide(nil))
L = cons(5, cons(4, cons(3, cons(2, cons(1, cons(0, nil))))))
print("estVide(L) : ", estVide(L))
print("compte(L) : ", compte(L))
L = ajouteEnTete(L, 6)
print("compte(L) : ", compte(L))
x, L = supprEnTete(L)
print("x : ", x)
print("compte(L) : ", compte(L))
x, L = supprEnTete(L)
print("x : ", x)
print("compte(L) : ", compte(L))
print("")


class Cellule:
    def __init__(self, tete, queue):
        self.car = tete
        self.cdr = queue


class Liste:
    def __init__(self, c):
        self.cellule = c

    def estVide(self):
        return self.cellule is None

    def car(self):
        assert not (self.cellule is None), 'Liste vide'
        return self.cellule.car

    def cdr(self):
        assert not (self.cellule is None), 'Liste vide'
        return self.cellule.cdr
    
    # a faire 5
    def ajouteEnTete(self, x):
        self.cellule.cdr = copy(self.cellule.car)
        self.cellule.car = x


def cons(tete, queue):
    return Liste(Cellule(tete, queue))


nil = Liste(None)
L = cons(5, cons(4, cons(3, cons(2, cons(1, cons(0, nil))))))

print("L.estVide() : ", L.estVide())
print("L.car() : ", L.car())
print("L.cdr().car() : ", L.cdr().car())
print("L.cdr().cdr().car() : ", L.cdr().cdr().car())
print("")

"""
L.estVide() :  False
L.car() :  5                L[0]
L.cdr().car() :  4          L[1]
L.cdr().cdr().car() :  3    L[2]
"""


def longueurListe(L):
    n = 0
    while not (L.estVide()):
        n += 1
        L = L.cdr()
    return n


"""
return len(L)
"""


def listeElements(L):
    t = []
    while not (L.estVide()):
        t.append(L.car())
        L = L.cdr()
    return t


"""
return L = [5,4,3,2,1]
"""

L = cons(6, L)
"""
cela construit une nouvelle list avec comme première cellule car = 6 et cdr = (L)
donc L = [6,5,4,3,2,1]
"""

"""
a faire 6
"""

x = L.car()
# x est la "tête" de la liste ou le premier element = 6
L = cons(L.cdr().car(), L.cdr().cdr())
# L est la liste reste de list x = L[1::]


def supprEnTete(L):
    return (L.car(), cons(L.cdr().car(), L.cdr().cdr()))

"""
III) UNE STRUCTURE MUTABLE :
"""

L1 = L
L2 = L1.cdr()
L4 = L1.cdr().cdr()
L3 = cons(3, L4)

# print("listeElements(L1) : ",listeElements(L1))
# print("listeElements(L2) : ",listeElements(L2))
# print("listeElements(L3) : ",listeElements(L3))
# print("listeElements(L4) : ",listeElements(L4))

"""
À faire 8 :
"""

def insert(L,e,pos):
    if longueurListe(L) < pos:
        raise
    t = L
    for i in range(pos):
        t = t.cdr()
    t.cellule.cdr = cons(e,t.cdr())
    return L

NL = insert(L,9,longueurListe(L)-3)
# L[-2] = 9 + L[-2:-1]
print("listeElements(L) : ",listeElements(L))
# [5, 4, 3, 2, 9, 1, 0]

