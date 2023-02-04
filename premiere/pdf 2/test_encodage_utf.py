# coding utf-8

import csv

def charger_fichier(nom_fic):
    '''fonction prenant un fichier csv (nom_fic)
       et le sortant sous forme d'une liste de dictionnaire (sortie)'''
    sortie=[]
    with open(nom_fic,'r',newline='',encoding='iso-8859-1') as csvfile:  #Régler le paramètre 'encoding' sur différentes valeurs pour tester la sortie
        ligne=csv.DictReader(csvfile,delimiter=",")
        for test in ligne:
            sortie.append(dict(test))
    return sortie
tableau=charger_fichier("tableau_encodage_utf.csv")
for i in range(len(tableau)):
    print(tableau[i])
