import matplotlib.pyplot as plt
import os
import sys


def vérife_nom_fichier() -> str:
    """ import le nom du fichier vérifier
    return : string
    """
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


def lirePoints(nomfichier: str) -> list:
    L = []
    with open(nomfichier, 'r') as file:
        n = int(file.readline().rstrip())
        for line in file.readlines():
            x, y = line.rstrip().split(',')
            L.append((int(x), int(y)))
        return L


def Taille(S: list) -> int:
    # n Retourne le nombre n de points dans S.
    ### arr_size = sizeof(name_of_array)/sizeof(name_of_array[index]);
    return len(S)


def Trier(S: list, y=False) -> tuple:
    # Trie l’ensemble S selon x puis y.
    if y:
        return sorted(S, key=lambda x: x[1])
    return sorted(S, key=lambda x: x[0])


def Decouper(S: list) -> tuple:
    # (SL,SR) Retourne les ensembles SL et SR.
    return (S[0:(Taille(S)//2)], S[(Taille(S)//2):])


def Domine(p1: tuple, p2: tuple) -> int:
    """
    # bool Retourne Vrai si et seulement si p1 domine p2.
    # 4 possibilité

    # renvoie un chifre pour debug
    # 0 x  1
    # x p1 x
    # 2 x  3
    """
    if (p1[0] >= p2[0]):
        # p2 p1
        # p2 p1
        if (p1[1] >= p2[1]):
            # x  p1
            # p2 x
            return 2
        # p2 p1
        # x  x
        return 0
    else:
        # p1 p2
        # p1 p2
        if (p1[1] >= p2[1]):
            # p1 x
            # x  p2
            return 3
        # x  p2
        # p1 x
        return 1
    # return True if (p1[0] >= p2[0]) and (p1[1] >= p2[1]) else False


def Ajouter(S: list, p: tuple) -> list:
    # Modifie l’ensemble S en lui ajoutant le point p.
    # on ajoute des points ????
    S.append(p)
    return S


def Supprimer(S: list, p: tuple) -> list:
    # Modifie l’ensemble S en y supprimant le point p.
    # mais pourquoi ?
    S.remove(p)
    return S


def EMPS(S: list, depth=0) -> list:

    def twopoints(s1: tuple, s2: tuple) -> tuple:
        """
        # si domine(s1,s2) = 0 || 3 c'est l'indifférence on retourne les 2
        # si domine(s1,s2) = 1 on retourne s1
        # si domine(s1,s2) = 2 on retourne s2
        """
        assert len(s1) == 1, s1
        assert len(s2) == 1, s2
        print(depth*" ", depth, "M merge", s1, s2)

        x = Domine(s1[0], s2[0])

        if x == 0 or x == 3:
            # s2 x  x
            # x  s1 x
            # x  x  s2
            print(depth*" ", depth, "M return",
                  Domine(s1[0], s2[0]),  "both", [*s1, *s2])
            return [*s2, *s1]
        elif x == 1:
            # x  x  s2
            # x  s1 x
            # x  x  x
            print(depth*" ", depth, "M return", Domine(s1[0], s2[0]), "s2", s2)
            return s2
        else:  # x == 2
            # x x  x
            # x  s1 x
            # s2 x  x
            print(depth*" ", depth, "M return", Domine(s1[0], s2[0]), "s1", s1)
            return s1

    depth += 1
    if Taille(S) > 3:
        # multiple points
        x = Trier(S,y=1)
        s1, s2 = Decouper(S)
        print(depth*" ", depth, "F EMPS", len(S), S)
        print(depth*" ", depth, "F EMPS L")
        emp1 = EMPS(s1, depth)
        print(depth*" ", depth, "F EMPS R")
        emp2 = EMPS(s2, depth)
        print(depth*" ", depth, "F EMPS L", emp1, "\t\t", s1)
        print(depth*" ", depth, "F EMPS R", emp2, "\t\t", s2)
        x = [*EMPS(emp1, depth), *EMPS(emp2, depth)]
        x = Trier(x)
        x = EMPS(x,depth)
        print(depth*" ", depth, "F return", x)
        print()
        return x

    elif Taille(S) == 3:
        # 3 points
        # we actually only want 2 points
        # print(S)
        S = Trier(S)
        print(depth*" ", depth, "M 3 merge", S)
        x = twopoints([S[0]],[S[1]])
        y = twopoints([S[1]],[S[2]])
        z = twopoints([S[1]],[S[2]])
        """
        [(15, 789), (18, 30), (20, 206)]
            4 M merge [(15, 789)] [(18, 30)]
            4 M return 3 both [(15, 789), (18, 30)]
            4 M merge [(18, 30)] [(20, 206)]
            4 M return 1 s2 [(20, 206)]
            4 F 3 points [(18, 30), (20, 206), (15, 789)]
        
        if one dominante over not carried
        """
        # remove duplicate
        # list(dict.fromkeys(z))

        print(depth*" ", depth, "M 3 return", z , S)
        return twopoints([S[0]],[S[2]])

    elif Taille(S) == 2:
        # else:
        # 2 points
        return twopoints(*Decouper(S))

    elif Taille(S) == 1:
        # 1 seul point safety
        return S
    raise


if __name__ == "__main__":
    # test pour domine
    assert Domine((1, 1), (0, 0)) == 2
    assert Domine((1, 1), (2, 0)) == 3
    assert Domine((1, 1), (0, 2)) == 0
    assert Domine((1, 1), (2, 2)) == 1
    assert Domine((2, 2), (1, 1)) == 2

    # allow to open with cmd arg
    if len(sys.argv) > 1:
        try:
            listePoints = lirePoints(sys.argv[1])
        except Exception as ex:
            print("an error occur while openning argument passed file")
            print(ex)
            listePoints = lirePoints(vérife_nom_fichier())
    else:
        listePoints = lirePoints(vérife_nom_fichier())

    assert isinstance(
        listePoints, list), f"something wrong W input mate '{listePoints}'"
    assert len(listePoints), f"something wrong W input mate '{listePoints}'"

    print("Nombre de points totale : ", Taille(listePoints))
    pareto = Trier(EMPS(Trier(listePoints)))
    print()
    print("retourn to main")
    print("Nombre de points de la courbe pareto : ", Taille(pareto))
    # print(pareto)
    print(f"Coordonnées des {len(pareto)} points : [")
    for x in pareto:
        print(f"\t[{x[0]} , {x[1]} ]")
    print("]")
    # trace le blob de points
    plt.scatter(*zip(*listePoints))
    # met les points bien en couleur et fait la ligne
    plt.scatter(*zip(*pareto), c='r', marker="x")
    for i, _ in enumerate(pareto[0:-1]):
        dx = pareto[i+1][0] - pareto[i][0]
        dy = pareto[i+1][1] - pareto[i][1]
        plt.arrow(pareto[i][0], pareto[i][1], dx,
                  dy, antialiased=True, color="r")
    plt.show()
