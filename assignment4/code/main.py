import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import ast
from operator import itemgetter

def centrality(G):
	#Degree centrality
	DC=nx.degree_centrality(G)
	all_values=DC.values()
	max_value=max(all_values)
	max_key=max(DC,key=DC.get)
	print("Degree centrality: Maximum value :",max_value)
	print("Degree centrality: Node with Maximum value :",max_key)
	res = dict(sorted(DC.items(), key = itemgetter(1), reverse = True)[:10]) 
  	# printing result 
	print("The top 10 Node centrality pairs are  " + str(res)) 

	#print(DC)

	#eigenvector centrality 
	EC=nx.eigenvector_centrality(G)
	all_values=EC.values()
	max_value=max(all_values)
	max_key=max(EC,key=EC.get)
	print("Eigenvector centrality: Maximum value :",max_value)
	print("Eigenvector centrality: Node with Maximum value :",max_key)
	res = dict(sorted(EC.items(), key = itemgetter(1), reverse = True)[:10]) 
  	# printing result 
	print("The top 10 Node centrality pairs are  " + str(res)) 
	#print(EC)

	#closeness centrality 
	CC=nx.closeness_centrality(G)
	all_values=CC.values()
	max_value=max(all_values)
	max_key=max(CC,key=CC.get)
	print("Closeness centrality: Maximum value :",max_value)
	print("Closeness centrality: Node with Maximum value :",max_key)
	res = dict(sorted(CC.items(), key = itemgetter(1), reverse = True)[:10]) 
  	# printing result 
	print("The top 10 Node centrality pairs are  " + str(res)) 
	#print(CC) """

	#betweenness centrality
	BC=nx.betweenness_centrality(G)
	all_values=BC.values()
	max_value=max(all_values)
	max_key=max(BC,key=BC.get)
	print("Betweenness centrality: Maximum value :",max_value)
	print("Betweenness centrality: Node with Maximum value :",max_key)
	res = dict(sorted(BC.items(), key = itemgetter(1), reverse = True)[:10]) 
  	# printing result 
	print("The top 10 Node centrality pairs are  " + str(res)) 
	#print(BC) 

	
	# Plot the centrality distribution
	all_centrality=DC.values()
	unique_centrality_1=list(set(all_centrality))
	#print unique_degrees
	count_of_centralities_1=[]
	for i in unique_centrality_1:
		x=list(all_centrality).count(i)
		count_of_centralities_1.append(x)

	all_centrality=EC.values()
	unique_centrality_2=list(set(all_centrality))
	#print unique_degrees
	count_of_centralities_2=[]
	for i in unique_centrality_2:
		x=list(all_centrality).count(i)
		count_of_centralities_2.append(x)


	all_centrality=CC.values()
	unique_centrality_3=list(set(all_centrality))
	#print unique_degrees
	count_of_centralities_3=[]
	for i in unique_centrality_3:
		x=list(all_centrality).count(i)
		count_of_centralities_3.append(x)


	all_centrality=BC.values()
	unique_centrality_4=list(set(all_centrality))
	#print unique_degrees
	count_of_centralities_4=[]
	for i in unique_centrality_4:
		x=list(all_centrality).count(i)
		count_of_centralities_4.append(x)

	plt.subplot(4, 1, 1)
	plt.plot(unique_centrality_1,count_of_centralities_1,'yo')
	plt.xlabel('Degree centralities')
	plt.ylabel('No of Nodes')
	plt.title('Degree centrality Distribution of Covid network')
	#plt.title('Degree centrality Distribution of Arxiv HEP-TH collaboration network')
	#plt.title('Degree centrality Distribution of Gnutella peer-to-peer network')
	plt.tight_layout()

	plt.subplot(4, 1, 2)
	plt.plot(unique_centrality_2,count_of_centralities_2,'yo')
	plt.xlabel('Eigenvector centralities')
	plt.ylabel('No of Nodes')
	plt.title('Eigenvector centrality Distribution of Covid network')
	#plt.title('Eigenvector centrality Distribution of Arxiv HEP-TH collaboration network')
	#plt.title('Eigenvector centrality Distribution of Gnutella peer-to-peer network')
	plt.tight_layout()

	plt.subplot(4, 1, 3)
	plt.plot(unique_centrality_3,count_of_centralities_3,'yo')
	plt.xlabel('Closeness centralities')
	plt.ylabel('No of Nodes')
	plt.title('Closeness centrality Distribution of Covid network')
	#plt.title('Closeness centrality Distribution of Arxiv HEP-TH collaboration network')
	#plt.title('Closeness centrality Distribution of Gnutella peer-to-peer network')
	plt.tight_layout()

	plt.subplot(4, 1, 4)
	plt.plot(unique_centrality_4,count_of_centralities_4,'yo')
	plt.xlabel('Betweenness centralities')
	plt.ylabel('No of Nodes')
	plt.title('Betweenness centrality Distribution of Covid network')
	#plt.title('Betweenness centrality Distribution of Arxiv HEP-TH collaboration network')
	#plt.title('Betweenness centrality Distribution of Gnutella peer-to-peer network')
	plt.tight_layout()
	plt.show()

def giant(G):
#connected=nx.is_connected(G)
#if connected :
  
	Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
	G0 = G.subgraph(Gcc[0])
	print (nx.info(G0))
	#print(list(G0.nodes))
	print ('Density : ',nx.density(G0))
	print ('Average clustering coefficient : ',nx.average_clustering(G0))
	print('Diameter: ', nx.diameter(G0)) 
	print ('k value in k-connectedness : ',nx.node_connectivity(G0))
	print ('average of shortest paths : ',nx.average_shortest_path_length(G0))
  	nx.draw_networkx_edges(G0, pos=nx.spring_layout(G0),
                           with_labels=False,
                           edge_color='r',
                           width=6.0
                          )
	plt.show()

