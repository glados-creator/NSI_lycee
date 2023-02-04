import sys , os
import pickle

default_datafilename = "Titanic.csv"
default_loader = None # this is use to indicate custome loader filename to be imported (expect pickle)
default_guess = None
default_loop = None

guess = None

def tableprint(*arg):
    args = list(arg)
    # we use None to have a delimiter
    pr = [[]]
    while True:
        # parsing ...
        if not args:
            break
        elif args[0] == None:
            args.pop(0)
            if len(pr[-1]) == 0:
                pr.pop(0)
            try:
                truc = (args.pop(0),args.pop(0),args.pop(0),args.pop(0))
                pr.append(truc)
            except Exception as ex:
                print(ex)
        elif not isinstance(pr[-1],list):
            pr.append([(args.pop(0))])
        else:
            pr[-1].append((args.pop(0)))
    # that will be one AND the other element else we mess something up
    if len(pr) % 2 != 0 and not isinstance(pr[-1],tuple):
         # pr[i+1] doesn't existe so be nice and inject a default
        d = (None,None,None,None)
        pr.append(d)
    for i in range(0,len(pr)-1,2):
        assert isinstance(pr[i+1],tuple) , "don't known the odd element"
        pr[i+1] = list(pr[i+1]) # 'tuple' object does not support item assignment so we cast to list        # parse elements with controle and get elements length for alinement
        # pr[i] -> line (elements thaht will be on one line) | pr[i][x] -> element (str [cast anyway]) for string encaptulation |
        # pr[i+1] -> controle tuple (vertical char to put between elements , (tuple where to put them) , horizontale controle char)
        # example ("|" , (1, ... ) , "-" , None)
        # if the chr is None don't care about insertion
        # if the postion is None then don't care either (need to change call parameter)
        # ( { pr[i][x] + controle char } , <- len)
        # get max out of colone to calcul space between controle char and element for alinement
        for j,x in enumerate(pr[i]):
            pr[i][j] = str(x)
        if pr[i+1][0] is not None and pr[i+1][1] is not None : # vertical is not none
            if pr[i+1][1] == -1:
                # special case
                pr[i+1][1] = tuple(i for i in range(len(pr[i])))
            assert isinstance(pr[i+1][0],str) , "vertical controle char in not chr"
            for j in pr[i+1][1]:
                pr[i][j] = pr[i][j] + pr[i+1][0]
        pr[i] = [(j,len(j)) if len(j) != 0 else ("-",1) for j in pr[i]] # we will have to check that to last char is controle char for space padding
    
    # for each colone get max space
    # spaces = [ max([pr[i][j][1] for i in range(0,len(pr)-1,2)]) for j in range(len(pr[0])-1)]
    spaces = []
    for k in range(len(pr[0])-1):
        temp = []
        for i in range(0,len(pr),2):
            # print(k,"/",len(pr[0])-1,i/2,"/",len(pr)-1/2)
            # print(pr[i][k])
            temp.append(pr[i][k][1])
        spaces.append(max(temp)+1)
    spaces.append(10)
    spaces.append(10)
    try:
        for j in range(0,len(pr)-1,2):
            print()
            for i,element in enumerate(pr[j]):
                s = spaces[i] - element[1]
                print("",end=" ")
                print( ( element[0][0:-1] + (" "*s) +element[0][-1] ) if element[0][-1] is pr[j+1][0] else (element[0] + " "*s),end="")
            
            if pr[j+1][3] == -1:
                    # special case
                    pr[j+1][3] = tuple(i for i in range(len(pr[j])))
            if pr[j+1][2] is not None: # if controle chr is none than don't skip line
                print()
                for k in range(len(pr[j])):
                    print("",end=" ")
                    print( ( pr[j+1][2]*spaces[k] ) if k in pr[j+1][3] else (" "*spaces[k] ),end="")
    except TypeError as ex:
        print("\n","on ne peut imprimer que des caractères")
        print(ex)
    print()
    
