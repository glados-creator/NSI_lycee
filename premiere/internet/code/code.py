import requests # librairie qui gère les connexion HTTP
url = "https://google.com/azeaze"
reponse = requests.get(url)
# on établit une connexion avec le site Pre NSI DDM45
print(reponse)

for x in ["reponse.headers","reponse.content","reponse.request","reponse.request.headers"]:
    with open(x +".txt","w") as f:
        f.write(str(eval(x)))