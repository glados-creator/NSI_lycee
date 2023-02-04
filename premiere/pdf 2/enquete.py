# coding: utf-8

import json
def charger_data(nom_fichier):
    # Retourne un tableau de dictionnaire correspondant au fichier json passé en paramètre
    with open(nom_fichier) as data:
        data_dict = json.load(data)
    return data_dict

employes=(charger_data('liste_employes.json'))

# Partie I)

#print('la liste des clés est :', cles)


#print(suspects)


#print(suspects)


#print(suspects)


# Partie II)

#print(suspects)


#print(suspects_2)


#print(suspects_3)


#print(suspects_4)


#print(suspects_5)

