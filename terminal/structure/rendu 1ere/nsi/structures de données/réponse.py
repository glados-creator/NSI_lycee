"""
# II) LA METHODE :
# Le cahier des charges :
# • Stocker les données (nom, prénom, date de naissance, notes) pour les élèves d’une classe.
# • Calculer et stocker leur moyenne.
# • Calculer et stocker la moyenne générale de chaque matière.
#
# Choix de la structure de données :
# • Pour un élève.
# • Pour la classe.
# Implémentation : (ne doit pas modifier le cahier des charges ni le choix de la structure de données).
# • Enregistrement des données.
# • Implémentation des fonctions.
#
# Exercice 1 :
# Implémenter le cahier des charges précédent pour une classe contenant les 3 élèves suivants :
# • Nom : Térieur
# • Prénom : Alain
# • Date : 01/01/2000
# • Programmation : 12
# • Algorithmique : 10
# • Projet : 15
# 
# • Nom : Onette
# • Prénom : Camille
# • Date : 01/07/2004
# • Programmation : 7
# • Algorithmique : 14
# • Projet : 11
#
# • Nom : Oma
# • Prénom : Modeste
# • Date : 01/11/2002
# • Programmation : 13
# • Algorithmique : 8
# • Projet : 17
"""

def moyenne(eleve):
    '''
    eleve : type dict
    clés(type(valeur)) : Nom(str),Prenom(str),date(str),Programmation(float),Algorithmique(float),Projet(float)
    calcule et retourne la moyenne(float) des notes
    '''
    moy=(eleve["Programmation"]+eleve["Algorithmique"]+eleve["Projet"])/3
    for k,v in eleve.items():
        print(k,v)
    return moy
eleve1={"Nom":"Onette","Prenom":"Camille","Date":"01/07/2004","Programmation":7,"Algorithmique":14,"Projet":11}
eleve2={"Nom":"Oma","Prenom":"Modeste","Date":"01/11/2002","Programmation":13,"Algorithmique":8,"Projet":17}
eleve={"Nom":"Térieur","Prenom":"Alain","Date":"01/01/2000","Programmation":12,"Algorithmique":10,"Projet":15}
print("moyenne de ",eleve["Prenom"],eleve["Nom"]," : ",moyenne(eleve))
print()
print("moyenne de ",eleve1["Prenom"],eleve1["Nom"]," : ",moyenne(eleve1))
print()
print("moyenne de ",eleve2["Prenom"],eleve2["Nom"]," : ",moyenne(eleve2))
print("")
print("moyenne de la classe : ",(moyenne(eleve) + moyenne(eleve1) + moyenne(eleve2))/3)
print()


eleves = """
"Nom","Prenom","Date","Programmation","Algorithmique","Projet"
Térieur,Alain,01/01/00,12,10,15
Onette,Camille,01/07/04,7,14,11
Oma,Modeste,01/11/02,13,8,17
"""

"""
# Exercice 2 :
# Avec un éditeur (VS Code, Notepad ou le bloc note...) créer le fichier eleves.csv, puis réaliser un programme qui
# affiche les résultats suivants :
"""

def moyenne1(eleve):
    '''
    eleve : type dict
    clés(type(valeur)) : Nom(str),Prenom(str),date(str),Programmation(float),Algorithmique(float),Projet(float)
    calcule et retourne la moyenne(float) des notes
    '''
    moy=(float(eleve["Programmation"])+float(eleve["Algorithmique"])+float(eleve["Projet"]))/3
    print("moyenne de ",eleve["Prenom"],eleve["Nom"]," : ",moy)

import csv
reader = csv.DictReader(open("eleves.csv","r"))
classe = []
for row in reader:
    classe.append(dict(row))
    moyenne1(dict(row))
print(classe)