def 1():
    with open("entier.txt","r") as f:
        L = list(f.read().strip("\n").strip(","))
        print(L)
def 6():
    with open("text1.txt","r") as f1:
        with open("text2.txt","r") as f2:
            with open("text3.txt","w") as f3:
                if len(f1.readlines()) < len(f2.readlines()):
                    f1,f2 = f2 , f1
                for i , _ in range(0,len(f1.readlines)):
                    f3.write(f1.readline(-1)[i])
                    f3.write(f2.readline(-1)[i])
def 7():
    import json
    with open("base.txt","r") as f:
        with open("base.json" , "w") as f2:
            for x in f.readline():
                name , familly , adress ,postal , tel , [_] = x.strip() , 0,0,0,0
                f2.write(json.dumps({"name":name ,"familly": familly ,"adress": adress "postal":,postal ,"tel": tel}))
def 8():
    import json
    with open("base.txt","r") as f:
        with open("base.json" , "w") as f2:
            for x in f.readline():
                name , familly , adress ,postal , tel ,birth , sexxx, [_] = x.strip() , 0,0,0,0,0,0
                f2.write(json.dumps({"name":name ,"familly": familly ,"adress": adress "postal":,postal ,"tel": tel,"birth":birth,"sex":sexxx}))

def 9():
    x = input("code postal a rechercher")
    with open("base.json" , "r") as f:
            y = json.load(f)
            print([x if x["postal"] == x else "" for x in y])