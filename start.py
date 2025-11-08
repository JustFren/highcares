import networkx as nx
import matplotlib.pyplot as plt
import random 

G = nx.Graph()
#add edge method iterate with two for loops for all edges
#G.add_node()
#G.add_edge()
num_nodes= range(28)
for i in range(28):
     G.add_node(i,UTM=[i**2,i**3])

print(G.nodes.data())
elist=[]
choices = random.choices(range(100),k=280)
for i in range(28):
    for j in range(0+10*i,10+10*i):
        if choices[j]%10-4<0:
            t=random.choice(num_nodes)
            while t==i:
                    t=random.choice(num_nodes)
            G.add_edge(i,t,weight=1)

elist=G.edges
weightlist=nx.get_edge_attributes(G,"weight")
pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility
#print(G.nodes.data)

#path = nx.dijkstra_path(G,0,1)
#print(path)
# nodes
nx.draw_networkx_nodes(G, pos, node_size=300)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elist, width=3)

# labels
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
edge_labels = nx.get_edge_attributes(G,"weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels,font_size=5)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()

