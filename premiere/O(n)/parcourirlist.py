l=[52,23,12,15,14,54,17,88,1,0,56,9,58,66,17,88,45,887,120,154,548,17,88,1,36,366,501,3,17,99]
def par(l,r):
    return [i for i,o in enumerate(l) for len(r) if l[o] == r]

print(par(l,[17,88,1]))