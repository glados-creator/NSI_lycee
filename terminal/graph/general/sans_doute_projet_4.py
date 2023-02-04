import networkx as nx
import matplotlib.pyplot as plt

liste1=['a','b','c','d']
g2 = nx.Graph()
g2.add_nodes_from(liste1)
liste2=[('a','b'),('a','c'),('c','b'),('c','d'),('b','d')]
g2.add_edges_from(liste2)
nx.draw(g2, with_labels=True, font_weight='bold', node_size=800, node_color='lightgrey')
plt.show()

print([x for x in nx.dfs_edges(g2.nodes)])

print()
print([x for y in liste1 for x in nx.all_simple_paths(g2,"c",y)])