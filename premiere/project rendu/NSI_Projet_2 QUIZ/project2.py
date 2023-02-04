import json, random , os , sys
import malicious

def js(file:str)->dict:
    return json.load(open(file,"r")) if os.path.exists("data.json") else {"fichier non présent":{"type":-1}}

def gen(num:int)->dict:
    if not isinstance(num,int):
        try:
            num = int(num)
        except Exception:
            return -1

    def ran(typ):
        #génére un réponse de type approprier str
        #fonction interne n'est pas utiliser autre part
        if isinstance(typ,list):
            return "".join([str(random.randint(min(typ),max(typ))) for x in range(len(typ))])
        elif isinstance(typ,float):
            x = random.random()
            return str(typ - (x if random.random() > 0.5 else -x))
        elif isinstance(typ,int):
            return str(typ - (random.randint(typ-1,typ+1) if random.random() > 0.5 else -random.randint(typ-1,typ+1)))
        elif isinstance(typ,str):
            x = list(typ)
            random.shuffle(x)
            return "".join([str(x) for x in typ])
        else:
            raise RuntimeError(f"unhandle type {type(typ)} in ran gen")

    ret = {}
    for n in range(num):
        funcs = [getattr(malicious,x) for x in dir(malicious) if '__' not in x] #prendre les fonction
        random.shuffle(funcs)
        x = funcs[0] #choisi une fonction aléatoire
        v = random.randint(-100,100) # détermine une valeur aléatoire
        if v == 0:
            v=1
        typ = random.randint(0,3) # détermine le type de question 1/3 type 0 2/3 type 1
        #le générateur ne peux pas faire des question type 3
        Lans = random.randint(0,1) # détermine si il y aura 2 ou 4 réponse
        i = random.randint(0,1) if Lans else random.randint(0,3) #détermine l'emplacement de la bonne réponse
        résultat = x(v)
        valeur = v

        #détermine si il y a changement de type
        if isinstance(x(v),tuple):
            #si la fonction n'attend pas un simple nombre en inp
            #failsafe si la fonction revoie plus que on n'attend ne pas faire d'erreur
            valeur , résultat ,*arg = x(v) 
            if arg:
                print("résultat de fonction non attendu -> ",arg)
        
        #formatage
        if not valeur or not résultat and résultat != 0:
            # si les variable sont magiquement vide
            raise RuntimeError(type(valeur),valeur,type(résultat),résultat)
        Srésultat , Svaleur = str(résultat if not isinstance(résultat,list) else "".join([str(x) for x in résultat])) , str(valeur if not isinstance(valeur,list) else "".join([str(x) for x in valeur]))

        key = str(x.__name__).replace("_"," ") + " "+str(Svaleur) # question

        if typ == 1:
            ret[key] = { "type" :1 ,
                        "reponse" :  ([Srésultat] + [ran(résultat)] # mode 2 réponse
                                if i == 0 else [ran(résultat)] + [Srésultat] #mode 2 réponse
                                ) if Lans else ( #mode 4 réponse
                                    [Srésultat] + [ran(résultat),ran(résultat),ran(résultat)] if i == 0 else
                                    [ran(résultat)] + [Srésultat] + [ran(résultat),ran(résultat)] if i == 1 else 
                                    [ran(résultat),ran(résultat)] + [Srésultat] + [ran(résultat)] if i == 2 else
                                    [ran(résultat),ran(résultat),ran(résultat)] + [Srésultat]
                                )
                        ,"correct" : i
                        }
        else:
            ret[key] = {"type":0
                        ,"reponse":[Srésultat]
                        ,"correct":0
                        }
    return ret

