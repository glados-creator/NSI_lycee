def recherche_dichotomique(liste, élément):
    # on initialise les indices début et fin aux extrémités de la liste
    début = 0
    fin = len(liste)

    while début <= fin:
        # On se place au milieu de la liste
        milieu = (début + fin) // 2  # il, s'agit d'une division entière

        if liste[milieu] == élément:
            print(élément, "trouvé à l'indice:", milieu, liste[milieu])
            return True
    # on arrête la boucle début = fin - 1
        elif liste[milieu] < élément:
            début = milieu + 1
        else:
            fin = milieu - 1
            print(élément, "non trouvé")
            return False


def tri_selection(t):
    n = len(t)
    for i in range(n-1):
        i_min = i
        for j in range(i+1, n):
            if t[j] < t[i_min]:
                i_min = j
        if i_min != i:
            # échanger t[i] et t[min]
            t[i], t[i_min] = t[i_min], t[i]
    return t


def tri_insertion(t: list):
    n = len(t)
    for i in range(1, n):
        x = t[i]
        j = i
        while j > 0 and t[j-1] > x:
            t[j] = t[j-1]
            j = j - 1
            t[j] = x
    return t


for i in range(5):
    print(i)
"""
0
1
2
3
4
"""
print("----------------")

for i in range(1, 5):
    print(i)
"""
1
2
3
4

"""
print("----------------")

for i in range(5, 1, -1):
    print(i)
"""
5
4
3
2
"""
print("----------------")

for i in range(5):
    for j in range(i):
        print(j)
"""
0
0
1
0
1
2
0
1
2
3
"""
print("----------------")

for i in range(5):
    while i > 0:
        print(i)
        i -= 1
"""
1
2
1
3
2
1
4
3
2
1
"""
print("----------------")

"""
O
OO
OOO
OOOO
OOOOO
OOOOOO
OOOOOOO
OOOOOOOO
OOOOOOOOO
"""
for x in range(10):
    print("O"*x)

print("----------------")

"""
0000000000
111111111
22222222
3333333
444444
55555
6666
777
88
9
"""
for i, x in enumerate(range(10, 0, -1)):
    print(f"{i}"*x)

print("----------------")


def is_sorted(T: list):
    """test if a list is sorted
    o(n)

    Args:
        T (list): _description_

    Return:
        True / False
    """
    for x1, _ in enumerate(T):
        if x1-1 < 0:
            x0 = 0
        if x1 == len(T)-1:
            x2 = x1
        if not (T[x0] < T[x1] < T[x2]):
            return False
    return True


assert (is_sorted([]), True)
assert (is_sorted([1, 1, 1, 1]), True)
assert (is_sorted([0, 1, 2, 3]), True)
assert (is_sorted([0]), True)
assert (is_sorted([0, 9, 1, 2, 4, 3]), False)


def tri_insertion(t): 
    n = len(t)
    for i in range(1, n):  # ICI
        x = t[i] 
        j = i
        while j > 0 and t[j-1] > x:
            t[j] = t[j-1]
            j = j - 1
            t[j] = x
    # LA
    return t
