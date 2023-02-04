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


class Pile:
    ''' classe Pile
    création d'une instance Pile avec une liste
    '''

    def __init__(self):
        self.L = []

    def vide(self):
        return self.L == []

    def depiler(self):
        assert not self.vide(), "Pile vide"
        return self.L.pop()

    def sommet(self):
        assert not self.vide(), "Pile vide"
        return self.L[-1]

    def empiler(self, x):
        self.L.append(x)