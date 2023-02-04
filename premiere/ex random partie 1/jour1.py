# Créé par arthur.pavard, le 06/09/2021 en Python 3.7

optime = False

def billets(n):
    ls = [1,2,5,10, 20, 50, 100, 200 , 500] if optime else [1,2,3,5,7,11]
    ls = ls[::-1]
    re = []

    def recur(t:int,l:list):
        try:
            if sum(l) + t > n:
                raise RuntimeError
            else:
                return t
        except Exception:
            return -1

    for x in ls:
        while not sum(re) >= n:
            if recur(x,re) > 0:
                re.append(x)
            else:
                break
    return re


try:
    x = int(input("enter : "))
    print(billets(x))
    print(len(billets(x)))
    print(sum(billets(x)))
except Exception as ex:
    print(ex)