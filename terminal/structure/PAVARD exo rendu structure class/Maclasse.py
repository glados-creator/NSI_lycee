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