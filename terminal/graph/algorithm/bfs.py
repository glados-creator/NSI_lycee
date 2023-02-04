import general


def voisins(G, sommet):
    return G[sommet]


def bfs(graph: dict):
    # fonction parcours_largeur(G,sommet):
    # sommet_visite = []
    # f = File()
    # f = sommet
    # Tant que f n’est pas vide faire
    #  on défile f dans tmp
    #  on affiche tmp
    #  Si tmp n’est pas dans sommet_visite alors
    #     l’ajouter à sommet_visite
    #  Pour chaque voisin de tmp faire
    #  Si il n’est pas dans sommet_visite et pas dans la file alors
    #     l’enfiler
    # fin tant que
    # renvoyer sommet_visite

    sommet_visite = []
    f = general.File()  # sommet
    f.enfiler(list(graph.keys())[0])
    while f.taille():
        tmp = f.defiler()
        if tmp not in sommet_visite:
            sommet_visite.append(tmp)
            # print(tmp,end=" ")
        for x in voisins(graph, tmp):
            if x not in sommet_visite:
                f.enfiler(x)
    return sommet_visite


# prof
def dfs_bis(G, sommet):
    p = general.Pile()
    sommets_visites = []
    p.empiler(sommet)
    while p.vide() == False:
        tmp = p.depiler()
        if tmp not in sommets_visites:
            sommets_visites.append(tmp)
            # print(tmp, end=" ")
        voisin = [y for y in voisins(G, tmp) if y not in sommets_visites]
        for vois in voisin:
            p.empiler(vois)
    return sommets_visites


# prof recurs
def bfs_recur(G, sommet):
    def bfs_recur_inner(G, f, sommets_visites):
        if f.vide():
            return None
        tmp = f.defiler()
        # print(tmp, end=" ")
        for u in voisins(G, tmp):
            if u not in sommets_visites:
                sommets_visites.append(u)
                f.enfiler(u)
        bfs_recur_inner(G, f, sommets_visites)

    f = general.File()
    sommets_visites = []
    sommet = 'b'
    f.enfiler(sommet)
    sommets_visites.append(sommet)
    bfs_recur_inner(G, f, sommets_visites)