def check(datafilename):
    """
    check if the data format is in right forme
    count the number of each charactere
    """
    print("ouverture du fichier " + str(datafilename) + " ... ")
    if datafilename[-3:] != "csv":
        return (False,"extension non valide")

    if not os.path.exists(datafilename):
        return (False,"fichier n'existe pas")

    letter = {}
    copy = None
    with open(datafilename,"r") as f:
        for x in f.read(-1):
            if x in letter:
                letter[x] += 1
            else:
                letter[x] = 1
        f.seek(0)
        copy = f.read(-1)
    
    if letter['"'] % 2 != 0:
        return (False,"nombre de " + '"' + '"' + '"' + " non valide")
    
    return (letter.items(),None,copy)

def importer(filename,default):
    try:
        return pickle.load(filename)
    except Exception as ex:
        print(ex)
        return default

def Dguess(first,data,firstindex):
    # first : list of separation / depth of firstindex if list if not crash
    # data : list data should be list of list depth of first else the loader made a mistake

    # return type , value
    # firstindex : int for index of first use for global %
    # or list to find value most probable
    # global / relational

    # guess = {
    #   var
    #   "pos" (possibility) : list tuple (pos str ; int) = [ :: list for each index of first list all possibilities ]
    #   "type" (self-explaining) for eahc first : list
    #   "value" (see return) : list
    #   
    #   "data" : tuple = (id , len)
    # }

    def rebuild():
        #global scale
        guess = {"pos" : [{} for x in first],"type":[() for x in first],"value":[() for x in first]}
        # posibilities
        # go through everything to have every posibility
        # we could or should discard selector where there is to many posibility bc it's probably unique
        # but the data is interesting
        # temp use after for counting
        temp = [[] for x in first] # need to creat new list for each list of possibilities
        print("....")

        for x in data:
            for i,f in enumerate(first):
                (temp[i]).append(x[i])
            # extra arg possibly added
        # 2nd parsing to count
        
        print("...")
        for i,table in enumerate(temp):
            for element in table:
                if element not in guess["pos"][i]:
                    guess["pos"][i][element] = 0
                guess["pos"][i][element] += 1
        # building of the types for each first
        print("..")

        def get_type(guess_pos):
            short = [type(x) for x in guess_pos.keys()]
            for a in short:
                if a != short[0]:
                    # can't handle
                    return None # multiple type per key so either something type AND an other type
            short = list(guess_pos.keys())[0] # there are only one type so grab the first element
            if len(guess_pos.keys()) == 2:
                return bool
            # technically there are all string so i'll use str methode
            elif short.isnumeric():
                return int
            elif short.isdecimal():
                return float
            else:
                return str # fallback to string if string element doesn't format well to " start
            """
            elif short[0] == '"':
                return str # possible for the type to not be str.isalpha() because of unicode wizardry
            empty string break it
            """
        
        for i,x in enumerate(first):
            # we are only going to handle one type for each
            # bool , str , int , float types are handle
            guess["type"][i] = (get_type(guess["pos"][i]),guess["pos"][i])
            if guess["type"][i] is not None: 
                guess["value"][i] = (max(guess["pos"][i].items(),key=lambda x:x[1]))[0]
            else:
                guess["value"][i] = None
        print(".")

        # rebuild data cache condition 
        guess["data"] = (id(data),len(data))
        return guess 
        # local guess to this function scope need to by return 
        # to be assigne to global guess at function depth -1
    """
    def find(l,*args):
        args = list(args) # handy
        # length and path
        # this is where really the knn algorithm is
        # assuming that a entry don't existe already
        # 
        # check if entry don't already existe by the search algorithm
        # search passsenger
        print("recherche ...")
        r = []
        try:
            for j,d in enumerate(data):
                    if str(d[i]) == p:
                        r.extend((str(j),*d,None,"|",(0,),None,None))
            print("...")
            for j,d in enumerate(data):
                if p in str(d[i]):
                    r.extend((str(j),*d,None,"|",(0,),None,None))
        except Exception as ex:
            print(ex) # debug but proceed
        else:
            # an entry actuelly existe so return that
            print("un passager rechercher existe déja")
            tableprint(*first,None,"|",(0,),"-",-1,*r)
            return r
        # so no entry existe so get similar entry
        # core algorithm of the knn 
        #
        # for each first get type and have default
        # be nice "" -> "default str" always usefull
        #
        # get similar cases and see
        print("ok")
        raise
    """
    
    if isinstance(firstindex,int):
        global guess # use for cache
        if guess is not None and id(data) == guess["data"][0] and len(data) == guess["data"][1]:
            pass # cache still valide
        else:
            guess = rebuild()
        return (guess["type"][firstindex], guess["value"][firstindex])

