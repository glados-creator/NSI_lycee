from copy import deepcopy


def file():
    # retourne une file vide return []
    return []


def vide(f):
    ''' renvoie True si la file est vide
    False sinon'''
    return f == []


def enfiler(f, x):
    # ajoute x à la file f"
    return f.append(x)


def defiler(f):
    # enlève et renvoie le premier élément de la file
    assert not vide(f), "file vide"
    return f.pop(0)


"""
À faire 1:
Tester les instructions suivantes:
"""
f = file()
for i in range(5):
    enfiler(f, 2*i)
print("f : ", f)
a = defiler(f)
print("a : ", a)
print("f : ", f)
print("vide(f) : ", vide(f))
print("")

"""
f :  [0, 2, 4, 6, 8]
a :  0
f :  [2, 4, 6, 8]
vide(f) :  False
"""

"""
Exercice 1:
Réaliser les fonctions taille(f) et sommet(f) qui retournent respectivement la taille de la file et le sommet de la file(le
premier à sortir) sans le supprimer.
"""


def taille(f):
    f1 = deepcopy(f)
    n = 0
    while not vide(f1):
        n += 1
        defiler(f1)
    return n


def sommet(f):
    f1 = deepcopy(f)
    return defiler(f1)


print("taille(f) : ", taille(f))
print("sommet(f) : ", sommet(f))
print("f : ", f)
print("")

"""
taille(f) :  4
sommet(f) :  2
f :  [2, 4, 6, 8]
"""


"""
II) IMPLEMENTATION - METHODE 2:
Nous allons créer une classe File pour implémenter cette structure.
À faire 2:
En vous inspirant de ce que l’on a vu pour la classe Pile(), réaliser cette implémentation
"""


class File:
    ''' classe File
    création d'une instance File avec une liste
    '''

    def __init__(self):
        "Initialisation d'une file vide"
        self.f = []

    def vide(self):
        "teste si la file est vide"
        return self.f == []

    def defiler(self):
        "défile"
        return self.f.pop(0)

    def enfiler(self, x):
        "enfile"
        self.f.append(x)

    # Exercice 2 :
    def taille(self):
        return len(self.f)

    # Exercice 2 :
    def sommet(self):
        return deepcopy(self.f).pop(0)


f = File()
for i in range(5):
    f.enfiler(2*i)
print("f : ", f)
print("f.f : ", f.f)
a = f.defiler()
print("a : ", a)
print("f : ", f)
print("f.f : ", f.f)
print("vide(f) : ", f.vide())
print("")

"""
f :  <__main__.File object at 0x00000000023B6148>
f.f :  [0, 2, 4, 6, 8]
a :  0
f :  <__main__.File object at 0x00000000023B6148>
f.f :  [2, 4, 6, 8]
vide(f) :  False
"""

"""
On souhaite écrire un algorithme qui simule le départ des voitures sur la route R3, modélisée par la file f 3.
_ Dans la file f 1 on représentera la présence d’une voiture par le nombre 1 et l’absence de voiture par 0.
_ Dans la file f 2 on représentera la présence d’une voiture par le nombre 2 et l’absence de voiture par 0.
_ On n’utilisera que les méthodes enfiler, defiler, sommet et vide.
_ On testera l’algorithme sur f 1 : tête <–[0, 1, 1, 0, 1]<– queue.
_ On testera l’algorithme sur f 2 : tête <–[0, 2, 2, 2, 0, 2, 0]<– queue.
_ Le résultat attendu : f 3 : tête <–[0, 1, 1, 2, 1, 2, 2, 0, 2, 0]<– queue.
"""
"""
Question 1 :
Que doit faire l’algorithme si les deux sommets des files sont à 0 ?
    - faire passer l'autre file 

Question 2 :
Que doit faire l’algorithme si le sommet de f 1 est à 1 et celui de f 2 à 2 ?
    - faire passer la 1 de f1 puis le 2 de f2

Question 3 :
Que doit faire l’algorithme si le sommet de f 1 est à 1 et celui de f 2 à 0 ?
    - faire passer f1

Question 4 :
Que doit faire l’algorithme si le sommet de f 1 est à 0 et celui de f 2 à 2 ?
    - faire passer f2

Question 5 :
Que doit faire l’algorithme si l’une des deux files est vide ?
    - finir l'autre file

"""
"""
Question 6 :
Compléter l’algorithme qui modélise ce carrefour. On utilisera une fonction croisement(f1,f2) qui prend en paramètres
deux files f 1 et f 2 et qui retourne une file f 3 contenant la file f 3 des voitures sur la route R3.
On utilise trois tableaux f1, f2 et f3 qui seront utilisées comme des files.
"""


# def Croisement_routier(f1,f2) :
#     n1, n2 = longueur de f1, longueur de f2
#     i1, i2 = 1, 1
#
#     tant que f1 et f2 ne sont pas vides :
#         si le sommet de f1 = 1
#             defiler f1 et
#             enfiler f3 avec cet élément
#             augmenter i1 de 1
#             si le sommet de f2 = 0
#                 defiler f2
#                 augmenter i2 de 1
#         sinon
#             si le sommet de f2 = 2
#                 defiler f2 et enfiler f3 avec cet élément
#                 augmenter i2 de 1
#                 defiler f1
#                 augmenter i1 de 1
#             sinon
#                 defiler f2 et enfiler f3 avec cet élément
#                 augmenter i2 de 1
#                 defiler f1
#                 augmenter i1 de 1
#
#     # on complète f3 avec le reste de la pile qui n’est pas vide
#     tant que i1 <= n1
#           defiler f1 et enfiler f3 avec cet élément
#           augmenter i1 de 1
#
#     tant que i2 <= n2
#         defiler f2 et enfiler f3 avec cet élément
#         augmenter i2 de 1
#
#     retourner f3

