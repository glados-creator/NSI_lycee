### recherche doublons
def doublons_brute(T : list):
    L = []
    for x in T:
        if x in L:
            return True
        L.append(x)
    return False

### doublons par index
def double_index(T : list):
    L = []
    for _ in range(366):
        L.append(False)
    for x in T:
        if L[x]:
            return True
        L[x] = True
    return False

def double_bitarray(T : list):
    bi = 0
    for x in T:
        if bi & 1 << x:
            return True
        bi += 1 << x
        print(bin(bi))
        
    return False

def double_bank(T : list):
    ma = max(T)
    ### répartition par bank
    ### x bank de y bits
    ### 4kibi align to be cache friendly
    ### 2**12
    page = [0 for x in range(ma//2**12)]
    for x in T:
        pass

### print(double_bitarray([0,0,2,3,4,5,5,10,0]))

def double_pythonic(T : list):
    L = {*T}
    return False if len(L) == len(T) else True
