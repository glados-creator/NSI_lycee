"""
# import dataclasses
# @dataclasses.dataclass
# class Eleve:
#     nom : str
#     prenom : str
#     date : str
#     note_mat1 : float
#     note_mat2 : float
#     note_mat3 : float
"""


class Eleve:
    '''
    Création d'une instance eleve:
    eleve=Eleve(nom(str),prenom(str),date(str),note1(programm)(float)
    note2(algo)(float),note3(projet(float)))
    attributs d'instance : nom,prenom,date,note_mat1,note_mat2,note_mat3
    attributs de classe: matiere1,matiere2,matiere3
    Méthode : moyenne() retourne la moyenne de l'élève
    '''
    # attributs de classe
    matiere1 = "Programmation"
    matiere2 = "Algorithmique"
    matiere3 = "Projet"
    # constructeur (attention deux underscores de chaque côté !!)

    def __init__(self, Nom, Prenom, Date, Note1, Note2, Note3):
        # attributs d’instance
        self.nom = Nom
        self.prenom = Prenom
        self.date = Date
        self.note_mat1 = Note1
        self.note_mat2 = Note2
        self.note_mat3 = Note3
    
    def moyenne(self):
        return ((self.note_mat1+self.note_mat2+self.note_mat3)/3)

# création d’un élève
eleve1 = Eleve("Térieur", "Alain", "01/01/2000", 12, 10, 15)

# Affichage des propriétées
print(eleve1.prenom, eleve1.nom)
print(eleve1.matiere1, ":", eleve1.note_mat1)
print(eleve1.matiere2, ":", eleve1.note_mat2)
print(eleve1.matiere3, ":", eleve1.note_mat3)
print()

"""
# Q1.
# Question 1 :
# Quel est l’affichage obtenu ?

# Résultats
# Alain Térieur
# Programmation : 12
# Algorithmique : 10
# Projet : 15
"""


"""
# Q2.
# À faire 1 :
# Ajouter cette méthode et faire afficher la moyenne de l’élève.
# Ajouter ces deux élèves et faire afficher leurs résultats et leurs moyennes.
"""

eleve2 = Eleve("Onette", "Camille", "01/07/2004", 7, 14, 11)
eleve3 = Eleve("Oma", "Modeste", "01/11/2002", 13, 8, 17)

print("Q2.\n")
print(eleve2.prenom, eleve2.nom)
print(Eleve.matiere1, ":", eleve2.note_mat1)
print(Eleve.matiere2, ":", eleve2.note_mat2)
print(Eleve.matiere3, ":", eleve2.note_mat3)
print("moyenne eleve2 : ",eleve2.moyenne())
print()
print(eleve3.prenom, eleve3.nom)
print(Eleve.matiere1, ":", eleve3.note_mat1)
print(Eleve.matiere2, ":", eleve3.note_mat2)
print(Eleve.matiere3, ":", eleve3.note_mat3)
print("moyenne eleve3 : ",eleve3.moyenne())
print()

"""
# Q2.
# Résultats
# Camille Onette
# Programmation : 7
# Algorithmique : 14
# Projet : 11
# 
# Modeste Oma
# Programmation : 13
# Algorithmique : 8
# Projet : 17
"""

"""
class Eleves:
    # add print methode to class
    def print(self):
        print(self.prenom, self.nom)
        print(self.matiere1, ":", self.note_mat1)
        print(self.matiere2, ":", self.note_mat2)
        print(self.matiere3, ":", self.note_mat3)
"""

"""
# Q3.
# Écrire une fonction (hors de la classe bien sûr) qui prend en paramètre une liste constituée de ces trois élèves et qui
# retourne les moyennes par matières.
"""

def moyenne(*L):
    """
    L : list[Eleves]
    pour chaque eleve prendre ses notes les mettres dans la liste qui lui coorespond
    et faire la moyenne de classe
    """
    nom = []
    prenom = []
    date = []
    note_mat1 = []
    note_mat2 = []
    note_mat3 = []
    moyennes = []
    for e in L:
        # pour chaque eleve
        nom.append(e.nom)
        prenom.append(e.prenom)
        date.append(e.date)
        note_mat1.append(e.note_mat1)
        note_mat2.append(e.note_mat2)
        note_mat3.append(e.note_mat3)
        moyennes.append(e.moyenne())
    Mnote_mat1 = sum(note_mat1)
    Mnote_mat1 = Mnote_mat1/len(note_mat1)
    Mnote_mat2 = sum(note_mat2)
    Mnote_mat2 = Mnote_mat2/len(note_mat2)
    Mnote_mat3 = sum(note_mat3)
    Mnote_mat3 = Mnote_mat3/len(note_mat3)
    Mmoyennes =  sum(moyennes)
    Mmoyennes = Mmoyennes/len( moyennes)
    # pretty print
    # print(
    #     "Q3."
    #     "\néleves : \n", str([e.nom+"."+e.prenom for e in L])[1:-2],
    #     "\n\tMoyenne de ",Eleve.matiere1 ,":" , Mnote_mat1,
    #     "\n\tMoyenne de ",Eleve.matiere2 ,":" , Mnote_mat2,
    #     "\n\tMoyenne de ",Eleve.matiere3 ,":" , Mnote_mat3,
    #     "\n\tMoyenne de général : " , Mmoyennes
    # )
    return {Eleve.matiere1 : Mnote_mat1,Eleve.matiere2 : Mnote_mat2,Eleve.matiere3 : Mnote_mat3}

print(moyenne(eleve1,eleve2,eleve3))

"""
# Résultats
# Q3.
# éleves :
#  'Térieur.Alain', 'Onette.Camille', 'Oma.Modeste
#         Moyenne de  Programmation : 10.666666666666666
#         Moyenne de  Algorithmique : 10.666666666666666
#         Moyenne de  Projet : 14.333333333333334
#         Moyenne de général :  11.888888888888888
# {'Programmation': 10.666666666666666, 'Algorithmique': 10.666666666666666, 'Projet': 14.333333333333334}
"""

