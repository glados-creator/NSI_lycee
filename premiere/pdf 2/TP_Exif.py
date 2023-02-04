from exif import Image
import os

chemin = 'photos/'  # Variable modifiable pour gagner du temps lors de la saisie du chemin

def exif_load(chemin,nom_fichier):
    """Ouvre une image et construit une liste contenant les clés
    Le fichier image nom_fichier est sans extension sous Unix, avec sous Windows, il se trouve dans le répertoire "chemin"
    myexif est l'objet exif qui contient les informations exif du fichier image

    Remarque : la sortie myimage n'est pas exactement un dictionnaire, cependant la syntaxe est assez proche, pour accéder à une clé par exemple, il suffit d'écrire myimage["ma_cle"] ou myimage.ma_cle"""
    nom_fichier=chemin+nom_fichier
    print(nom_fichier)
    with open(nom_fichier, 'rb') as image_file:
            myexif= Image(image_file)
    return myexif

def exif_dictionnaire(exif_obj):
    """ Convertit un objet exif en un dictionnaire
        la variable de sortie : dico
        Remarque : l'objet exif contient des tags, qui ne peuvent pas être convertis en clé. Dans ce cas les tags sont ignorés."""

    dico={}
    for k in dir(exif_obj):
        try:
            dico[k]=exif_obj[k]
        except:
            None

    return dico

def ecriture(chemin,nom_fichier,exif_obj):
    """ Cette fonction permet d'écrire une donnée exif contenue dans une variable dans une photo existante.
    exif est l'objet exif (créé par la fonction exif_load)
    nom_fichier : est le nom du fichier image dans laquel on dépose les données exif contenues dans la variable exif.
    chemin : le chemin dans lequel on va trouver le fichier"""

    os.chdir(chemin) # répertoire de travail est maintenant chemin
    with open(nom_fichier, 'wb') as  new_image_file:
            new_image_file.write(exif_obj.get_file())
    os.chdir('..')   # on quitte le répertoire de travail pour remonter au répertoire parent de chemin

def nombre_de_fichiers(chemin):
    """Comptabilise le nombre de fichiers dans le répertoire "chemin" et retourne cette valeur"""
    for root, _, files in os.walk(chemin):
	    nombre_de_fichiers=len(files)
    return nombre_de_fichiers



