# Créé par arthur.pavard, le 09/09/2021 en Python 3.7
import math
num = 3
try:
    if num == 3:
        x = int(input("prix : x"))
        print(x+0.1*x if input("taux plien ? y/n : ") == "n" else (x+0.2*x))


    if num == 4:
        a = int(input("a : "))
        b = int(input("b : "))
        c = int(input("c : "))
        delt = b**2 - 4*a*c
        print("discrimiant : ",delt)
        print("pas de solution" if delt < 0 else -b/(2*a) if delt == 0 else ('deux racine : ' , (-b + math.sqrt(delt))/2*a ,(-b - math.sqrt(delt))/2*a ))


    #ex 9
    if num == 9:
        x = int(input("température de l'eau : "))
        if x <= 0:
            print("l'eau est sous forme solid")
        elif x >= 100:
            print("l'eau se transforme en nuage")
        else:
            print("l'eau est liquide")

    #ex 8 et 10
    elif num == 10:

        moyenne = float(input("Entrez votre moyenne au bac : "))

        if moyenne < 8:
            print("Vous êtes éliminé ! Au revoir...")
        if 8 <= moyenne < 10:
            print("Vous pouvez aller à l'oral : bonne chance!")
        if moyenne >= 10:
            print("Bravo, vous avez le bac!")

        if 12 <= moyenne < 14:
            mention = "assez bien"
        if 14 <= moyenne < 16:
            mention = "bien"
        if moyenne > 16 :
            mention = " trés bien"

        print("mention : ",mention)
except Exception as ex:
    print("error occur " , ex)

