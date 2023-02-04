# coding: utf-8

import json
def charger_data(nom_fichier):
    # Retourne un tableau de dictionnaire correspondant au fichier json passé en paramètre
    with open(nom_fichier) as data:
        data_dict = json.load(data)
    return data_dict

employes : list=(charger_data('liste_employes.json'))

print(employes[1])

#Partie I)

print('la liste des clés est :', employes[0].keys())

print('le nombre des clés est :', len(employes[0].keys()))

print("len emp",len(employes))


suspects=[(x["nom"],x["pointure"]) for x in employes if x["sexe"] == "femme" and x["sang"] == "A" and x["cheveux"] == "blond"]

print("suspects ",(suspects) , len(suspects))

"""
print("suspects ",suspects)


print("suspects ",suspects)


# Partie II)

print("suspects ",suspects)


print("suspects_2 ",suspects_2)


print("suspects_3 ",suspects_3)


print("suspects_4 ",suspects_4)


print("suspects_5 ",suspects_5)

"""