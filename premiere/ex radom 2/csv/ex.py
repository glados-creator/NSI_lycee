import csv
def charger_csv(nom_fic):
	"""Fonction qui permet d'importer les données du fichier csv sous forme de liste de listes """
	liste = [] # resultat de la fonction
	# ouverture du fichier CSV
	with open(nom_fic, # nom du fichier
	"r", # ouverture en lecture
        newline="", # évite les problèmes de codage du retour à la ligne
        encoding="utf-8-sig" # permet de forcer la lecture en utf-8 (sig pour "UTF-8 codec with BOM signature")
        ) as csvfile: # cvsfile est le fichier que l'on vient d'ouvrir
		# création du lecteur csv indiquant le caractère séparateur
		csv_reader = csv.reader(csvfile, delimiter=";")
		for enreg in csv_reader: # boucle de parcours des enregistrements
		# enreg est une liste de str contenant chaque champ de l ' enregistrement
		# ajout de enreg dans la liste
			liste.append(enreg)
	return liste

def charger_csv_dict(nom_fic):
	"""Fonction qui permet d'importer les données du fichier csv sous forme de liste de dictionnaires """
	liste = [] # resultat de la fonction
	# ouverture du fichier CSV
	with open(nom_fic, # nom du fichier
		"r", # ouverture en lecture
		newline="", # évite les problèmes de codage du retour à la ligne
		encoding="utf-8-sig" # permet de forcer la lecture en utf-8 (sig pour "UTF-8 codec with BOM signature")
		) as csvfile: # cvsfile est le fichier que l'on vient d'ouvrir
		# création du lecteur csv indiquant le caractère séparateur
		csv_reader = csv.reader(csvfile, delimiter=";")
		# permet de sauter la ligne d'entête si pas besoin
		csv_reader.__next__()
		for enreg in csv_reader: # boucle de parcours des enregistrements
			# enreg est une liste de str contenant chaque champ de l ' enregistrement
			# ajout du score dans la liste
			liste.append(
			{
			
				"Fédération" : enreg[0],
				"Discipline" : enreg[1],
				"Epreuve" : enreg[2],
				"NOM" : enreg[3],
				"Prénom" : enreg[4],
				"Sexe" : enreg[5],
				"MEDAILLE(S)": enreg[6],
				"Année" : enreg[7],
				"Olympique/paralympique" : enreg[8]
			}
			)
	return liste

li = charger_csv_dict("JO_Liste_Medaille_2012-2014.csv")

def liste_doublons(liste,t=False):
	"""
	fonction qui prend comme entrée une liste
	et qui renvoie la liste des doublons.
	Cette liste sera vide s’il n'y a aucun doublon.
	"""
	doublons = []
	tract = []
	
	for x in liste:
		if x in tract:
			doublons.append(x)
		else:
			tract.append(x)
	return doublons if not t else tract

def nombre_medailles_fede(federation,liste):
	"""
	Fonction qui en paramètre prend l'intitulé d'une fédération (voir csv)
	et la liste des médailles sous forme de liste de dictionnaires
	et qui retourne le nombre de médailles pour cette fédération
	"""
	# A vous de compléter
	ret = {}
	ret.setdefault(lambda x: x,{})
	for f in federation:
		ret[f] = {"Or":0,"Argent":0,"Bronze":0}
		#ret[f].setdefault(lambda x: x,[])
	
	for x in liste:
		ret[x[0]][x[6]] = ret[x[0]][x[6]] +1 

	return ret

"""fed = []
for x in charger_csv("JO_Liste_Medaille_test_doublons.csv"):
	fed.append(x[0])
fed = liste_doublons(fed,True)
fed.remove(fed[0])
cv = charger_csv("JO_Liste_Medaille_test_doublons.csv")
cv.remove(cv[0])

print(nombre_medailles_fede(fed,cv))

{<function nombre_medailles_fede.<locals>.<lambda> at 0x0000000002A36318>: {}, 
'Athlétisme': {'Or': 1, 'Argent': 1, 'Bronze': 0}, 
'BASKET BALL': {'Or': 0, 'Argent': 14, 'Bronze': 0}, 
'Canoë-Kayak': {'Or': 2, 'Argent': 0, 'Bronze': 0}, 
'Cyclisme': {'Or': 1, 'Argent': 5, 'Bronze': 0}, 
'Gymnastique': {'Or': 0, 'Argent': 0, 'Bronze': 1}, 
'HAND BALL': {'Or': 15, 'Argent': 0, 'Bronze': 0}, 
'Handisport': {'Or': 14, 'Argent': 37, 'Bronze': 32}, 
'Judo-Jujitsu Kendo et Disciplines Associées': {'Or': 2, 'Argent': 0, 'Bronze': 5}, 
'Lutte': {'Or': 0, 'Argent': 0, 'Bronze': 1}, 
'Natation': {'Or': 9, 'Argent': 6, 'Bronze': 6}, 
'Ski': {'Or': 4, 'Argent': 4, 'Bronze': 4}, 
'Ski ': {'Or': 0, 'Argent': 1, 'Bronze': 6}, 
"Sociétés d'Aviron": {'Or': 0, 'Argent': 2, 'Bronze': 0}, 
'Taekwondo et disciplines associées': {'Or':0, 'Argent': 1, 'Bronze': 0}, 
'Taekwondo': {'Or': 0, 'Argent': 0, 'Bronze': 1}, 
'Tennis': {'Or': 0, 'Argent': 2, 'Bronze': 2}, 
'Tir': {'Or': 0, 'Argent': 1, 'Bronze': 1}, 
'Voile': {'Or': 0, 'Argent': 0,'Bronze': 1}
}"""

def nombre_medailles(champ,valeur,liste):
	"""
	Fonction qui en paramètre prend l'intitulé le champ cible (par exemple 'NOM'),
	sa valeur cible (par exemple 'FOURCADE')
	et la liste des médailles sous forme de liste de dictionnaires
	et qui retourne le nombre de médailles correspondant
	"""
	# A vous de compléter
	ret = []
	for x in liste:
		if x[champ] == valeur:
			ret.append(x)
	return ret

print(len( nombre_medailles("MEDAILLE(S)","Or",charger_csv_dict("JO_Liste_Medaille_2012-2014.csv"))))
	