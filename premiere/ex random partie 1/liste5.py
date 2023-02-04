# Créé par arthur.pavard, le 20/09/2021 en Python 3.7
"""
Créer une fonction count_car(ch,c) qui retourne le nombre d’apparitions du caractère c dans la chaîne ch.
Créer une fonction Dictionnaire_frequence(chaine) qui retourne le dictionnaire des fréquences d’une chaine
Créer une fonction affichage_frequence(chaine) qui afficher le dictionnaire par ordre croissant de fréquences
"""

def count_char(ch: str,c : str) -> int:
    return len(ch) - len(ch.replace(c,""))

def Dictionnaire_frequence(chaine: str) -> dict:
    dic = {}
    for ch in chaine:
        dic[ch] = count_char(chaine,ch)
    return dic

def affichage_frequence(chaine : str) -> None:
    dic = Dictionnaire_frequence(chaine)
    keys = dict(sorted(dic.items(),key= lambda x:x[1],reverse = True))
    for x in keys:
        print(x,dic[x])

affichage_frequence(input("truc : "))


