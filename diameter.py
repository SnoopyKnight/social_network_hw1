# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 03:53:02 2018

@author: Chunbi
"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 14:13:25 2018

@author: 
"""
import pandas as pd
import numpy as np
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
import queue
import networkx as nx 


def main():
    df = pd.read_csv('com-youtube.ungraph.csv')    #file name
    # Nodes: 1134890 Edges: 2987624
    lenght = df.FromNodeId.size

    
    ''' average degree '''
    print("average degree: ",(2987624*2)/1134890)

    
    '''daimeter'''
    G = nx.Graph()   
    for i in range(0,lenght):    
        G.add_edge(df.iloc[i]['FromNodeId'],df.iloc[i]['ToNodeId'])
    #max degree
    MaxDegree = max(G.degree().items(), key = lambda x: x[1]) 
    bfs = list(nx.bfs_edges(G,MaxDegree[0]))
    r1 = bfs[len(bfs)-1][1]
    a1 = list(nx.bfs_edges(G,r1))
    a1 = a1[len(a1)-1][1]
    b1 = list(nx.bfs_edges(G,a1))
    b1 = b1[len(b1)-1][1]
    distance = nx.dijkstra_path_length(G, source=a1, target=b1)
    ##
    MaxDegree = max(G.degree().items(), key = lambda x: x[1]) 
    bfs = list(nx.bfs_edges(G,MaxDegree[0]))
    r1 = bfs[len(bfs)-1][1]
    a1 = list(nx.bfs_edges(G,r1))
    a1 = a1[len(a1)-1][1]
    b1 = list(nx.bfs_edges(G,a1))
    b1 = b1[len(b1)-1][1]
    r2 = nx.dijkstra_path(G, source=a1, target=b1)
    r2 = r2[int((len(r2)+1)/2)]
    bfs_r2 = list(nx.bfs_edges(G,r2))
    a2 = bfs_r2[len(bfs_r2)-1][1]
    b2 = list(nx.bfs_edges(G,a2))
    b2 = b2[len(b2)-1][1]
    path = nx.dijkstra_path(G, source=a2, target=b2)
    lb = len(path)-1
    u = path[int((len(path)-1)/2)]
    ecc_u = list(nx.bfs_edges(G,u))
    ecc_u = ecc_u[len(ecc_u)-1][1]
    ecc_u =  nx.dijkstra_path_length(G, source=u, target=ecc_u)
    ub = 2 * ecc_u\
    ##
    print('diameter: ',distance)
    
    
    ### clustering coefficietn ###
    c = nx.average_clustering(G)
    
if __name__ == '__main__':
    main()
    
    

