import functools

def encrypt(key,word):
    # fist need to have bin key as long as word
    tmpk = []
    i = 0
    x = 0
    while i < len(word):
        if x > len(key)-1:
            x -= len(key)
        tmpk.append(key[x])
        i += 1
        x += 1
    assert len(key) <= len(word)
    bkey = [int(bin(ord(x)),2) for x in ("".join(tmpk))]
    bword = [int(bin(ord(x)),2) for x in word]
    r = []

    print("bkey",bkey)
    print("bword",bword)
    for i,x in enumerate(bword):
        r.append(x ^ bkey[i])
    print("raw ",list(map(lambda x : (int(x)),r)))
    return "".join(map(lambda x : chr(int(x)),r))

def encrypt_reduce(key,word):
    return functools.reduce(
        lambda a , w: (w[0], a[1] + str(
        chr(
            
                int(bin(
                    ord(key[w[0]%len(key)])
                    ),2) 
                ^ 
                int(bin(ord(w[1])),2)
        )
        ))
        ,enumerate(word),(0,""))

def encrypt_map(key,word):
    return "".join(map(
        lambda k,w: str(
        chr(
            
                int(bin(ord(k)),2) 
                ^ 
                int(bin(ord(w)),2)
        )
        )
        ,[key[x%len(key)] for x in range(len(word))],word))

if __name__ == "__main__":
    word = "Bonjour, comment allez-vous ?"
    key = "mystère"
    print("key",len(key)-1,key)
    print("data",len(word)-1,word)
    print("encrypt",encrypt(key,word))
    print()
    print(encrypt_reduce(key,word))
    print(encrypt_map(key,word))
    print()
    print(encrypt(key,encrypt(key,word)))

