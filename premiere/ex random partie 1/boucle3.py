# Créé par arthur.pavard, le 13/09/2021 en Python 3.7
num = 10
try:
    if num == 0:
        import numpy

        def xfrange(start, stop, step):
            i = 0
            while start + i * step < stop:
                yield start + i * step
                i += 1

        for i in numpy.arange(1,10,0.5):
            print(i)

    if num == 1:
        x= -1
        while 0 < x and x < 101:
            x= int(input("value : "))

    if num == 2:
        n = 0
        u = int(input("number : "))
        print(u)
        while u > 0:
            u = 0.5*u - 3*n
            print("level : ", n)
            n += 1

    if num == 3:
        i = int(input("num : "))
        for x in range(i):
            for _ in range(x+1):
                print('*', end='')
            print('')

    if num == 5 :
        x = input("truc a inverser : ")
        print("".join(list(x)[::-1]))

    if num == 10:
        i : str = str(input("cypher : ")).upper()
        key = int(input("key : "))

        def cy(inp , key):
            i = list( inp.replace("é","e").replace("à","a").replace("è","e"))

            x = [ord(x)+key+26 if ord(x)+key < 65 else ord(x)+key-26 if ord(x)+key > 90 else ord(x)+key for x in i]
            for f in x:
                print(str(chr(f)).lower().replace("'"," ").replace("3",",") , end='')

        if key < 0:
            for f in range(0,26):
                print(cy(i,f))
        else:
            print(cy(i,key))

except Exception as f:
    print(f)

