import matplotlib.pyplot as plt
import os
import sys


def vérife_nom_fichier():
    while True:
        try:
            f = input("> nom du fichier : ")
            if not os.path.exists(f):
                print("le fichier n'éxiste pas")
                print("voici les possibilité : ")
                for x in os.listdir():
                    print("\t-'", x, "'")
            if os.path.isdir(f):
                os.chdir(f)
            else:
                with open(f, "r") as f1:
                    pass
                return f
        except Exception as ex:
            print(ex)


def lirePoints(nomfichier):
    """ import points with one point per line 
    return  of tuples points as (x,y) int cast not verifyed
    """
    L = []
    with open(nomfichier, 'r') as file:
        n = int(file.readline().rstrip())
        for line in file.readlines(-1):
            x, y = line.rstrip().split(',')
            L.append((int(x), int(y)))
        return L


def Taille(S):
    # n Retourne le nombre n de points dans S.
    return len(S)


def Trier(S, y=False):
    # Trie l’ensemble S selon x ou y.
    if y:
        return sorted(S, key=lambda x: x[1])
    return sorted(S, key=lambda x: x[0])


def Decouper(S):
    # (SL,SR) Retourne les ensembles SL et SR
    return (S[0:(Taille(S)//2)], S[(Taille(S)//2):])


def Domine(p1, p2):
    """
    # bool Retourne True si et seulement si p2 domine p1.
    # 4 possibilité
    # en réalité c'est trier donc p1.x <= p2.x
    # 0 x  1
    # x p1 x
    # 2 x  3
    donc 0 et 2 sont une erreur
    """
    # assert p1[0] < p2[0], f"Points Dominated Not Sorted {p1}, {p2}"
    return True if (p1[0] <= p2[0]) and (p1[1] <= p2[1]) else False


def Ajouter(S, p):
    # Modifie l’ensemble S en lui ajoutant le point p.
    # return S modifier pour enchainer comme dans js
    S.append(p)
    return S


def Supprimer(S, p):
    # Modifie l’ensemble S en y supprimant le point p.
    # return S modifier pour enchainer comme dans js
    S.remove(p)
    return S


def EMPS(S, depth=0):
    """ by divide and conquer get the dominant points of an pareto curve (max)
    S  of tuple (x,y) points sorted by x
    depth : int for pretty debug bc it's reccursive hell
    return  of points as tuple (x,y)
    """
    depth += 1
    s1, s2 = Decouper(S)
    if Taille(S) > 3:
        # multiple points
        # print(depth*" ", depth, "F EMPS", len(S), S)
        emp1 = EMPS(s1, depth)  # type: ignore
        emp2 = EMPS(s2, depth)  # type: ignore
        # print(depth*" ", depth, "F EMPS L", emp1, "\t\t", s1)
        # print(depth*" ", depth, "F EMPS R", emp2, "\t\t", s2)
        # don't ask why but it work with that magic
        x = Trier([*emp1, *emp2], y=True)[::-1]
        i = 0
        while i < len(x)-1:
            if x[i][0] > x[i+1][0]:
                x.pop(i+1)
            else:
                i += 1
        x = Trier(x)
        # print(depth*" ", depth, "F return", x)
        # print()
        return x

    elif Taille(S) == 3:
        # 3 points
        # we return magic sorting
        # print(depth*" ", depth, "M 3 merge", S)
        x = Domine(S[0], S[1])  # type: ignore
        y = Domine(S[1], S[2])  # type: ignore
        # print(depth*" ", depth, "M 3 merge", x,y)
        if x:
            if y:
                # x  x  s2
                # x  s1 x
                # s0 x  x
                return [S[2]]
            # x x  x
            # x  s1 x
            # s0  x  s2
            return [S[1], S[2]]
        if y:
            # s0 x  s2
            # x  s1 x
            return [S[0], S[2]]
        # s0 x  x
        # x  s1 x
        # x  x  s2
        return S

    elif Taille(S) == 2:
        """
        # en réalité c'est trier donc p1.x <= p2.x
        # 0 x  1
        # x p1 x
        # 2 x  3
        donc 0 et 2 sont une erreur

        # x x  True -> return p2
        # x p1 x
        # x x  False -> return both
        """
        # assert len(s1) == 1, s1
        # assert len(s2) == 1, s2
        if Domine(s1[0], s2[0]):
            return s2
        return [*s1, *s2]

    elif Taille(S) == 1:
        # 1 seul point safety
        return S


if __name__ == "__main__":
    # allow to open with cmd arg
    if len(sys.argv) > 1:
        print("try to open argv", sys.argv[1])
        try:
            if not os.path.isfile(sys.argv[1]):
                raise FileNotFoundError(f"file does not exist '{sys.argv[1]}'")
            listePoints = lirePoints(sys.argv[1])
        except Exception as ex:
            print("an error occur while openning argument passed file")
            print("error : ", ex)
            listePoints = lirePoints(vérife_nom_fichier())
    else:
        listePoints = lirePoints(vérife_nom_fichier())

    print("Nombre de points totale : ", Taille(listePoints))
    pareto = EMPS(Trier(listePoints))  # type: ignore
    pareto = list(pareto) # type: ignore # just so linter is happy
    # # assert len(pareto) > 0 ,"no pareto points"
    print()
    print("Nombre de points de la courbe pareto : ", Taille(pareto))
    # print(pareto)
    print(f"Coordonnées des {len(pareto)} points : [")
    for x in pareto:
        print(f"\t({x[0]} , {x[1]})")
    print("]")
    # trace le blob de points
    plt.scatter(*zip(*listePoints), marker="x")  # type: ignore
    # met les points bien en couleur et fait la ligne
    plt.scatter(*zip(*pareto), c='r', marker="X")  # type: ignore
    for i, _ in enumerate(pareto[0:-1]):
        dx = pareto[i+1][0] - pareto[i][0]
        dy = pareto[i+1][1] - pareto[i][1]
        plt.arrow(pareto[i][0], pareto[i][1], dx,
                  dy, antialiased=True, color="r")
    plt.show()
