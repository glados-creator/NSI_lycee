"""
import pandas
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
#traitement CSV
iris=pandas.read_csv("iris.csv")
x=iris.loc[:,"petal_length"]
y=iris.loc[:,"petal_width"]
lab=iris.loc[:,"species"]
#fin traitement CSV
#valeurs
longueur=4.8
largeur=1.7
k=5
#fin valeurs
#graphique
plt.scatter(x[lab == 0], y[lab == 0], color='g', label='setosa')
plt.scatter(x[lab == 1], y[lab == 1], color='r', label='virginica')
plt.scatter(x[lab == 2], y[lab == 2], color='b', label='versicolor')
plt.scatter(longueur, largeur, color='k')
plt.legend()
#fin graphique
#algo knn
d=list(zip(x,y))


model = KNeighborsClassifier(n_neighbors=k)
model.fit(d,lab)
prediction= model.predict([[longueur,largeur]])
#fin algo knn
#Affichage résultats
txt="Résultat : "
if prediction[0]==0:
 txt=txt+"setosa"
if prediction[0]==1:
 txt=txt+"virginica"
if prediction[0]==2:
 txt=txt+"versicolor"
plt.text(3,0.5, "largeur : {} cm, longueur : {} cm".format(largeur, longueur), fontsize=12)
plt.text(3,0.3, "k : {}".format(k), fontsize=12)
plt.text(3,0.1, txt, fontsize=12)
#fin affichage résultats
plt.show()
"""



# Import des bibliothèques nécessaires
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from random import randint
from math import sqrt
import hashlib
import sys

# Constantes
MAX_RANGE = 100 # les coordonnées sont entre 0 et 99
FORMES = {"red":"o", "blue":"^", "green":"s", "black":"x"}
COULEURS = {'red':(255,0,0), 'green':(0,255,0), 'blue':(0,0,255), 'black':(0,0,0)}

# Récupération d'un jeu existant
def nb_data(data):
 """Renvoie le nombre de points total dans le jeu de données"""
 return sum([len(data[propriete]) for propriete in data.keys()])

data = {
'black': [(52, 2), (59, 0), (68, 8), (77, 11), (28, 21)],
'blue': [(0, 66), (0, 77), (28, 61), (21, 56), (29, 66),(10, 40),(10, 81),(30, 49)],
'green': [(83, 87), (96, 56), (45, 77), (73, 69), (53, 77), (34, 68), (70, 63)],
'red': [(85, 34), (36, 54), (33, 54), (65, 52), (45, 45), (70, 62), (48, 66), (63, 28), (40, 28),(82, 18)]
 }
print("ce jeu contient ", nb_data(data), " données")
#print("les points noirs sont ", data["black"])
# Fonction pour faire afficher les points, et le point testé (origine)
def dessine_points(data,origine):
    
    plt.rcParams["figure.figsize"] = (4, 4)
    plt.axis('equal')
    for couleur in data.keys():
        x=[e[0] for e in data[couleur]]
        y=[e[1] for e in data[couleur]]
        plt.scatter(x, y, c=couleur, marker=FORMES[couleur])
    # Dessin du point origine (point testé) en orange.
    plt.scatter(origine[0], origine[1], c="orange", marker="*")
    plt.show()

### BEGIN SOLUTION
def distance(pointA, pointB,color=None):
    xA, yA = pointA
    xb , yb = pointB
    if color:
        print("color :",color,"p1",pointA,"p2",pointB,"distance",sqrt((xb-xA)**2+(yb-yA)**2))
    return sqrt((xb-xA)**2+(yb-yA)**2)
### END SOLUTION

### BEGIN SOLUTION
def k_proches_voisins(data, origine, k=1,all=False):

    reponse=[]
    for propriete in data.keys():
        for voisin in data[propriete]:
            d = distance(origine, voisin)
            # Insertion dans la liste des k plus proches voisins
            i=0
            
            while len(reponse)-1 > i and reponse[i][0] < d:
                # print(reponse,i,reponse[i][0])
                i += 1
            reponse.insert(i,(d,propriete))
    
    return reponse if all else reponse[:k]
### END SOLUTION

### BEGIN SOLUTION
def categorie_devine(data, origine, k=1):
    liste_cles = list(data.keys())
    tri = [[0,0,p] for p in liste_cles]

    kpv = k_proches_voisins(data, origine, k)
    print(kpv)
    
    for d,p in kpv:
        for x in tri:
            if x[2] == p:
                x[0] -= d

    print(tri)
    
    return min(tri)[2]
### END SOLUTION

origine = (40,60)
reponse = categorie_devine(data, origine, 5)
plt.text(origine[0],origine[1]+2,reponse)

dessine_points(data, origine)