def knn(first,data,guess):
    print("\tKNN algorithm : ")
    per = ["" for x in first]
    while True:
        tableprint(*first,None,"|",(0,),"-",-1,*per)
        p = input("que voulez-vous ?\n\t0 - entrer valeur\n\t1 - rechercher\n\t2 - voire le type et la valeur de base\n\t3 - voire les possibilitées\n\t8 - menu principale\n\t9 - data\n : ")
        if p == "" or p == "q":
                    return
        elif p == "0":
            # input
            for i,x in enumerate(first):
                print(i," : ",x)
            while True:
                i = input("quelle index voulez vous rentrer ? : ")
                if i in [str(x) for x,_ in enumerate(first)]:
                    break
                if i == "" or i == "q":
                    return
            per[int(i)] = input("quelle est la valeur ? : ")
        
        elif p =="1":
            # rechercher
            for i,x in enumerate(first):
                print(i," : ",x)
            while True:
                e = input("quelle index voulez vous chercher ? : ")
                if e in [str(x) for x,_ in enumerate(first)]:
                    break
                if e == "q":
                    return
            
            print("recherche ...")
            # get everything we can
            # if only one possibility do that
            r = data.copy()
            for i,f in enumerate(first):
                temp = []
                temp = r.copy()
                r = []
                for j,x in enumerate(temp):
                    if x is None:
                        # data is None so we can't know
                        r.append(x)
                    elif per[i] == "":
                        # not set
                        r.append(x)
                    elif x[i] == per[i]:
                        # set
                        r.append(x)
                    # else discard data
                if len(r) == 0 or len(r) == 1:
                    break
            
            if len(r) == 1:
                # found a guy
                print("une entrée existe déja")
                per = r[0]
                tableprint(*first,None,"|",(0,),"-",-1,*r[0])
            elif len(r) != 0:
                # found many
                print("des entrées existe déja")
                temp = []
                for x in r:
                    temp.extend((*x,None,None,None,None,None))
                tableprint(*first,None,"|",(0,),"-",-1,*temp)
                
            elif len(r) == 0:
                print("KNN")
                print("résultat proche")
                try:
                    r = temp.copy()
                    temper = []
                    for x in r:
                        temper.extend((*x,None,None,None,None,None))
                    tableprint(*first,None,"|",(0,),"-",-1,*(temper[0:5]))
                except:
                    pass
                types = []
                for i,x in enumerate(first):
                    types.append(guess(first,data,i)[0][0])

                def collision(per,element):
                    r = 0
                    for t,f in enumerate(first):
                        try:
                            if per[t] != "":
                                if (types[t] is int) or (types[t] is float):
                                    r += ( float(per[t]) - float(element[t])) if float(element[t]) < float(per[t]) else (float(element[t]) - float(per[t]))
                                elif types[t] is bool and per[t] != element[t]:
                                    r+= 1
                        except:
                            r += 1
                    return r
                
                k = [(collision(per,x),x) for x in r]
                sorted(k,key=lambda x:x[0])
                per = k[0][1]
                print("distance",k[0][0])
                print("max/min",max(k,key=lambda x:x[0]),min(k,key=lambda x:x[0]))
        
        elif p == "2":
            # default value
            for i,x in enumerate(first):
                print(x,",",guess(first,data,i)[0][0]," : (default) '",guess(first,data,i)[1],"'")
        elif p == "3":
            for i,x in enumerate(first):
                print(i," : ",x)
            while True:
                i = input("quelle index voulez vous rentrer ? : ")
                if i in [str(x) for x,_ in enumerate(first)]:
                    break
                if i == "" or i == "q":
                    return
            pos = guess(first,data,int(i))
            total = 0
            for x in pos[0][1].items():
                total += x[1]
            print("il y a ",len(pos[0][1].keys())," possibilitées")
            temp = [("'"+str(x)+"'",y,y/total*100,"%",None,None,None,None,None) for x,y in pos[0][1].items()]
            f = []
            for x in temp:
                f.extend(x)
            if len(pos[0][1].keys()) > 15:
                i = input("il y a beaucoup de valeur , voulez-vous tous afficher ? : ")
                if i.lower() == "y":
                    tableprint("caractère","utiliser","total%",None,"|",(0,),"-",-1,*f)
                else:
                    tableprint("caractère","utiliser","total%",None,"|",(0,),"-",-1,*f[0:15])
            else:
                    tableprint("caractère","utiliser","total%",None,"|",(0,),"-",-1,*f)
            i = input("voire les données brut ? :")
            if i.lower() == "y":
                print(pos)
        elif p == "8":
            return
        elif p == "9":
            print(repr(per))
        else:
            print("option incorrect")

