import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import ast
G = nx.path_graph(3)
attrs = {0: {'attr1': 20, 'attr2': 'nothing'}, 1: {'attr2': 3}}
nx.set_node_attributes(G, attrs)
print(G.nodes[0]['attr1'])

G.nodes[0]['attr2']

G.nodes[1]['attr2']

G.nodes[2]

