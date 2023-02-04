# ! /usr/bin/python3
import sqlalchemy
import getpass


def ouvrir_connexion(user, passwd, host, database):
    """
    ouverture d'une connexion MySQL
    paramètres:
       user     (str) le login MySQL de l'utilsateur
       passwd   (str) le mot de passe MySQL de l'utilisateur
       host     (str) le nom ou l'adresse IP de la machine hébergeant le serveur MySQL
       database (str) le nom de la base de données à utiliser
    résultat: l'objet qui gère le connection MySQL si tout s'est bien passé
    """
    try:
        #  creation de l'objet gérant les interactions avec le serveur de BD
        engine = sqlalchemy.create_engine(
            'mysql+mysqlconnector://'+user+':'+passwd+'@'+host+'/'+database)
        #  creation de la connexion
        cnx = engine.connect()
    except Exception as err:
        print(err)
        raise err
    print("connexion réussie")
    return cnx


def saisir_produit():
    ref = input("entrez la référence du produit: ")
    ref = int(ref)
    nom = input("entrez le nom du produit: ")
    prix = input("entre le prix unitaire du produit: ")
    prix = float(prix)
    return (ref, nom, prix)


def ajouter_des_produits(connexion):
    """
    ajoute un nouveau produit dans la base de données
    paramètres:
       connexion (Connection) une connexion ouverte sur le serveur MySQL
    """
    rep = 'O'
    while rep == 'O':
        prod = saisir_produit()
        try:
            #  instruction permettant l'insertion
            #  les %s vont être remplacés par les valeurs représentant le produit
            connexion.execute(
                "insert into PRODUIT(refProd, nomProd, PUProd) values (%s,%s,%s)", prod)
            print("le produit", prod, "a été inséré avec succès")
        except Exception as err:
            print("le produit", prod, "n'a pas pu être inséré")
            print(err)
        rep = input("Voulez vous ajouter un nouveau produit (O/N)? ")


def afficher_clients_ville(connexion):
    ville = input("entrez la ville dont vous recherchez les clients ")
    resultat = connexion.execute(
        "select numCli,nomCli,prenomCli from CLIENT where adresseCli=%s", ville)
    print("les clients habitant", ville, "sont les suivants")
    for (num, nom, prenom) in resultat:
        print(str(num).rjust(5), nom.ljust(15), prenom.ljust(15))


def afficher_clients_date_factures(connexion):
    resultat = connexion.execute("select numFac,date_format(dateFac,'%d/%m/%Y') as dateFacture, nomCli, prenomCli" +
                                 " from FACTURE natural join CLIENT order by numFac")
    for (numFac, dateFacture, nomCli, prenomCli) in resultat:
        print("numero : ", str(numFac).ljust(5), dateFacture.ljust(
            12), "Client : ", prenomCli+" "+nomCli)


def ajouter_des_clients(connexion):
    pass


def afficher_produits_entre_deux_prix(connexion):
    pass


def effacer_client(connexion):
    pass


def afficher_client_produits_quantité_date_factures(connexion):
    pass


if __name__ == "__main__":
    # login=input("login MySQL ")
    login = "root"
    passwd = ''
    serveur = '127.0.0.1'
    # bd=input("nom de la base de données ")
    bd = "facture"
    cnx = ouvrir_connexion(login, passwd, serveur, bd)
    #  ajouter_des_produits(cnx)
    #  afficher_clients_ville(cnx)
    #  afficher_clients_date_factures(cnx)
    #  afficher_client_produits_quantité_date_factures(cnx)
    #  ajouter_des_produits(cnx)
    #  ajouter_des_clients(cnx)
    #  afficher_clients_date_factures(cnx)
    #  afficher_produits_entre_deux_prix(cnx)
    #  effacer_client(cnx)

    cnx.close()
