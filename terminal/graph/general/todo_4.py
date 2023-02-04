import networkx as nx
import matplotlib.pyplot as plt

liste1=['a','b','c','d','e','f']
g2 = nx.DiGraph()
g2.add_nodes_from(liste1)
liste2=[('a','b'),('a','c'),('b','c'),('b','d'),('d','e'),('e','f'),('f','c'),('c','d'),('c','e')]
g2.add_edges_from(liste2)
nx.draw(g2, with_labels=True, font_weight='bold', node_size=800, node_color='lightgrey')
plt.show()

print([x for x in nx.dfs_edges(g2)])