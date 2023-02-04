import networkx as nx 
# On crée un graphe vide #création du graphe
g1 = nx.Graph()
# On ajoute les sommets (appelés node) #création des sommets 
g1.add_node('a')
g1.add_node('b')
g1.add_node('c')
g1.add_node('d')
g1.add_node('e')
g1.add_node('f')
g1.add_node('g')
g1.add_node('h')
# On ajoute les arêtes (appelés edge) #Création des arêtes 
g1.add_edge('a','b')
g1.add_edge('a','c')
g1.add_edge('b','d')
g1.add_edge('b','e')
g1.add_edge('c','d')
g1.add_edge('d','e')
g1.add_edge('e','g')
g1.add_edge('e','f')
g1.add_edge('g','f')
g1.add_edge('g','h')

import matplotlib.pyplot as plt

nx.draw(g1, with_labels=True, font_weight='bold', node_size=800, node_color='lightgrey')
plt.show()
