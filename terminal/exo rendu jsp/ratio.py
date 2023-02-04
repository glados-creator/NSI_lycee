"""
# Le cahier des charges
# On doit créer une classe Rationnel dont les instances auront les attributs numerateur et denominateur (celui-ci ne
# pourra être nul !!) et des méthodes pour :
#   -Simplifier la fraction et normaliser son écriture.
#   -Additionner deux fractions.
#   -Soustraire deux fractions.
#   -Multiplier et diviser deux fractions

# Méthode :
# Un peu de Mathématiques.
# La fraction 12/-15 doit s’écrire -4/5.
# Il y a eu simplification par le PGCD de 12 et 15 et transfert du signe au numérateur. Il nous faudra :
#   -Une fonction qui calcule le PGCD.
#   -Une méthode pour simplifier et normaliser la fraction.
"""

"""
# Thanks internet
# def gcd(a, b):
#   
#     # Everything divides 0
#     if (a == 0):
#         return b
#     if (b == 0):
#         return a
#   
#     # base case
#     if (a == b):
#         return a
#   
#     # a is greater
#     if (a > b):
#         return gcd(a-b, b)
#     return gcd(a, b-a)
"""


def pgcd(x, y):
    # Euclidean algo
    while (y):
        x, y = y, x % y
    return abs(x)

# fichier ratio.py


class Rationnel:
    # création des instances
    def __init__(self, num, den=1):  # par défaut le dénominateur vaut 1
        if den == 0:
            # on déclenche une exception spécifique
            raise ZeroDivisionError('denominateur nul')
        else:
            self.num = num
            self.den = den
            self.normalise()
    # pour voir une fraction sur la console appelée par print

    def __str__(self):
        return str(self.num)+'/'+str(self.den)

    # simplification des fractions
    def normalise(self):
        g = pgcd(abs(self.num), abs(self.den))
        self.num = self.num // g
        self.den = self.den // g

        if (self.num*self.den < 0):
            if self.den < 0:
                self.den = -self.den
                self.num = -self.num
        else:
            if self.den < 0:
                self.den = -self.den
                self.num = -self.num
    
    def add(self,other):
        return Rationnel(self.num*other.den+self.den*other.num,self.den*other.den)
    
    def __add__(self, other): #addition
        n=self.num*other.den+other.num*self.den
        d=self.den*other.den
        return Rationnel(n,d)
    
    def __sub__(self,other):
        n=self.num*other.den-other.num*self.den
        d=self.den*other.den
        return Rationnel(n,d)
    
    def __mul__(self,other):
        n=self.num*other.num
        d=self.den*other.den
        return Rationnel(n,d)

    def __truediv__(self,other):
        n=self.num*other.den
        d=self.den*other.num
        if d == 0:
            raise ZeroDivisionError()
        return Rationnel(n,d)
