import networkx as nx
import matplotlib.pyplot as plt #création du graphe à partir de listes 
liste1=['a','b','c','d','e','f','g','h']
g2 = nx.Graph()
g2.add_nodes_from(liste1)
liste2=[('a','b'),('a','c'),('b','d'),('b','e'),('c','d'),('d','e'), ('e','g'),('e','f'),('g','f'),('g','h')]
g2.add_edges_from(liste2)
nx.draw(g2, with_labels=True, font_weight='bold', node_size=800, node_color='lightgrey')
plt.show()

B = nx.adjacency_matrix(g2) 
print(B[(0,0)])
n=len(liste1)
A=[[0]*n for i in range(n)] 
for i in range(n):
    for j in range(n): 
        A[i][j]= B[(i,j)]
    print(A)

# g.degree(’a’)
# g.number_of_nodes() 
# g.number_of_edges()
# g.neighbors(i)
# g.predecessors(i) 
# g.successors(i)
