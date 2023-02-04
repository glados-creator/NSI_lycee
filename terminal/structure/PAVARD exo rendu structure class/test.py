from math import factorial
from ratio import Rationnel

f = Rationnel(12, -15)
print(f)
# 12/-15
# print va appeller f.__str__ pour convertir
# l'object en string pour afficher
# return str(self.num)+'/'+str(self.den)
# les attribut sont ensuite eux même convertie en string
print(f.num, f.den)
# on accède directement au attribut de l'object
# qui sont convertie en string

f1 = Rationnel(7)
# f1 = Rationnel(num = 7 , # default dem = 1)
print(f1)
print(type(f1))
# <class 'ratio.Rationnel'>
# on affiche le type de f1
# c'est a dire la classe d'ou l'object a été instancier

"""
# À faire 6 :
# Suite OK
# -4/5
# -4 5
# 7/1
# <class 'ratio.Rationnel'>
"""

print()
f1=Rationnel(2,7)
f2=Rationnel(5,3)
print(f1.add(f2))
# 41/21 OK

print()
f1=Rationnel(2,7)
f2=Rationnel(5,3)
print(f1+f2)
# 41/21

"""
TEST
"""

print()
f1=Rationnel(15,12)
f2=Rationnel(8,15)
print("f1*f2",f1*f2)
# 6/35

print()
f1=Rationnel(2,7)
f2=Rationnel(5,3)
print("f1-f2",f1-f2)
# -29/21

print()
f1=Rationnel(2,7)
f2=Rationnel(5,3)
print("f1/f2",f1/f2)
# 6/35


"""
exo 2
"""

def nombre_euler(n):
    fact = 1
    r = Rationnel(1)
    for i in range(1, n+1):
        fact = fact * i
        r += Rationnel(1,fact)
    return r

print()
print("e : ",nombre_euler(50))
# 2666905705783137373306341322880702364612402788688346977445977371/981099780700431549793955102131121575625085211901952000000000000
# 2.718281828459045

"""
exo 3 approximation de pi pass
"""

def appropi(n):
    r = Rationnel(0)
    b = True
    for i in range(1, n+1,2):
        if b:
            b = False
            r += Rationnel(1,i)
        else:
            b = True
            r -= Rationnel(1,i)
    return Rationnel(4)*r

print()
print("pi :",appropi(100))
# 3400605476464206445954873476681150352328/1089380862964257455695840764614254743075
# 3.1215946525910105

"""
"""