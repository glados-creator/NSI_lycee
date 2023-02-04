# Créé par arthur.pavard, le 16/09/2021 en Python 3.7
"""
def eleMax(liste : list = [],debut: int = 0 ,fin : int = -1) ->int:
    return max(liste[debut:fin])

serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
print(eleMax(serie))
print(eleMax(serie, 2, 5))
print(eleMax(serie, 2))
print(eleMax(serie, fin =3, debut =1))
"""

def adder(x11:bin,x12:bin):
    def conv(a:bin,b:bin):
        print(a,b)
        if len(a) > len(b):
            b = b.zfill(len(a) - len(b))
        elif len(b) > len(a) :
            a = a.zfill(len(b) - len(a))
        return a,b

    def __binad(a : bin = 0,b : bin = 0,c : bin = 0):
        final = (a ^ b) ^ c
        carry = ((a ^ b) & c) ^( a & b)
        return final , carry

    r= [bin(255)]
    print(x11,x12)
    x1,x2  = conv(x11,x12)
    old = 0

    for x in range(2,len(x1 if len(x1) > len(x2) else x2)):
        print(x,x1,x2)
        print(x,x1[x],x2[x])
        r[x] , old = __binad(x1[x],x2[x],old)
    return r[:len(x1)]

print( adder(bin(10),bin(5)))