"""
Exercice 3 :
Réaliser le programme et tester le dans différents scénarios.
"""


def Croisement_routier(_f1, _f2):
    f1 = deepcopy(_f1)
    f2 = deepcopy(_f2)
    n1, n2 = len(f1), len(f2)
    i1, i2 = 1, 1
    f3 = []

    while not (vide(f1) or vide(f2)):
        if sommet(f1) == 1:
            enfiler(f3, defiler(f1))
            i1 += 1
            if sommet(f2) == 0:
                defiler(f2)
                i2 += 1
        else:
            if sommet(f2) == 2:
                enfiler(f3, defiler(f2))
                i2 += 1
                defiler(f1)
                i1 += 1
            else:
                enfiler(f3, defiler(f2))
                i2 += 1
                defiler(f1)
                i1 += 1

    # on complète f3 avec le reste de la pile qui n’est pas vide
    while i1 <= n1:
        enfiler(f3, defiler(f1))
        i1 += 1

    while i2 <= n2:
        enfiler(f3, defiler(f2))
        i2 += 1

    return f3


f1 = [0, 1, 1, 0, 1]
f2 = [0, 2, 2, 2, 0, 2, 0]
assert Croisement_routier(f1, f2) == [0, 1, 1, 2, 1, 2, 2, 0, 2, 0]
print("f1 : ", f1)
print("f2 : ", f2)
print("Croisement_routier(f1,f2) : ", Croisement_routier(f1, f2))
print("")

"""
f1 :  [0, 1, 1, 0, 1]
f2 :  [0, 2, 2, 2, 0, 2, 0]
Croisement_routier(f1,f2) :  [0, 1, 1, 2, 1, 2, 2, 0, 2, 0]

On testera l’algorithme sur f 1 : tête <–[0, 1, 1, 0, 1]<– queue.
_ On testera l’algorithme sur f 2 : tête <–[0, 2, 2, 2, 0, 2, 0]<– queue.
_ Le résultat attendu : f 3 : tête <–[0, 1, 1, 2, 1, 2, 2, 0, 2, 0]<– queue.
OK
"""

def pile():
    return []

def empiler(p, x):
    "Ajoute l'élément x à la pile p"
    p.append(x)


def depiler(p):
    "dépile et renvoie l'élément au sommet de la pile p"
    return p.pop()


def enfiler(f, x):
    # ajoute x à la file f"
    return f.append(x)


def defiler(f):
    # enlève et renvoie le premier élément de la file
    return f.pop(0)

f = [0,1,2,3,4,5,6,7,8,9]

"""
Exercice 4 :
On dispose d’une file, écrire une fonction qui renvoie la file inversée (l’élément de la tête sera situé à la queue et ainsi de suite). On utilisera seulement les méthodes associées aux piles et aux files.
"""
def inversefile(f1):
    f = deepcopy(f1)
    p = pile()
    while not vide(f):
        empiler(p,defiler(f))
    while not vide(p):
        enfiler(f,depiler(p))
    return f

print("f : ",f)
print("inversefile(f) : ",inversefile(f))
print("")

"""
f :  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
inversefile(f) :  [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
f[-1::]
"""

"""
Exercice 5 :
On dispose d’une file contenant des entiers, écrire une fonction qui renvoie une file où on aura séparé les nombres pairs des impairs.
"""
def pair(f1):
    f = deepcopy(f1)
    p = file()
    ip = file()
    while not vide(f):
        x = defiler(f)
        if x %2 == 0:
            enfiler(p,x)
        else:
            enfiler(ip,x)
    return (p,ip)

print("pair(f) : ",pair(f))
print("")

"""
pair(f) :  ([0, 2, 4, 6, 8], [1, 3, 5, 7, 9])
"""

"""
Exercice 6 :
On dispose d’une pile contenant des entiers, écrire une fonction ou une méthode qui renvoie une pile où l’on aura supprimé le premier élément entré.
"""

def supper(f):
    defiler(f)
    return f

print("f : ",f)
print("supper(f) : ",supper(f))
print("")

"""
f :  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
supper(f) :  [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

"""
Exercice 7 :
On dispose d’une file contenant des entiers, écrire une fonction ou une méthode qui renvoie une file où l’on aura supprimé le dernier élément entré.

"""

def supplast(f1):
    f = deepcopy(f1)
    p = pile()
    while not vide(f):
        empiler(p,defiler(f))
    # f[-1::]
    depiler(p)
    while not vide(p):
        enfiler(f,depiler(p))
    while not vide(f):
        empiler(p,defiler(f))
    while not vide(p):
        enfiler(f,depiler(p))
    return f

print("f : ",f)
print("supplast(f) : ",supplast(f))
print("")

"""
f :  [1, 2, 3, 4, 5, 6, 7, 8, 9]
supplast(f) :  [1, 2, 3, 4, 5, 6, 7, 8]
"""