def passer(quest : dict):
    score = [] # est une list pour peu de réson 
    f = list(quest.items())
    random.shuffle(f)
    print("L : question libre , S : question à réponse seul , M : question a réponse multiple ';' est utiliser pour séparer les choix\n\tveuillez donné les réponse dans l'autre donné")
    for question , dic in f:
        if dic["type"] == -1:
            print(question)
        elif dic["type"] == 0:
            #question libre
            if input(question+" L : ? ") in dic["reponse"]:
                score.append(1)
        elif dic["type"] == 1:
            #réponse seul
            if input(question+" S : "+
            "".join([x+" ," if index != len(dic["reponse"])-1 else x for index , x in enumerate(dic["reponse"])])
            +" ? ") == dic["reponse"][dic["correct"]]:
                score.append(1)
        elif dic["type"] == 2:
            # reponse multiple dic["correct"] est une list de possibiliter de combinaison de réponse
            if [x.strip() for x in input(question+" M : "+
            "".join([x+" ," if index != len(dic["reponse"])-1 else x for index , x in enumerate(dic["reponse"])])+" ? ").split(";")] in [[dic["reponse"][y] for y in x] for x in dic["correct"]]:
                score.append(1)
        else:
            print(question , " n'a pas de type reconnu " , dic)
    print("\n\tvotre score est : ",str(len(score)))

"""
#le format du questionnaire est un simple dictionnaire
#format : dict[str,dict[str,typing.Union[int,list[typing.Union[str,tuple[int]]]]]]
print("démo")
passer(
{
    "question" : 
    {
        "type": 0 # libre , 1 radio , 2 multiple
        ,"reponse" : [str]
        ,"correct" : 0
        #le 'correct' fait référence a l'index de 'reponse' 
    },

    #exemple type 0
    "quel est le chiffre entre 1 et 3":
    {
        "type": 0 #libre
        ,"reponse": ["2"]
        ,"correct":0
    },
    
    #affichage
    #quel est le chiffre entre 1 et 3 L : ? -> 2

    #type 1
    "quel est le chiffre entre 1 et 3":
    {
        "type": 1 #réponse seul
        ,"reponse": ["2","7"]
        ,"correct":0
    },
    #affichage
    #quel est le chiffre entre 1 et 3 S : 2 ,7 ? -> 2

    #exemple type 3 réponse multiple
    #NOTE: correct est une list de tuple de int pour les questionnaire de type 2
    "êtes vous sur de vos réponse" :
    {
        "type": 2 #réponse multiple 1
        ,"reponse": ["oui","non","peut-être"]
        ,"correct":[(0),(0,2),(2)]
    }
    #affichage
    #êtes vous sur de vos réponse M : oui ,non ,peut-être ?
    #les réponse possible sont ->
    #oui
    #oui ; peut-être
    #peut-être

    #le type 2 ne peut pas être générer aléatoirement par le générateur et donc doit être fait manuellement

})
"""

if __name__ == "__main__":
    #affiche toute les conversion trouver dans le fichier de conversion '__' est utiliser pour masquer les choses qui ne peuvent pas être utiliser
    print("conversion possible", "".join([str(x).replace("_"," ")+" , " for x in dir(malicious) if '__' not in x]))
    #il est possible car c'est la console de commande de spécifier des fichier en argument
    if len(sys.argv) == 2:
        if input("input or output file ? ") == "output":
            #le fichier d'argument de la ligne de commende est pour exporter
            #NOTE: les éléves ne sont pas senser crée des test donc on ne vérifie pas que le nombre de question voulue soit un nombre 
            nq = int(input("nombre de question ? "))
            json.dump(gen(nq),open(sys.argv[1],"w"))
        else:
            #le fichier  de la ligne de commande est un test (sauvegarder au format json) à importer
            passer(js(sys.argv[1]))
    else:
        #aucun argument n'est passer par l'inviter de commande donc on va faire un test aléatoire
        x = True
        while x:
            try:
                #on vérifie que l'input soit bien un nombre
                nq = input("combien de question voulez vous ? ")
                nq = int(nq)
            except Exception:
                #pas besoin de faire d'exception on peut reposer la question en boucle
                pass
            else:
                x = False
        #on passe le test avec le nombre de question selectionner
        passer(gen(nq))