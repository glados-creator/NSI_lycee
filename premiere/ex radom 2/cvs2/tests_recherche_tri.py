#!/usr/bin/env python
# -*- coding: UTF-8 -*-


#################################

from recherche_tri import *


#################################
####  PARTIE 1
#################################


#################################
### Exercice 1
#################################


liste = import_csv("adherents.csv")
assert liste[1][2]==14, "Problème de type avec numéro de rue"
assert liste[3][5]==45460, "Problème de type avec Code postal"
assert liste[15][11], "Problème de type sur la cotisation"


#################################
### Exercice 2
#################################


cotis_absente = cotisation_pasajour(liste)
cotis_absente = [(x[0],x[1]) for x in cotis_absente]
assert ('FOURNIER', 'Virginie') in cotis_absente, "Devrait être dans la liste"
assert not ('PAILLART', 'Mélanie') in cotis_absente, "Ne devrait pas être dans la loste"
assert len(cotis_absente)==7, "Il en manque"


#################################
### Exercice 3
#################################


anciennete(liste)
export_csv(liste)#optionel ,"adherents_anciens.csv")
assert liste[0][0]=='Nom', "Problème ligne des titres"
assert liste[1][0]=='PAILLART'
assert liste[5][0]=='BOUGEOT'
assert liste[6][0]=='MERCIER' and liste[7][0]=='SICARD'


#################################
### Exercice 4
#################################


alphabetique(liste)
export_csv("alphabetique.csv", liste)
assert liste[0][1]=='Prénom', "Problème ligne des titres"
assert liste[1][0]=='ASSELIN'
assert liste[22][0]=='PINOTEAU' and liste[22][1]=='Andrée'


#################################
####  PARTIE 2
#################################


#################################
### Exercice 5
#################################


dico = import_dico("adherents.csv")
assert "mail professionnel" in dico[0].keys()
assert dico[0]["Nom"]=="ASSELIN"
assert dico[0]['adresse']["Numéro rue"]==14, "Problème de type avec numéro de rue"
assert dico[2]['adresse']["Code postal"]==45460, "Problème de type avec Code postal"
assert dico[5]["téléphone personnel"]=="0225984127", "Problème de format téléphone perso sur 10 chiffres"
assert dico[6]["téléphone portable"]=="0689125632", "Problème de format téléphone perso sur 10 chiffres"
assert dico[14]["cotisation"], "Problème de type sur la cotisation"
assert len(dico)==35, "Problème nombre d'adhérents"


#################################
### Exercice 6
#################################


assert adresse_mail(dico, "ASSELIN", "Francis") == ["ass4@gmail.com"]
mail_vannier = adresse_mail(dico, "VANNIER", "Anne")
mail_vannier.sort()
assert mail_vannier == ["vannier_2@orange.fr","vannier_4@red.fr"]


#################################
### Exercice 7
#################################


assert telephone(dico, "ASSELIN", "Francis") == ["0689154763"]
assert telephone(dico, "LELAY", "Romuald") == ["0238963791"]
tel_vannier = telephone(dico, "VANNIER", "Anne")
tel_vannier.sort()
assert tel_vannier == ["0203690452","0713791685"]


#################################
### Exercice 8
#################################


villes = classement_par_villes(dico)
assert(villes[0] == ('Bellegarde',8))
assert(villes[2][0] == 'Bonny sur Loire')
assert(villes[4][1] == 3)
