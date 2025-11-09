import networkx as nx
import matplotlib.pyplot as plt
import random
import csv
import requests 
import os
from difficulty_assessment import difficulty_assessment
G = nx.Graph()

def difficulty_weight(height,user_type,trail_type):
    #trasy
    #łatwa - e
    #średnia - m
    #trudna - h
    #bardzo trudna -v
    if user_type =="e":
        if trail_type == "e":
            mult = 1
        if trail_type == "m":
            mult = 2
        if trail_type == "h":
            mult = 4
        if trail_type == "v":
            mult = 8

    if user_type =="m":
        if trail_type == "e":
            mult = 2
        if trail_type == "m":
            mult = 1
        if trail_type == "h":
            mult = 2
        if trail_type == "v":
            mult = 4

    if user_type =="h":
        if trail_type == "e":
            mult = 4
        if trail_type == "m":
            mult = 2
        if trail_type == "h":
            mult = 1
        if trail_type == "v":
            mult = 2

    if user_type =="v":
        if trail_type == "e":
            mult = 100
        if trail_type == "m":
            mult = 50
        if trail_type == "h":
            mult = 20
        if trail_type == "v":
            mult = 1
        
    return height * mult


def best_path(num_of_nodes,node_data,starting_point,user_type):
    num_nodes = range(1,num_of_nodes+1)
    for i in num_nodes:
         G.add_node(i,data=node_data[i-1])


    # v zamieniasz to na metode dodawania krawedzi
    #v_data - idv id1 id2 wchodzenie schodzenie
    file=open("abs_elev.csv")
    csvfile = csv.reader(file)
    abs_elev=[]
    for lines in csvfile:
        abs_elev.append(lines)
    file=open("v_data.csv")
    csvfile = csv.reader(file)
    e_data=[]
    for lines in csvfile:
        e_data.append(lines)
    for edge in e_data:
        G.add_edge(int(edge[1]),int(edge[2]),
                   weight=\
                   difficulty_weight(float(abs_elev[int(edge[0])-1][1]),user_type,edge[5]),
                   time_asc=edge[3],
                   time_desc=edge[4])

    path = nx.dijkstra_path(G,starting_point,15)
    sum_of_time=0
    for i in range(len(path)-1):
        sum_of_time+=int(G.edges[path[i],path[i+1]]["time_asc"])
    #print(path)
    return path

def read_nodes_data():
    data=[]
    plik=open("nodes.csv")
    nodes_csv=csv.reader(plik)
    for lines in nodes_csv:
        data_core={}
        data_core["id"]=lines[0]
        data_core["nazwa"]=lines[1]
        data_core["elevation"]=lines[2]   
        data.append(data_core)      
    return data

def read_pogoda():
    plik=open("open-meteo-50.74N15.74E1587m.csv")
    pogoda=0
    csvPlik = csv.reader(plik)
    for lines in csvPlik:
        if  lines[0][0] == '2':
            pogoda = lines
            break
    return pogoda    
    
def print_pogoda(pogoda):
    print("   relative humidity: "+pogoda[1]+"%")
    print("   precipitation probability: "+pogoda[2]+"%")
    print("   precipitation: "+pogoda[3]+" mm")
    print("   pressure (mean sea level): "+pogoda[4]+" hPa")
    print("   surface pressure: "+pogoda[5]+" hPa")
    print("   visibility: "+pogoda[6]+" m")
    print("   wind speed: "+pogoda[7]+" km/s")
    print("   temperature: "+pogoda[8]+" °C")

def get_path_names():
    name_path=[]       
    for i in range(len(path)):
        name_path.append(G.nodes.data()[int(path[i])]["data"]["nazwa"])
    return name_path

user_diff = difficulty_assessment()[1]

path=best_path(28,read_nodes_data(),2,user_diff)
print("Weather:")
print_pogoda(read_pogoda())
print("Path is:")
path_names=get_path_names()
for i in range(len(path)):
    print("   "+path_names[i])


