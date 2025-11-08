import networkx as nx
import matplotlib.pyplot as plt
import random 

G = nx.Graph()
#add edge method iterate with two for loops for all edges
#G.add_node()
#G.add_edge()
nlist=[i for i in range(28)]
G.add_nodes_from(nlist)
elist=[]
choices = random.choices(range(100),k=280)
for i in range(28):
    for j in range(0+10*i,10+10*i):
        if choices[j]%10-4<0:
            t=random.choice(nlist)
            while t==i:
                    t=random.choice(nlist)
            G.add_edge(i,t,weight=(choices[j]%10)/10)

elist=G.edges
print(elist)
pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

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

