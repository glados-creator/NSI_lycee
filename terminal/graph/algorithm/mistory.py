class File:
    ''' classe File
    création d'une instance File avec une liste
    '''

    def __init__(self):
        self.L = []

    def vide(self):
        return self.L == []

    def defiler(self):
        assert not self.vide(), "file vide"
        return self.L.pop(0)

    def enfiler(self, x):
        self.L.append(x)

    def taille(self):
        return len(self.L)

    def sommet(self):
        return self.L[0]

    def present(self, x):
        return x in self.L


def voisin(G, sommet):
    return G[sommet]


def fonct_inconnue(G, sommet):
    sommets_visites = []
    f = File()
    sommets_visites.append(sommet)
    f.enfiler((sommet, -1))
    while f.vide() == False:
        print(f.L)
        (tmp, parent) = f.defiler()
        voisins = voisin(G, tmp)
        for vois in voisins:
            if vois not in sommets_visites:
                sommets_visites.append(vois)
                f.enfiler((vois, tmp))
            elif vois != parent:
                return True
    return False


G = dict()
G['a'] = ['b', 'c']
G['b'] = ['a', 'd', 'e']
G['c'] = ['a', 'd']
G['d'] = ['b', 'c', 'e']
G['e'] = ['b', 'd', 'f', 'g']
G['f'] = ['e', 'g']
G['g'] = ['e', 'f', 'h']
G['h'] = ['g']

if fonct_inconnue(G, 'a') == True:
    print("Le graphe cyclique")
else:
    print("Le graphe est pas cyclique")
