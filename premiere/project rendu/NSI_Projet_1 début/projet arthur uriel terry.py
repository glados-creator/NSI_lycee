import json
from os import listdir

def ecriture(identiter,number):
    if len(number) < 2 or len(number) > 15:
        raise RuntimeError("incorrect numéro")
    # remplace la notation / le préfixe +33 par un 0
    number.replace("+33","0")
    try:
        # vérifie que le numéro est un nombre
        int(number)
    except Exception:
        raise ReferenceError("numéro non conventionelle")
    else:
        #si il n'y a pas d'erreur importer le dictionnaire
        dic = json.load(open("numbers.json","r"))
        # entrée la valeur
        dic[identiter] = number
    with open("numbers.json","w") as f:
        # récrire le dictionnaire
        f.write(json.dumps(dic))



def recherche(attemp):
    data = json.load(open("numbers.json","r"))
    for thing in data.items():
        # test pour le numéro
        if attemp == thing[1]:
            return thing[0] , attemp
        # test pour le nom
        elif attemp == thing[0]:
            return attemp , thing[1]
    # on ne trouve pas l'attemp
    raise RuntimeError("non trouvé")

def remove(attemp):
    data = json.load(open("numbers.json","r"))
    per = recherche(attemp=attemp)
    with open("numbers.json","w") as f:
        data.__delitem__(per[0])
        f.write(json.dumps(data)) 


def menu():
    while True:
        #menu
        entrer = input("\n\t0-quitter\n\t1-écrire dans le répertoire\t(1)\n\t2-écrire dans le répertoire\t(pls)\n\t3-recherche dans le répertoire\n\t4-aficher tout le répertoire\n\t5-supprimer une entrée\n\t6-supprimer tout le répertoire\nvotre choix ? : \n")
        try:
            entrer = int(entrer)
            if entrer == 0:
                return 0
            elif entrer == 1:
                ecriture(input("nom : "),input("\nTéléphone : "))
            elif entrer == 2:
                inp = -1
                while not inp == "0":
                    inp = input("nom\t(0 pour quiter)\t: ")
                    if not inp == "0":
                        ecriture(inp,input("numéro : "))
            elif entrer == 3:
                nom , num =recherche(input("numéro ou nom : "))
                print("nom : ",nom,",\tnuméro : ",num)
            elif entrer == 4:
                for x in json.load(open("numbers.json","r")).items():
                    name , num = recherche(x[0]) 
                    print("nom : ",name," numéro : ",num)
            elif entrer == 5:
                remove(input("numéro ou nom a supprimer : "))
            elif entrer == 6:
                with open("numbers.json","w") as f:
                    f.write("{}")
            else:
                raise RuntimeError("valeur non accepter")

        except Exception as ex:
            print(ex)

#regarde si il y a le fichier number.json et si il n'y ai pas cela crée le fichier
if not 'numbers.json' in listdir():
    with open("numbers.json","w") as f:
        f.write(json.dumps({})) 

if __name__ == '__main__':
    menu()