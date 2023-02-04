import profile
"""
def main(lt,x):

    def inner(deb,fin,trouve,m):
        if lt[m] == x:
            trouve = 1
        else:
            m += 1
        
        return trouve , deb , fin , m

    trouve = 0
    deb = 0
    fin = len(lt)
    m= 0
    while not trouve:
        trouve , deb , fin , m = inner(deb,fin,trouve,m)
    assert lt[m] == x , "erreur"
    print("trouve",trouve ,"m",m)
    main(lt,lt[m-1])
"""


def main(lt,x):

    def inner(deb,fin,trouve):
        m=(deb+fin)//2
        print("deb",deb,"fin",fin, m)
        if lt[m]==x :
            trouve = 1
        elif x> lt[m] :
            deb = m+1
        else: 
            fin = m-1
        return trouve , deb , fin , m

    trouve = 0
    deb = 0
    fin = len(lt)
    while (trouve==0 and deb<=fin):
        trouve , deb , fin , m = inner(deb,fin,trouve)
    assert lt[m] == x , "erreur"
    print("trouve",trouve ,"m",m)
    main(lt,lt[m-1])

L = [1,5,6,7,9,12,16,19,25,36,41,44,49,51,55,57,60,61,62,65,66,68,69,71,73,75,77,81,82,99,101,103,105,108,111,112,115
,119,120,123,125,127,129,133,136,138,141,144,145,150,160,166,168,169,170,172,175,180,182,186,188,200,202,205,
208,209,212,215,218,220,224,228,233,235,239,244,245,251,252,254,256,258,260,261,262,268,270,271,278,301,303,
305,307,311,315,316,319,320,322,325,329]
number = 329

profile.run('main(L,number)',sort='ncall')