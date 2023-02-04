

import csv


#################################
####  PARTIE 1
#################################


#################################
### Exercice 1
#################################


### On va chercher les données dans le fichier csv

def import_csv(fichier="adherents.csv"):
    """
        Fonction qui ouvre le fichier csv dont le nom est fichier
        renvoie une table bi-dimensionnelle
        table[0] contient les titres des colonnes
        Les données numériques ('Numéro rue' et 'Code postal') doivent être des entiers;
        La cotisation (payée ou pas payée) doit être un booléen;
        Les numéros de téléphone sont complétés en chaîne de 10 caractères.
    """
    with open(fichier,"r", newline="", encoding="utf-8") as adherents:
        table = adherents.read()
    table = table.split("\n")[:-1]
    for k in range(len(table)):
        table[k] = table[k].split(",")
        if k>0:
            table[k][2] = int(table[k][2])
            table[k][5] = int(table[k][5])
            table[k][9] = "{:0>10}".format(table[k][9])
            table[k][10] = "{:0>10}".format(table[k][10])
            if table[k][11] == "oui":
                table[k][11] = True
            else:
                table[k][11] = False
    return table

table = import_csv()
#print(table)


#################################
### Exercice 2
#################################


### On cherche les membres qui ne sont pas à jour de leur cotisation

def cotisation_pasajour(donnees):
    """
        Fonction qui cherche les membres dont la cotisation n'est pas à jour
        renvoie une liste des noms et prénoms ces membres sous forme d'un tuple :
        [(nom, prenom)].
    """
    rep = []
    for element in donnees:

        # À COMPLÉTER
        if not element[11]:
            rep.append(element)
    return rep

#print(x[0],x[1] for x in cotisation_pasajour(table))

#################################
### Exercice 3
#################################


### On veut créer un nouveau fichier dans lequel les membres sont triés par ancienneté


def export_csv(donnees,fichier="export.csv"):
    """
        Fonction qui enregistre la liste dans le fichier csv dont le nom est fichier
        liste[0] contient les titres des colonnes
    """
    table = "Nom,Prénom,Numéro rue,Rue,Complément,Code postal,Ville,mail personnel,mail professionnel,téléphone personnel,téléphone portable,cotisation,date d’adhésion,statut\n"
    for k in range(1,len(donnees)):
        ligne = ""
        """for i in range(9):
            ligne = ligne + str(donnees[k][i]) + ','"""
        for i in range(9): # 0 - 8
            ligne = ligne + str(donnees[k][i]) + "," 
        if donnees[k][9]=='0000000000':
            ligne = ligne + ","
        else:
            ligne = ligne + donnees[k][9] + ','
        ligne = ligne + str(donnees[k][10]) + ","
        if donnees[k][11]:
            ligne = ligne + 'oui,'
        else:
            ligne = ligne + 'non,'
        ligne = ligne + str(donnees[k][12]) + ","
        ligne = ligne + str(donnees[k][13]) + "\n"
        table = table + ligne
    with open(fichier,"w", newline="", encoding="utf-8") as adherents:
        adherents.write(table)


def anciennete(donnees):
    """
        Fonction qui tri la liste suivant le critère d'ancienneté
        Sauvegarde le résultat dans un fichier csv en utilisant la fonction export_csv
        ancien et actuel sont les variables qui stockent les dates d'adhésion
        de deux membres (i et k dans la liste)
        au format [jour, mois, année] "jour", "mois" et "année" sont des entiers.
    """

    nb_adh = len(donnees)
    for i in range(1,nb_adh):
        position = i
        if donnees[i][12]!='':
            ancien = list(map(int, donnees[i][12].split('/') ))
            for k in range(i+1,nb_adh):
                if donnees[k][12]!='':
                    actuel = list(map(int,donnees[k][12].split('/')))
                    if ancien[2]*365.25 + ancien[1]*31+ancien[0] > actuel[2]*365.25 + actuel[1]*31+actuel[0]:
                        position = k
                        ancien = actuel
            donnees[i], donnees[position] = donnees[position],donnees[i]
    return donnees


#################################
### Exercice 4
#################################


### On veut créer un nouveau fichier dans lequel les membres sont triés par liste alphabétique


def alphabetique(donnees):
    """
        Fonction qui trie la liste suivant le critère nom, prénom
        Sauvegarde le résultat dans un fichier csv en utilisant la fonction export_csv
    """
    #print(donnees)
    #print([x for x in sorted(donnees,key=lambda x: x[0].lower())]) 
    return [x for x in sorted(donnees,key=lambda x: x[0].lower())]
    """for i in range(# À COMPLÉTER
):
        position = i
        for k in range(# À COMPLÉTER
):
            if []:# À COMPLÉTER

                position = k
                donnees[i], donnees[position] = donnees[position], donnees[i]"""

#export_csv(alphabetique(table))


#################################
####  PARTIE 2
#################################


#################################
### Exercice 5
#################################


### On va chercher les données dans le fichier csv


def import_dico(fichier="adherents.csv"):
    """
        Fonction qui ouvre le fichier csv dont le nom est fichier
        renvoie une liste de dictionnaires dont les clés sont
        les titres des colonnes du fichier csv
    """
    donnees=[{"Nom":[]},{'Prénom':[]},{'Numéro rue':[]},{'Rue':[]}]
    with open(fichier, "r", newline="",encoding="utf-8" ) as adherents:
        # création du lecteur csv utilisant la ligne d'entête comme clés du dictionnaire
        # des enregistrements.
        table=csv.DictReader(adherents,delimiter=",")
        for element in table:
            print(element)
            donnees[element[0]] += element[1]
    return donnees

print(import_dico())

#################################
### Exercice 6
#################################


### On cherche l'adresse mail d'un membre


def adresse_mail(donnees, nom, prenom=''):
    """
        Fonction qui cherche les membres dont les nom et prénom sont
        ceux fournis en argument
        renvoie une liste des adresses mail personnelles des personnes
    """
    # À COMPLÉTER
    return [x[8] for x in [x for x in donnees if x[0] == nom and (x[1] == prenom if prenom else True)]]


#################################
### Exercice 7
#################################


### On cherche un numéro de téléphone, portable de préférence, pour joindre un membre


def telephone(donnees, nom, prenom=''):
    """
        Fonction qui cherche les membres dont les nom et prénom sont
        ceux fournis en argument
        renvoie une liste des telephones, portables de préférence, des personnes
    """
    return [(x[9],x[10]) for x in [x for x in donnees if x[0] == nom and (x[1] == prenom if prenom else True)]]


#################################
### Exercice 8
#################################


### On cherche à trier les communes par nombre d'adhérents


def classement_par_villes(donnees):
    """
        Fonction qui crée une liste des communes dont sont issues les adhérents
        en y adjoignant le nombre d'adhérents correspondants.
        renvoie cette liste triée par ordre décroissant du nombre d'adhérents,
        puis par ordre alphabétique des villes
    """
    return [x for x in sorted(donnees,key=lambda x: x[6])]
