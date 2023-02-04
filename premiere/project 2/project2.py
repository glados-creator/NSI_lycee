import json, typing, random, time , os
import mal

"""format : dict[str,dict[str,typing.Union[int,list[str]]]] = 
    {
        "question" : {
            "type": 0 # libre , 1 radio , 2 multiple
            ,"reponse" : [str]
            ,"correct" : 0
        }
    }
"""


def js(file: str)-> list:
    return json.load(open("data.json","r")) if os.path.exists("data.json") else 0

def rep(question : str, case: [str,int]) -> int:
    x = True
    while x:
        rep = input(question)
        for x in case:
            if x[0] == rep:
                return rep if x[1] == -1 else x[1]
            elif x[0] == -1:
                return rep if x[1] == -1 else x[1]

def passer(quest):
    score = []
    f = list(quest.items())
    random.shuffle(f)
    print("L : question libre , S : question à réponse seul , M : question a réponse multiple ';' est utiliser pour séparer les choix\n\tveuillez donné les réponse dans l'autre donné")
    for question , dic in f:
        if dic["type"] == 0:
            if input(question+" L : ") in dic["reponse"]:
                score.append(1)
        elif dic["type"] == 1:
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
    print("\nvotre score est : ",str(len(score)))

if __name__ == "__main__":
    passer(
        {
            "randome" : {
                "type" : 0,
                "reponse" : ["1"],
                "correct" : 0
            }
            ,"2eme": {
                "type" : 1,
                "reponse" : ["ok","ok 2"],
                "correct" : 0
            }
            ,"qcm" : {
                "type": 2
                ,"reponse":["oui","oui","non","peut être"]
                ,"correct" : [(0,1),(0,1,3)]
            }
        }
        )