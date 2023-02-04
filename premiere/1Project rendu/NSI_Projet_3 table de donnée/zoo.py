# Une fonction qui peut servir ...
def affiche(table):
    """Fonction qui affiche les éléments d'une table, un élément par ligne,
    quelle que soit le type de cet élément"""
    for element in table:
        print(element)
    print()    # \n

# I) a) Importation de la table et affichage
# écrire le code donné dans l'énoncé

import csv
with open('zoo.csv', 'r', newline='') as f:
    table = csv.reader(f, delimiter=';')
    table.__next__()
    for row in table:
        print(' - '.join(row))


# I) b) Importation de la table et affectation d'une variable

def csv_tuple(name):
    """Fonction qui importe un fichier csv sous la forme d'une liste de
    tuples en sautant la ligne d'entêtes"""
    with open(name, 'r', newline='') as f:
        table = csv.reader(f, delimiter=';')
        table.__next__()
        ret = []
        for row in table:
            ret.append(row)
        return [(x[0] , x[1]) for x in ret] # retourne une pair de la list ret type tuple

zoo = csv_tuple('zoo.csv')
assert zoo==[('mammifère', 'Lion'),
             ('mammifère', 'Kangourou'),
             ('mammifère', 'Panda'),
             ('poisson', 'Raie'),
             ('mammifère', 'Gorille'),
             ('mammifère', 'Girafe'),
             ('poisson', 'Requin'),
             ('oiseau', 'Perroquet'),
             ('mammifère', 'Girafe'),
             ('oiseau', 'Autruche'),
             ('mammifère', 'Panda'),
             ('reptile', 'Lézard'),
             ('amphibien', 'Crapaud')
             ]
affiche(zoo)


# II) a) Ajout d'un panda
zoo.append(('mammifère','Panda'))

assert zoo==[('mammifère', 'Lion'),
             ('mammifère', 'Kangourou'),
             ('mammifère', 'Panda'),
             ('poisson', 'Raie'),
             ('mammifère', 'Gorille'),
             ('mammifère', 'Girafe'),
             ('poisson', 'Requin'),
             ('oiseau', 'Perroquet'),
             ('mammifère', 'Girafe'),
             ('oiseau', 'Autruche'),
             ('mammifère', 'Panda'),
             ('reptile', 'Lézard'),
             ('amphibien', 'Crapaud'),
             ('mammifère','Panda')
             ]
affiche(zoo)


# II) b) Détection de doublons

def detecte_doublons(table):
    """Fonction qui renvoie True si au moins un doublon est détecté"""
    for index1 , element in enumerate(table):
        for index2 , el in enumerate(table): # pour chaque éléments de la table avec index
            if index1 != index2 and el == element: # si ce n'est pas la même index (donc litéralement l'élément lui même) et que les éléments sont les même c'est donc un doublon
                return True
    return False

assert detecte_doublons(zoo)
assert not detecte_doublons([('mammifère', 'Lion'),
                               ('poisson', 'Perche'),
                               ('mammifère', 'Panda')
                               ])


# II) c) Suppression de doublons

def supprime_doublons(table):
    """Fonction qui supprime les doublons d'une table"""
    while detecte_doublons(table): # tant que il y a des doublons
        for index1 , element in enumerate(table):
            for index2 , el in enumerate(table): # pour chaqu'un des éléments de la table avec index 
                if index1 != index2 and el == element: # si ce n'est pas le même index et que c'est un doublon
                    table.remove(element) # on supprime

supprime_doublons(zoo)
assert not detecte_doublons(zoo)
affiche(zoo)


# III) a) Importation de la table (listes) et affectation d'une variable

def csv_liste(name):
    """Fonction qui importe un fichier csv sous la forme d'une liste de
    listes en sautant la ligne d'entêtes"""
    with open(name, 'r', newline='') as f:
        table = csv.reader(f, delimiter=';')
        table.__next__()
        ret = []
        for row in table:
            ret.append(list(row))
        return ret

zoo = csv_liste('zoo.csv')
assert zoo==[['mammifère', 'Lion'],
             ['mammifère', 'Kangourou'],
             ['mammifère', 'Panda'],
             ['poisson', 'Raie'],
             ['mammifère', 'Gorille'],
             ['mammifère', 'Girafe'],
             ['poisson', 'Requin'],
             ['oiseau', 'Perroquet'],
             ['mammifère', 'Girafe'],
             ['oiseau', 'Autruche'],
             ['mammifère', 'Panda'],
             ['reptile', 'Lézard'],
             ['amphibien', 'Crapaud']
             ]
affiche(zoo)


# III) b) Nommage des animaux
def inp(txt):
    """Fontion input de base avec try except"""
    while True:
        try:
            i = input(txt)
            if i:
                return i
        except Exception:
            print("une erreur est survenu")

def ajout_nom(table):
    """Fonction qui demande et ajoute un nom à chaque élément de la table"""
    # on est pas sur du type de la table que cela soit tuple (imutable) ou list
    # donc on refait une table de list
    ret = []
    for x in table:
        ret.append(list(x))
    # ajout des noms
    for x in table:
        x.append(inp(f"[{x[0]}] quelle nom pour un {x[1]} ? "))
    return ret

ajout_nom(zoo)
affiche(zoo)


# IV) Tri de la table suivant un champ

def tri_table(table,i):
    """Fonction qui tri la table en fonction du champ d'indice i"""
    return [x for x in sorted(table,key=i)]

#tri par espèce
tri_table(zoo,lambda x:x[0])
affiche(zoo)
