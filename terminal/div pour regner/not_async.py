import random
import time


def gen_list(maxx):
    return [random.randint(0, x) for x in range(maxx)]


def fusion(l1: list, l2: list):
    r = []
    i1 = 0
    i2 = 0
    le1 = len(l1)
    le2 = len(l2)
    ### print("debug len fusion",le1,le2,l1,l2)

    # edgecase safety
    if le1 == 0:
        return l2
    if le2 == 0:
        return l1

    while i1 < le1 and i2 < le2:
        if l1[i1] < l2[i2]:
            r.append(l1[i1])
            i1 += 1
        else:
            r.append(l2[i2])
            i2 += 1

    # print("before",r)
    # grab leftover
    if i1 < le1:
        ### print("extend by l1")
        r.extend(l1[i1:])
    if i2 < le2:
        ### print("extend by l2")
        r.extend(l2[i2:])
    # else : list where equal
    ### print("manual verify",i1,"/",le1,i2,"/",le2,l1,l2)
    ### print("fusion return",r)
    # print()
    return r


def trifusion(l: list):
    # 0 ou 1 elem
    ### print("debug len trifusion",len(l),l)
    if len(l) < 2:
        ### print("return l")
        return l
    # div par 2
    divle = len(l)//2
    l1 = l[0:divle]
    l2 = l[divle:]
    ### print("debug len trifusion",divle,l1,l2)
    # input()
    return fusion(trifusion(l1), trifusion(l2))


def tri_bulle(tab):
    n=len(tab)
    for i in range(0,n):
        for j in range(0,n - 1):
            if tab[j + 1] <= tab[j] :
                tab[j], tab[j+1] = tab[j+1],tab[j]
    return tab

def benchmark():
    
    print("tri fusion 100 fois 100 elem")
    v = gen_list(100)
    mstart = time.perf_counter()
    timed = []
    for x in range(100):
        start = time.perf_counter()
        trifusion(v)
        timed.append(time.perf_counter()-start)
    print("total time taken",time.perf_counter()-mstart,"s")
    print("avg",sum(timed)/(len(timed)-1),"s")
    print()

    print("tri fusion 100 fois 1000 elem")
    v = gen_list(1000)
    mstart = time.perf_counter()
    timed = []
    for x in range(100):
        start = time.perf_counter()
        trifusion(v)
        timed.append(time.perf_counter()-start)
    print("total time taken",time.perf_counter()-mstart,"s")
    print("avg",sum(timed)/(len(timed)-1),"s")
    print()

    print("tri bulle 100 fois 100 elem")
    v = gen_list(100)
    mstart = time.perf_counter()
    timed = []
    for x in range(100):
        start = time.perf_counter()
        tri_bulle(v)
        timed.append(time.perf_counter()-start)
    print("total time taken",time.perf_counter()-mstart,"s")
    print("avg",sum(timed)/(len(timed)-1),"s")
    print()

    print("tri bulle 100 fois 1000 elem")
    v = gen_list(1000)
    mstart = time.perf_counter()
    timed = []
    for x in range(100):
        start = time.perf_counter()
        tri_bulle(v)
        timed.append(time.perf_counter()-start)
    print("total time taken",time.perf_counter()-mstart,"s")
    print("avg",sum(timed)/(len(timed)-1),"s")
    print()

    
    ### print("verification")
    ### verif = []
    ### for x in range(per_inter):
    ###     v = gen_list(per_size)
    ###     x = await main(v)
    ###     verif.append((1,v,x) if sorted(v) != x else (0,))
    ### verification = list(filter(lambda x : x[0],sorted(verif,key=lambda x : x[0])))
    ### print(verification if verification else "no errors")

benchmark()