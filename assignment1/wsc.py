# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.components import strongly_connected_components, connected_components

Graph = nx.read_edgelist('CA-GrQc.txt')


def plotd(G):
	all_degree=dict(nx.degree(G)).values()
	unique_degree=list(set(all_degree))
	count_degree=[]
	all_degree=list(all_degree)
	for i in unique_degree:
		x=all_degree.count(i)
		count_degree.append(x)
	plt.plot(unique_degree,count_degree,'yo-')
	plt.xlabel('Degrees')
	plt.ylabel('No of nodes ')
	plt.title('Degree distribution of network')
	plt.show()

plotd(Graph)

print("Graph is directed ",nx.is_directed(Graph))

nx.draw(Graph)
plt.show()

print("Graph Density is ",nx.density(Graph))

print("Clustering co-eff is",nx.average_clustering(Graph))
print(nx.info(Graph))


com=0
for C in (Graph.subgraph(c).copy() for c in connected_components(Graph)):
  com=com+1

print("Total components are" ,com)




#################################################################################################################


GB=nx.barabasi_albert_graph(5242, 20, seed=None)

for C in (GB.subgraph(c).copy() for c in connected_components(GB)):
  print(nx.average_shortest_path_length(C))

print(nx.average_clustering(GB))

plotd(GB)

#################################################################################################################

Gr = nx.gnm_random_graph(5242, 28980)

for C in (Gr.subgraph(c).copy() for c in connected_components(Gr)):
  print(nx.average_shortest_path_length(C))


print(nx.average_clustering(Gr))
plotd(Gr)


#################################################################################################################


GW =nx.watts_strogatz_graph(5242, 10, 0.6, seed=None)


component=0
for C in (GW.subgraph(c).copy() for c in connected_components(GW)):
  print(nx.average_shortest_path_length(C))

print(nx.average_clustering(GW))

plotd(GW)


#################################################################################################################