def Dloader(letter,data):

    def custome_strip(S,sep):
        # parsing string ...
        r , i , f = [] , -1 , None
        S += sep
        # print(S)
        while True:
            f = S.find(sep ,i+1)
            if f == -1:
                return r
            if "²" in S[i+1:f]:
                # r.append(S[i:S.find("'")])
                f = S.find("²",S.find("²",i)+1)
                f += 1
            r.append(S[i+1:f].replace("²",'"'))
            i = f
    
    try:
        sep = max(letter,key=lambda x: x[1])[0] # get the max character should be the delimiter
        if sep != ",":
            print("erreur dans le séparateur")
        sep = ","
        first , *strip = data.split("\n") # if we keep it simple with one thing per ligne
        #           first               elements                                                                                    separator
        return (first.split(sep),[custome_strip(x.replace('""',"²").replace('²²','³').replace('"',""),sep) for x in strip],sep)
    except Exception as ex:
        return (None,False,ex)

def Dloop(loader,guess):
    data = None
    while True:
            r = input("\nselectionner votre choix:\n\t0 - importer une table de donnée\n\t1 - voire les valeurs par défaut\n\t2 - afficher toute les valeurs manquantes\n\t3 - ajouter une entrée\n\t4 - enlever une entrée\n\t5 - rechercher une entrée\n\t6 - modifier une entrée\n\t7 - sauvegarder les changement\n\t8 - quitter\n\t9 - avancer\n : ")

            if r == "0":
                # importing
                data = check(default_datafilename)
                # letters , false if error ; error if any ; file data copy if success
                
                if not data[0]:
                    print("le fichier par défaut "+ default_datafilename + " n'est plus valide")
                    while not data[0]:
                        print(data[1])
                        data = check(input("indiquer le nom du fichier a ouvrire : "))
                
                print("transformation de la table ...")

                # user test so loadtable and keep it in memory if user agree
                # table , separateur = laoder( letters , file data copy)
                first , data , sep =  loader(data[0],data[2])

                if not data:
                    print("error in loader : ", sep)
                else:
                    if data[-1] == [] or data[-1] == [""] or data[-1] == None:
                        data.pop()
                    print("separateur : " + '"',sep,'"')
                    # count the number of charater to have to space needed because of alignement
                    temp = []
                    for x in data[0:3]:
                        temp.extend(x)
                        temp.extend((None,"|",(0,),None,None))
                    tableprint(*first,None,"|",(0,),"-",-1,*temp)
                    print("... "+str(len(data)-3)+" +")
                print("\ntable importer")

            if not (r == "0" or r =="8") and not data:
                    print("pas de table importer")
            elif r =="0":
                pass
            
            elif r == "1":
                # default value

                p = input("0 - voire les valeur par défaut global du tableau\n1 - chercher une valeur local\n:")
                if p == "0":
                    l = [] # (type , value)
                    for i,_ in enumerate(first):
                        l.append(guess(first,data,i))
                    tableprint(sep,*first,None,"|",(0,),"-",-1,"types",*[x[0][0] for x in l],None,"|",(0,),None,None,"défault",*[x[1] for x in l])
                elif p == "1":
                    knn(first,data,guess)
                else:
                    print("valeur incorrect")
            elif r == "2":
                # missing value
                r = []
                for i,passenger in enumerate(data):
                        for x,f in enumerate(first):
                            if not passenger[x]:
                                r.extend((*passenger,None,"|",(0,),None,None))
                                break
                tableprint(*first,None,"|",(0,),"-",-1,*r)
            
            elif r == "3":
                # add passenger
                r = []
                for x in first:
                    r.append(input(str(x) + " ? : "))
                data.append(r)
            elif r == "4":
                # remove passenger
                i = input("quel est l'index du passager ? : ")
                if not (i.isnumeric() or i == "-1"):
                    print("charactère non valide")
                else:
                    i = int(i)-1
                    tableprint(*first,None,"|",(0,),"-",-1,*data[i])
                    c= input("confirmer y/n ? : ")
                    if c.lower() == "y":
                        data.remove(data[i])
                        print("effacer")
                    else:
                        print("annuler")
            elif r == "5":
                # search passsenger
                for i,x in enumerate(first):
                    print(i," : ",x)
                while True:
                    i = input("qu'est ce que vous voullez chercher ? : ")
                    if i in [str(x) for x,_ in enumerate(first)]:
                        break
                i = int(i)
                p = input("quelle est le résultat rechercher ? : ")
                r = []
                print("recherche ...")
                for j,d in enumerate(data):
                    if str(d[i]) == p:
                        r.extend((*d,None,"|",(0,),None,None))
                print("...")
                for j,d in enumerate(data):
                    if p in str(d[i]):
                        r.extend((*d,None,"|",(0,),None,None))
                tableprint(*first,None,"|",(0,),"-",-1,*r)
                
            elif r == "6":
                # modify passenger
                while True:
                    p = input("quelle est l'index du passager ? : ")
                    if p.isnumeric():
                        break
                p = int(p)-1
                l = True
                while l:
                    tableprint(*first,None,"|",(0,),"-",-1,*data[p])
                    for i,x in enumerate(first):
                        print(i," : ",x)
                    print("'q' ou rien pour quitter")
                    while True:
                        i = input("qu'est ce que vous voullez modifier ? : ")
                        if i in [str(x) for x,_ in enumerate(first)]:
                            break
                        if i == "" or i == "q":
                            l = False
                            break
                    if l:
                        i = int(i)
                        data[p][i] = input("nouvelle valeur pour '"+str(first[i])+"' : ")
                    
            elif r == "7":
                # save
                with open("out.csv","w") as f:
                    # header
                    for x in first[0:-1]:
                        f.write(x+",")
                    f.write(first[-1]+"\n")
                    #data
                    for x in data:
                        f.write('"')
                        for i,_ in enumerate(first[0:-1]):
                            f.write(x[i].replace('"','""').replace('³','""""')+",")
                        f.write(x[-1].replace('"','""').replace('³','""""')+'"\n')
                        
            elif r == "8":
                # quit
                return 0
            elif r == "9":
                i = input("0 - eval\n>")

                if i == "0":
                    try:
                        print(eval(input("#")))
                    except Exception as ex:
                        print(ex)
            else:
                print("option non valide")

def main():
    global default_datafilename  , default_loader , default_guess , default_loop
    data = None
    loader = importer(default_loader,Dloader) if default_loader else Dloader
    guess = importer(default_guess,Dguess) if default_guess else Dguess
    loop = importer(default_loop,Dloop) if default_loop else Dloop

    try:
        loop(loader,guess)
    except Exception as ex:
        print(ex)
        while True:
            i = input("voulez-vous quitter ? : y/n ")
            if i.lower() == "y":
                return
            elif i.lower() == "n":
                main()
    

if __name__ == "__main__":
    # Dloop(Dloader,Dguess)
    main()
