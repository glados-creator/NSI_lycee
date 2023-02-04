import networkx as nx
import matplotlib.pyplot as plt

liste1=['1','2','3','4']
g2 = nx.Graph()
g2.add_nodes_from(liste1)
liste2=[("1","2"),("1","3"),("1","4"),("2","4"),("2","3")]
g2.add_edges_from(liste2)
nx.draw(g2, with_labels=True, font_weight='bold', node_size=800, node_color='lightgrey')
plt.show()


B = nx.adjacency_matrix(g2)
print(nx.adjacency_matrix(g2))

n=len(liste1)
A=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        A[i][j]= B[(i,j)]
    print(A)


