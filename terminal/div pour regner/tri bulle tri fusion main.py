import asyncio
import random
import time

def gen_list(maxx):
    return [random.randint(0,x) for x in range(maxx)]

async def fusion(l1 : list,l2 : list):
    r = []
    i1 = 0
    i2 = 0
    le1 = len(l1)
    le2 = len(l2)
    ### print("debug len fusion",le1,le2,l1,l2)

    ### edgecase safety
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

    ### print("before",r)
    ### grab leftover
    if i1 < le1:
        ### print("extend by l1")
        r.extend(l1[i1:])
    if i2 < le2:
        ### print("extend by l2")
        r.extend(l2[i2:])
    ### else : list where equal
    ### print("manual verify",i1,"/",le1,i2,"/",le2,l1,l2)
    ### print("fusion return",r)
    ### print()
    return r 

async def trifusion(l : list):
    ### 0 ou 1 elem
    ### print("debug len trifusion",len(l),l)
    if len(l) < 2:
        ### print("return l")
        return l
    ### div par 2
    divle = len(l)//2
    l1 = l[0:divle]
    l2 = l[divle:]
    ### print("debug len trifusion",divle,l1,l2)
    ### input()
    return await fusion(await trifusion(l1),await trifusion(l2))

### bad tri bulle

### def tri_bulle(tab):
###     n=len(tab)
###     for i in range(0,n):
###         for j in range(0,n - 1):
###             if tab[j + 1] <= tab[j] :
###                 tab[j], tab[j+1] = tab[j+1],tab[j]
###     return tab

### bon tri a bulle

### def tri_bulle(tableau):
###     permutation = True
###     passage = 0
###     while permutation == True:
###         permutation = False
###         passage = passage + 1
###         for en_cours in range(0, len(tableau) - passage):
###             if tableau[en_cours] > tableau[en_cours + 1]:
###                 permutation = True
###                 # On echange les deux elements
###                 tableau[en_cours], tableau[en_cours + 1] = \
###                 tableau[en_cours + 1],tableau[en_cours]
###     return tableau

async def main(L):
    ### print("input",L)
    cached = await trifusion(L)
    ### print(cached)
    return cached

async def benchmark():
    per_inter = 100
    per_size = 1000

    def display(per_size,x : list):
        avg = sum(x)/len(x)
        print()
        print("total time")
        print(f"{avg} ns \t\t| {avg/1_000_000} ms ")
        print(f"{avg/len(x)} ns/elem \t| {avg/len(x)/1_000_000} ms/elem")
        print(f"{len(x)} list sorted , {per_size} elements per list")
        print(f"{min(x)} min ns time \t| {max(x)} max ns time")
        print(f"{min(x)/1_000_000} min ms time \t| {max(x)/1_000_000} max ms time")
        print()
    
    async def no_wait(v):
        start = time.perf_counter_ns()
        await main(v)
        return (time.perf_counter_ns()-start)
    
    print("multiple time same value set")
    v = gen_list(per_size)
    timed = []
    for x in range(per_inter):
        start = time.perf_counter_ns()
        await main(v)
        timed.append(time.perf_counter_ns()-start)
    
    display(per_size,timed)

    print("multiple time different value set")
    timed = []
    for x in range(per_inter):
        v = gen_list(per_size)
        start = time.perf_counter_ns()
        await main(v)
        timed.append(time.perf_counter_ns()-start)
    
    display(per_size,timed)
    v = gen_list(per_size)
    print("bandwidth single value set")
    display(per_size,await asyncio.gather(*[no_wait(v) for x in range(per_inter)]))
    print("bandwidth different value set")
    display(per_size,await asyncio.gather(*[no_wait(gen_list(per_size)) for x in range(per_inter)]))

    print("verification")
    verif = []
    for x in range(per_inter):
        v = gen_list(per_size)
        x = await main(v)
        verif.append((1,v,x) if sorted(v) != x else (0,))
    verification = list(filter(lambda x : x[0],sorted(verif,key=lambda x : x[0])))
    print(verification if verification else "no errors")
    

asyncio.run(benchmark())