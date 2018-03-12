#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 14:13:25 2018

@author: snoopyknight
"""
import pandas as pd
import numpy as np
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns



# function to calculate the number of triangles in a simple
# directed/undirected graph.
# isDirected is true if the graph is directed, its false otherwise
def countTriangle(g, check_point, isDirected):
    nodes = len(g)
    count_Triangle = 0 #Initialize result
    # Consider every possible triplet of edges in graph
    for i in range(nodes):
        for j in range(nodes):
            for k in range(nodes):
                # check the triplet if it satisfies the condition
                if( i!=j and i !=k and j !=k and
                        g[i][j] and g[j][k] and g[k][i] and(i==check_point or j==check_point or k==check_point)):
                    count_Triangle += 1 
    # if graph is directed , division is done by 3, else division by 6 is done
    return count_Triangle/3 if isDirected else count_Triangle/6



def main():
    df = pd.read_csv('com-youtube.ungraph1.csv')    #file name
    #print(df)
    max_node = df.max()
    print(max_node)
    array_size = 1157733     #enter it in person
    
    ''' average degree '''
    degree = []
    a = list(df.FromNodeId)
    for i in range(1,array_size+1):
        tmp = a.count(i)
        degree.append(tmp)
    #print(degree)
    #print(degree[3])
    #avg_degree = sum(degree)/array_size
    #print(avg_degree)
    
    
    
    ''' clusting coefficient '''
    adj_array = np.zeros([array_size,array_size])   #adjacency matrix
    cur_node_start = 0
    for i in range(0,len(degree)):
        cur_node_end = degree[i]
        out = df.ToNodeId[cur_node_start:(cur_node_start+cur_node_end)]
        for j in out:   
            adj_array[i][j-1] = 1    
        cur_node_start = cur_node_start + cur_node_end
        #print(out)
        #print("=========================")
    print(adj_array)
        
    clustering_cofficient = []     #store clustering_cofficient for all node
    for x in range(array_size):    #the point that we want to calculate the clustering coefficient 
        num_friends = 0
        num_traingle = 0
        check_list = []
        for y in range(array_size):
            if adj_array[x][y] == 1:
                num_friends = num_friends + 1    #all friends of a
                check_list.append(y)
        num_traingle = countTriangle(adj_array, x, False) 
        print(num_traingle)        
        print(num_friends)
        print("==================")
        c = num_traingle/ (num_friends*(num_friends-1) / 2)   #clustering_cofficient formula
        clustering_cofficient.append(c)    
    print(clustering_cofficient)
    
    #np.savetxt("adj_array.txt",adj_array)
    
    
    '''degree disturbition'''
    '''
    sns.set(color_codes=True)
    sns.distplot(degree);
    '''

if __name__ == '__main__':
    main()
    
    