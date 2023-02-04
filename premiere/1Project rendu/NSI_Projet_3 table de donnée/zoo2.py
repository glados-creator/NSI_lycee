zoo = [{'espèce': 'Lion', 'nom': 'Simba', 'classe': 'mammifère'},
       {'espèce': 'Kangourou', 'nom': 'Jumper', 'classe': 'mammifère'},
       {'espèce': 'Panda', 'nom': 'Pandi', 'classe': 'mammifère'},
       {'espèce': 'Raie', 'nom': 'Nicola', 'classe': 'poisson'},
       {'espèce': 'Gorille', 'nom': 'Kong', 'classe': 'mammifère'},
       {'espèce': 'Girafe', 'nom': 'Coucou', 'classe': 'mammifère'},
       {'espèce': 'Requin', 'nom': 'Marteau', 'classe': 'poisson'},
       {'espèce': 'Perroquet', 'nom': 'Blu', 'classe': 'oiseau'},
       {'espèce': 'Girafe', 'nom': 'Neck', 'classe': 'mammifère'},
       {'espèce': 'Autruche', 'nom': 'Speedy', 'classe': 'oiseau'},
       {'espèce': 'Panda', 'nom': 'Glass', 'classe': 'mammifère'},
       {'espèce': 'Lézard', 'nom': 'Curieux', 'classe': 'reptile'},
       {'espèce': 'Crapaud', 'nom': 'Prince', 'classe': 'amphibien'}
       ]

# Une fonction qui peut servir ...
def affiche(table):
    """Fonction qui affiche les éléments d'une table, un élément par ligne,
    quelle que soit le type de cet élément"""
    for element in table:
        print(element)
    print()    #nouvelle ligne


# V) a) Importation de la table (dictionnaires) et affectation d'une variable
# Avec csv.reader(), on saute la ligne d'entête, et on définit manuellement les clés

import csv

def csv_read(name):
    """Fonction qui importe un fichier csv sous la forme d'une liste de
    dictionnaires en sautant la ligne d'entêtes"""
    ret = []
    with open(name, 'r', newline='') as f:
        table = csv.reader(f, delimiter=';')
        table.__next__()
        for row in table:
            ret.append({'nom': row[0], 'lieu' : row[1], 'heure' : row[2], 'repas' : row[3], 'comportement' : row[4]}) #Ajoute chaque elements
    return ret
    

gestion1 = csv_read("gestion.csv")
affiche(gestion1)


# V) b) Importation de la table (dictionnaires) et affectation d'une variable
# Avec csv.DictReader(), on utilise la ligne d'entête comme clés

def csv_dict(name):
    """Fonction qui importe un fichier csv sous la forme d'une liste de
    dictionnaires en utilisant la ligne d'entêtes comme clés"""
    ret = []
    with open(name, 'r', newline='') as f:
        table = csv.DictReader(f, delimiter=';')
        for row in table:
            ret.append(row)
    return ret

gestion2 = csv_dict("gestion.csv")
assert gestion1 == gestion2
affiche(gestion2)


# VI) Fusion des deux tables

def fusion_tables(tb1,tb2):
    """Fonction qui combine les deux tables en ne gardant que les champs
    'nom', 'espèce', 'lieu' et 'comportement'"""
    ret = []
    for a1 in tb1: 
        for a2 in tb2:  # pour chaqu'un des éléments dans les deux tables
            if a1["nom"] == a2["nom"]: #si nom est egal a nom
                ret.append({"nom": a1['nom'], "espèce": a1['espèce'], "lieu": a2['lieu'], "comportement": a2['comportement']}) #ajout des element de chaque table avec leur clés
                # on pourrai faire un fonction plus complète qui copie tout les attribut et check ceux qui sont en commun 
                # break si il n'y a pas de doublons
    return ret
    
fusion = fusion_tables(zoo,gestion2)
affiche(fusion)


# VII) Filtre d'une table suivant une valeur de champ

def filtre_table(table):
    """Fonction qui renvoir une table avec seulement les animaux n'ayant
    pas un comportement normal"""
    return [x for x in table if x['comportement'] != 'normal']


problemes = filtre_table(fusion)
affiche(problemes)
