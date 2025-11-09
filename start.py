import networkx as nx
import matplotlib.pyplot as plt
import random
import csv
import requests 

G = nx.Graph()

file=open("abs_elev.csv")
csvfile = csv.reader(file)
abs_elev=[]
for lines in csvfile:
    abs_elev.append(lines)

print(abs_elev)

def difficulty_weight(height):
    return height

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


def best_path(num_of_nodes,node_data):
    num_nodes = range(num_of_nodes)
    for i in num_nodes:
         G.add_node(i,data=node_data[i])

    # v zamieniasz to na metode dodawania krawedzi
    





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
#temp=best_path(28,data)
#profil_wysokościowy(temp)
plik=open("open-meteo-50.74N15.74E1587m.csv")

pogoda=0
csvPlik = csv.reader(plik)
for lines in csvPlik:
    if  lines[0][0] == '2':
        pogoda =lines
        break

def print_pogoda(pogoda):
    print("relative humidity: "+pogoda[1])    

print_pogoda(pogoda)
plik.close()