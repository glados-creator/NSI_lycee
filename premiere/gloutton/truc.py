import cProfile
"""
def main1():
    # Exemple d'algorithme force brute
    # affichage de tous les minimums de la liste par comparaison avec les voisins
    # de gauche et de droite avec parcours de la liste
    y = [8.4, 9.5, 8.2, 5.1, 1.2, -2.6, -5.3, -6.3, -5.8, -3.9, -1.4, 0.9, 2.6, 3.3,
    3.0, 2.0, 0.8, -0.1, -0.5, -0.4, 0.0, 0.4, 0.5, 0.1, -0.8, -2.0, -3.0, -3.3,
    -2.6, -0.9, 1.4, 3.9, 5.8, 6.3, 5.3, 2.6, -1.2, -5.1, -8.2, -9.5, -8.4]
    i = 1
    for i in range (len(y)-1):
        if y[i - 1] > y[i] and y[i] < y[i + 1] :
            print(y[i])

        i += 1


def main2():
    # Exemple d'algorithme glouton
    # recherche d'un minimum dans une liste par comparaison avec les voisins
    # de gauche et de droite
    import random
    y = [8.4, 9.5, 8.2, 5.1, 1.2, -2.6, -5.3, -6.3, -5.8, -3.9, -1.4, 0.9, 2.6, 3.3,
    3.0, 2.0, 0.8, -0.1, -0.5, -0.4, 0.0, 0.4, 0.5, 0.1, -0.8, -2.0, -3.0, -3.3,
    -2.6, -0.9, 1.4, 3.9, 5.8, 6.3, 5.3, 2.6, -1.2, -5.1, -8.2, -9.5, -8.4]
    # on tire un point au hasard qui ne soit pas le premier ni le dernier
    index_hasard = random.randint(1, len(y)-1)
    i = 1
    while y[index_hasard - 1] < y[index_hasard] or y[index_hasard] > y[index_hasard + 1]:
        if y[index_hasard - 1] < y[index_hasard]:
            index_hasard = index_hasard - 1
        else:
            index_hasard = index_hasard + 1
    minimum = y[index_hasard]
    print(minimum)
"""

"""
def main1():
    # rendu de monaie ex1

    renduType = [1, 2, 5, 10, 20, 50]
    renduTypeC = renduType.copy()
    Rendu = []
    montant = 10
    donner = 55

    arendre = donner - montant 

    while len(renduTypeC) > 1:
        # print("renduTypeC",renduTypeC,"\t\tlen(renduTypeC)",len(renduTypeC),"\t\tarendre",arendre)
        if arendre < renduTypeC[-1]:
            renduTypeC.pop()
        else:
            Rendu.append(renduTypeC[-1])
            arendre -= renduTypeC[-1]


    print(Rendu)
"""

"""
def main1():
    # ex2 voleur
    trucs = {'o1' : (300,50), 'o2' : (1,30), 'o3' : (100,10), 'o4' : (5 ,5), 'o5' : (50,60)} # (prix , poid)
    for x in trucs.keys():
        print(x,trucs[x][0] /trucs[x][1] , trucs[x][0] ,trucs[x][1])
        trucs[x] = trucs[x][0] /trucs[x][1]
    print(sorted(list(trucs.items()),key=lambda x: x[1])[-1])
"""


def main1():
    # ex3 livreur

    trucs = {'o1' : (4,0.5), 'o2' : (10,1), 'o3' : (25,2), 'o4' : (45 ,5), 'o5' : (120,10)} # (prix , volume)
    for x in trucs.keys():
        print(x,trucs[x][0] /trucs[x][1] , trucs[x][0] ,trucs[x][1])
        # prix par volume
        trucs[x] = trucs[x][0] /trucs[x][1]
    print(sorted(list(trucs.items()),key=lambda x: x[1])[-1])




def main():
    p1 = cProfile.Profile()
    p1.enable()
    main1()
    p1.disable()
    p1.print_stats()

"""    
    p2 = cProfile.Profile()
    p2.enable()
    main2()
    p2.disable()
    p2.print_stats()
"""


if __name__ == "__main__":
    main()