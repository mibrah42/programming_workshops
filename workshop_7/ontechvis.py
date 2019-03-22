#!/usr/bin/env python3
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def ws7_plot_graph(inputList):
    # These are parallel arrays for connections to nodes
    left  = []
    right = []

    alreadyConnected = set()

    for node in inputList:
        for connection in inputList[node]:
            connectionID = [node, connection]
            connectionID.sort()
            connectionID = tuple(connectionID)
            
            if connectionID in alreadyConnected:
                continue

            print("adding", node, connection)
            
            alreadyConnected.add(connectionID)
            left.append(node)
            right.append(connection)
    
    # Build a dataframe with 4 connections
    df = pd.DataFrame({ 'from':left, 'to':right })
    
    # Build your graph
    G=nx.from_pandas_edgelist(df, 'from', 'to')
    
    # Plot it
    nx.draw(G, with_labels=True)
    plt.show()