def plot_deg_dist(G):
        all_dregrees=dict(G.in_degree()).values()
        unique_degrees=list(set(all_dregrees))
	#print unique_degrees
	count_of_degrees=[]

	for i in unique_degrees:
		x=list(all_dregrees).count(i)
		count_of_degrees.append(x)
	maxvalue=max(unique_degrees)
        max_key=max(dict(G.in_degree()),key=dict(G.in_degree()).get)
        print('Patient with max degree:',max_key)
        print('No of people affected:',maxvalue)
	plt.plot(unique_degrees,count_of_degrees,'yo')
	#plt.loglog(unique_degrees,count_of_degrees,'yo')
	plt.xlabel('Degree')
	plt.ylabel('No of Nodes')
	#plt.title('Log-log Degree Distribution of Covid network')
        plt.title('Degree Distribution of Covid network')
	plt.show()	



def plot_dist(G,attr):
	all_values=dict(nx.get_node_attributes(G,attr)).values()
        alll=dict(nx.get_node_attributes(G,attr))
	unique_values=list(set(all_values))
        print(unique_values)
	
	count_of_values=[]
	for i in unique_values:
		x=0
		for p in alll:
			if(alll[p]==i):
				x+=G.node[p]['weight']
		#x=list(all_values).count(i)
		count_of_values.append(x)
	print(count_of_values)
	#plt.plot(unique_values,count_of_values,'yo')
	plt.bar(unique_values,count_of_values,align='center')
	#plt.loglog(unique_degrees,count_of_degrees,'yo')
	plt.xlabel('gender')
	plt.ylabel('No of Patients')
	#plt.title('Log-log Degree Distribution of Covid network')
        plt.title('Gender distribution of Covid patients')
	plt.show()

def plot_bar(G):
	deceased=[]
	recovered=[]
	hospital=[]
	Death=dict(nx.get_node_attributes(G,'Current Status'))
	for p in Death:
		if(Death[p]=='Recovered'):
			recovered.append(p)
		if(Death[p]=='Deceased'):
			deceased.append(p)
		if(Death[p]=='Hospitalized'):
			hospital.append(p)

	gend=dict(nx.get_node_attributes(G,'gender'))
	menMeans=[]
	womenMeans=[]
	m=[]
	f=[]
	for p in gend:
		if(gend[p]=='M'):
			m.append(p)
		if(gend[p]=='F'):
			f.append(p)
	menMeans.append(len(set(m).intersection(set(recovered))))
	womenMeans.append(len(set(f).intersection(set(recovered))))
	menMeans.append(len(set(m).intersection(set(deceased))))
	womenMeans.append(len(set(f).intersection(set(deceased))))
	menMeans.append(len(set(m).intersection(set(hospital))))
	womenMeans.append(len(set(f).intersection(set(hospital))))
	ind = np.arange(3) # the x locations for the groups
	width = 0.35
	fig = plt.figure()
	ax = fig.add_axes([0,0,1,1])
	ax.bar(ind, menMeans, width, color='r')
	ax.bar(ind, womenMeans, width,bottom=menMeans, color='b')
	ax.set_ylabel('Number of patients')
	ax.set_title('Genderwise analysis')
	ax.set_xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
	ax.set_yticks(np.arange(0, 81, 10))
	ax.legend(labels=['Men', 'Women'])
	plt.show()




G=nx.read_edgelist('../Data/test.edgelist')
#G=nx.read_edgelist('../Data/test.edgelist',create_using=nx.DiGraph())
G.remove_node("ISO")
print (nx.info(G))

file = open("../Data/attributes2", "r")

contents = file.read()
dictionary = ast.literal_eval(contents)
nx.set_node_attributes(G, dictionary)
#nx.set_node_attributes(G, 1, 'weight')
#age=nx.get_node_attributes(G,'age')
age=dict(nx.get_node_attributes(G,'age')).values()
#print(age)
#print(G.nodes.data())
filtered = []
Death=dict(nx.get_node_attributes(G,'Current Status'))
#print(Death)
for p in Death:
	if(Death[p]=='Recovered'):
		filtered.append(p)
#print(filtered)
H = G.subgraph(list(filtered))
"""filtered = []
for (p, d) in G.nodes(data=True):
    if d['Current Status'] == 'Deceased':
        filtered.append(p)"""



directed=nx.is_directed(G)

print ('Density : ',nx.density(G))
print ('Average clustering coefficient : ',nx.average_clustering(G))



if directed:
	print ('Is graph strongly connected : ',nx.is_strongly_connected(G))
	print ('Number of strongly connected components : ',nx.number_strongly_connected_components(G))
else :
	connected=nx.is_connected(G)
	print ('Is graph connected : ',connected)
	if connected :
		print('Diameter: ', nx.diameter(G)) 
		print ('k value in k-connectedness : ',nx.node_connectivity(G))
		print ('average of shortest paths : ',nx.average_shortest_path_length(G))
		print ('Number of connected components : ',nx.number_connected_components(G))

#plot_deg_dist(G)
#plot_dist(G,attr='gender')
giant(G)
#nx.draw(G)
#plt.show()
#plot_bar(G)
#centrality(G)
file.close()
