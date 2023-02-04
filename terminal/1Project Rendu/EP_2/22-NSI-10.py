def fusion(L1, L2):
    """ function qui fusionne les 2 list du trie fusion
    complexite O(n)
    L1 : list[int | float | any]
    L2 : list[int | float | any]
    return : list[int | float | any]
    """
    n1 = len(L1)  # longueur de list 1
    n2 = len(L2)  # longueur de list 2
    L12 = [0]*(n1+n2)  # list de retour initialise avec des 0
    i1 = 0  # indice 1
    i2 = 0  # indice 2
    i = 0  # indice retour / total
    # itere sur tout les element tant que une des 2 list n'est pas vide
    # goto Boucle 1
    while i1 < n1 and i2 < n2:
        # on regarde les valeurs au 2 indices des list
        # si la valeur de la list 1 est plus petit que
        # la valeur de la liste 2
        # alors on ajoute la valeur la plus petit
        # aka la valeur a indice list 1
        if L1[i1] < L2[i2]:
            L12[i] = L1[i1]
            # et on augmente l indice list 1
            i1 = i1 + 1
        else:
            # sinon on met la valeur de list 2
            L12[i] = L2[i2]
            # et on augmente l indice list 2
            i2 = i2 + 1
        # augmente indice total car on a ajouter un élément
        i += 1
    # optimisation l une des 2 list est forcement vide donc on pourrai faire
    # un if ur l une des 2 boucle
    # IF i2 >= n2:

    # si la boucle tourne c'est que dans la Boucle 1
    # la list 2 a ete vide en première
    # et donc on copie le reste de la list 1 dans le resultat
    while i1 < n1:
        L12[i] = L1[i1]
        i1 = i1 + 1
        i = i + 1
    # => L12.extend(L1[i1:])

    # ELSE:

    # si la boucle tourne c'est que dans la Boucle 1
    # la list 1 a ete vide en première
    while i2 < n2:
        L12[i] = L2[i2]
        i2 = i2 + 1
        i = i + 1
    # => L12.extend(L2[i2:])

    # retourne le résultat qui est dans L12
    return L12


def trie_fusion(L: list):
    """ pour le fun par ce que j'ai le temps
    complexite O(n log2(n))
    car on parcour la list avec fusion()
    et on fait ca récursivement en divisant la list en 2
    n fois le resultat de trie_fusion des moitier de liste
    L : list[int | float | any]
    """
    if len(L) < 2:
        return L
    return fusion(trie_fusion(L[0:len(L)//2]), trie_fusion(L[len(L)//2:]))


def occurence_lettres(stin):
    """ Cette fonction doit renvoyer un dictionnaire de type constitue des
        occurrences des caractères presents dans la phrase.
    complexite O(n) + hash
    stin : str
    return : dict[str,int]
    """
    # on cree un dictionnaire
    return_ = {}
    for char in stin:
        # pour tout les caractère donnee en paramètre
        # on augmente son nombre d'occurence de 1
        return_[char] = return_.get(char, 0) + 1
        # note la fonction dict.get(key,default) donne la valeur dans le dictionnaire
        # sinon le default donnee en paramètre

    return return_


def ex1():
    print('occurence_lettres("hello world !") : ',
          occurence_lettres("hello world !"))
    assert occurence_lettres("hello world !") == {
        'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 2, 'w': 1, 'r': 1, 'd': 1, '!': 1}

    print('occurence_lettres("programming") : ',
          occurence_lettres("programming"))
    assert occurence_lettres("programming") == {
        'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}

    print('occurence_lettres("bonjour") : ', occurence_lettres("bonjour"))
    assert occurence_lettres("bonjour") == {
        'b': 1, 'o': 2, 'n': 1, 'j': 1, 'u': 1, 'r': 1}

    # some more test donnees dans l enoncer
    assert occurence_lettres("bonjour’ ")["o"] == 2
    assert occurence_lettres("Bebe’ ")["b"] == 1
    assert occurence_lettres("Bebe’ ")["B"] == 1
    assert occurence_lettres("Hello world !")[" "] == 2

    print()


def ex2():
    # test donn" dans l enoncer
    print("fusion([1,6,10],[0,7,8,9]) : ", fusion([1, 6, 10], [0, 7, 8, 9]))
    assert fusion([1, 6, 10], [0, 7, 8, 9]) == [0, 1, 6, 7, 8, 9, 10]
    """
    import random
    TIMES = 100
    MAXE = 100
    MINE = 0
    print("trie_fusion",trie_fusion([random.randrange(MINE,MAXE) for x in range(TIMES)]))
    """
    print()


if __name__ == "__main__":
    # regex for pretty print
    # print\((?!")(?!')(.*)\)
    # print('$1 : ',$1)

    # please use auto-formating

    print("ex1\n")

    ex1()

    print("ex2\n")

    ex2()