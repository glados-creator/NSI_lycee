import matplotlib.pyplot as plt
import os
import sys


def vérife_nom_fichier() -> str:
    """ import valid filepath
    return : string
    """
    return "./data1.txt"


def lirePoints(nomfichier: str) -> list:
    """ import points with one point per line 
    return : list of tuples points as (x,y) int cast not verifyed
    """
    L = []
    with open(nomfichier, 'r') as file:
        # NOTE : n pas utiliser ?
        n = int(file.readline().rstrip())
        for line in file.readlines(-1):
            x, y = line.rstrip().split(',')
            # NOTE : no try ?
            L.append((int(x), int(y)))
        return L


def Taille(S: list) -> int:
    # n Retourne le nombre n de points dans S.
    ### arr_size = sizeof(name_of_array)/sizeof(name_of_array[index]);
    return len(S)


def Trier(S: list, y=False) -> tuple:
    # Trie l’ensemble S selon x ou y.
    if y:
        return sorted(S, key=lambda x: x[1])
    return sorted(S, key=lambda x: x[0])


def Decouper(S: list) -> tuple:
    # (SL,SR) Retourne les ensembles SL et SR
    return (S[0:(Taille(S)//2)], S[(Taille(S)//2):])


def Domine(p1: tuple, p2: tuple) -> bool:
    """
    # bool Retourne True si et seulement si p2 domine p1.
    # 4 possibilité
    # en réalité c'est trier donc p1.x <= p2.x
    # 0 x  1
    # x p1 x
    # 2 x  3
    donc 0 et 2 sont une erreur
    """
    assert p1[0] < p2[0], f"Points Dominated Not Sorted {p1}, {p2}"
    return True ... # if (p1[0] p2[0]) and (p1[1] p2[1]) else False


def Ajouter(S: list, p: tuple) -> list:
    # Modifie l’ensemble S en lui ajoutant le point p.
    # on ajoute des points ????
    # return S modifier pour enchainer comme dans js
    S.append(p)
    return S


def Supprimer(S: list, p: tuple) -> list:
    # Modifie l’ensemble S en y supprimant le point p.
    # return S modifier pour enchainer comme dans js
    # mais on utilise jamais la func donc pourquoi ?
    S.remove(p)
    return S


def twopoints(s1: tuple, s2: tuple) -> tuple:
    """
    # en réalité c'est trier donc p1.x <= p2.x
    # 0 x  1
    # x p1 x
    # 2 x  3
    donc 0 et 2 sont une erreur

    # si domine(s1,s2) = 0 || 3 c'est l'indifférence on retourne les 2
    # si domine(s1,s2) = 1 on retourne s1
    # si domine(s1,s2) = 2 on retourne s2

    # x x  True -> return p2
    # x p1 x
    # x x  False -> return both
    """
    # assert len(s1) == 1, s1
    # assert len(s2) == 1, s2
    # print(depth*" ", depth, "M merge", s1, s2)
    #
    # x = Domine(s1[0], s2[0])
    #
    # if x == 0 or x == 3:
    #     # s2 x  x
    #     # x  s1 x
    #     # x  x  s2
    #     print(depth*" ", depth, "M return",
    #           Domine(s1[0], s2[0]),  "")
    #     return 
    # elif x == 1:
    #     # x  x  s2
    #     # x  s1 x
    #     # x  x  x
    #     print(depth*" ", depth, "M return", Domine(s1[0], s2[0]), "")
    #     return 
    # else:  # x == 2
    #     # x x  x
    #     # x  s1 x
    #     # s2 x  x
    #     print(depth*" ", depth, "M return", Domine(s1[0], s2[0]), "")
    #     return 
    pass


def EMPS(S: list, depth=0) -> list:
    """ by divide and conquer get the dominant points of an pareto curve (max)
    S : list of tuple (x,y) points sorted by x
    depth : int for pretty debug bc it's reccursive hell
    return : list of points as tuple (x,y)
    """
    depth += 1
    s1, s2 = Decouper(S)
    if Taille(S) > 3:
        # multiple points
        # print(depth*" ", depth, "F EMPS", len(S), S)
        emp1 = EMPS(s1, depth)
        emp2 = EMPS(s2, depth)
        # print(depth*" ", depth, "F EMPS L", emp1, "\t\t", s1)
        # print(depth*" ", depth, "F EMPS R", emp2, "\t\t", s2)
        x = Trier(emp2,y=1)[::-1]
        x = Trier(x)
        # print(depth*" ", depth, "F return", x)
        # print()
        return x

    elif Taille(S) == 3:
        # 3 points
        # we return as much as the x increase
        # print(depth*" ", depth, "M 3 merge", S)
        x = 0 # ...
        y = 0 # ...
        # print(depth*" ", depth, "M 3 merge", x,y)
        if x:
            if y:
                # x  x  s2
                # x  s1 x
                # s0 x  x
                return 
            # x x  x
            # x  s1 x
            # s0  x  s2
            return 
        if y:
            # s0 x  s2
            # x  s1 x
            return 
        # s0 x  x
        # x  s1 x
        # x  x  s2
        return 

    elif Taille(S) == 2:
        """
        # en réalité c'est trier donc p1.x <= p2.x
        # 0 x  1
        # x p1 x
        # 2 x  3
        donc 0 et 2 sont une erreur

        # x x  True -> 
        # x p1 x
        # x x  False -> 
        """
        assert len(s1) == 1, s1
        assert len(s2) == 1, s2
        return 

    elif Taille(S) == 1:
        # 1 seul point safety
        return S


if __name__ == "__main__":
    # test pour domine
    # assert Domine((1, 1), (0, 0)) == error
    # assert Domine((1, 1), (0, 2)) == error
    assert Domine((1, 1), (2, 0)) == False
    assert Domine((1, 1), (2, 2)) == True
    # assert Domine((2, 2), (1, 1)) == error
    
    
    listePoints = lirePoints(vérife_nom_fichier())
    
    print("Nombre de points totale : ", Taille(listePoints))
    pareto = EMPS(Trier(listePoints))
    assert len(pareto) > 0 ,"no pareto points"
    print()
    print("Nombre de points de la courbe pareto : ", Taille(pareto))
    # print(pareto)
    print(f"Coordonnées des {len(pareto)} points : [")
    for x in pareto:
        print(f"\t({x[0]} , {x[1]})")
    print("]")
    # trace le blob de points
    plt.scatter(*zip(*listePoints))
    # met les points bien en couleur et fait la ligne
    plt.scatter(*zip(*pareto), c='r', marker="x")
    plt.show()
