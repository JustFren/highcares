import networkx as nx
import matplotlib.pyplot as plt
import random 

G = nx.Graph()

def difficulty_weight():
    out=1
    return out


def profil_wysokościowy(path):
    fig, ax = plt.subplots()
    x=[i for i in range(len(path))]
    ay=[]
    print(path)
    #for i in range(len(path)):
    #    print(G.nodes.data()[i]["data"]["elevation"])
    for i in path:
        ay.append(G.nodes.data()[i]["data"]["elevation"])
    plt.plot(x,ay)    
    plt.show()


def best_path(num_of_nodes,node_data,):
    num_nodes = range(num_of_nodes)
    for i in num_nodes:
         G.add_node(i,data=node_data[i])

    # v zamieniasz to na metode dodawania krawedzi
    choices = random.choices(range(100),k=num_of_nodes*10) # maks 10 polaczen na wierzcholek 
    for i in num_nodes:
        for j in range(0+10*i,10+10*i):
            if choices[j]%10-4<0: #40% wytworzenia polaczenia
                t=random.choice(num_nodes)
                while t==i:
                        t=random.choice(num_nodes)
                G.add_edge(i,t,weight=1) # 1 zamieniasz na dowolna funkcje wagi
    
    #elist=G.edges
    #weightlist=nx.get_edge_attributes(G,"weight")
    #pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility
    
    path = nx.dijkstra_path(G,0,1)
    #print(path)
    
    
    # nodes
    #nx.draw_networkx_nodes(G, pos, node_size=300)
    # edges
    #nx.draw_networkx_edges(G, pos, edgelist=elist, width=3)
    # labels
    #nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
    #edge_labels = nx.get_edge_attributes(G,"weight")
    #nx.draw_networkx_edge_labels(G, pos, edge_labels,font_size=5)
    
    #plt
    #ax = plt.gca()
    #ax.margins(0.08)
    #plt.axis("off")
    #plt.tight_layout()
    #plt.show()
    return path


data=[]
for i in range(28):
    data_core={}
    data_core["elevation"]=i
    data_core["rest of data"]=0   
    data.append(data_core)   
#print(data)    
temp=best_path(28,data)
profil_wysokościowy(temp)