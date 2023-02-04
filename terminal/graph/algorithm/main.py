import networkx as nx
import matplotlib.pyplot as plt  # création du graphe à partir de listes

""" 
liste1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
g2 = nx.Graph()
g2.add_nodes_from(liste1)
liste2 = [('a', 'b'), ('a', 'c'), ('b', 'd'), ('b', 'e'), ('c', 'd'),
          ('d', 'e'), ('e', 'g'), ('e', 'f'), ('g', 'f'), ('g', 'h')]
g2.add_edges_from(liste2)
print(func(g2))
nx.draw(g2, with_labels=True, font_weight='bold',
        node_size=800, node_color='lightgrey')
plt.show()
"""
import bfs

G = dict()
G['a'] = ['b','c']
G['b'] = ['a','d','e']
G['c'] = ['a','d']
G['d'] = ['b','c','e']
G['e'] = ['b','d','f','g']
G['f'] = ['e','g']
G['g'] = ['e','f','h']
G['h'] = ['g']


c = bfs.dfs_bis(G, 'g')
print('\n')
print(c)