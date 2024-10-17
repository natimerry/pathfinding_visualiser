import osmnx as ox
import networkx as nx
import heapq
import numpy as np
import matplotlib.pyplot as plt
import pickle
import gc

path = input("Enter OSM path: ")
result = path.split('.')[0]
print(f"Pickling to preloaded_graphs/{result}.pickle")
gc.disable()
G = ox.graph_from_xml(path)
print(f"Loaded graph")
with open(f"preloaded_graphs/{result}.pickle","wb") as f:
    pickle.dump(G,f)
    