import networkx as nx
import matplotlib.pyplot as plt
from betweenness import between
from closeness import close
from degree import degree
from eigen import eigen
fig_count = 0#counter for naming plots

###plotd - 
#input G = Centrality values
#      S = Type of centrality
#output  
#      A plot of centrality vs node, saved as S + dataset number
# example 'degree0.png'
def plotd(G,s):
    global fig_count
    plt.plot(G.values())
    plt.ylabel('Normalised Centrality value ')#y axis
    plt.xlabel('Node number ')#x axis
    plt.title(s+'centrality of network')#title	
    #uncomment line below to see the plot
    #plt.show()
    plt.savefig(s+str(fig_count/4))#saving plot
    fig_count+=1
    #comment the lines below to see the plot
    plt.clf()
    plt.cla()
    plt.close()#closing plot


##Graph Dataset 1
Graph = nx.read_edgelist('email-Eu-core.txt')

deg_centrality = degree(Graph)
print("degree centrality: ",list(deg_centrality.values())[:5])
plotd(deg_centrality,"degree ")


eig_centrality = eigen(Graph)
print("eigen centrality: ",list(eig_centrality.values())[:5])
plotd(eig_centrality,"eigen ")


bet_centrality = between(Graph)
print("betweenness centrality: ",list(bet_centrality.values())[:5])
plotd(bet_centrality,"betweenness ")


clo_centrality = close(Graph)
print("closeness centrality: ",list(clo_centrality.values())[:5])
plotd(clo_centrality,"closeness ")

######################################################################################

##Graph Dataset 2

Graph = nx.read_edgelist('CA-GrQc.txt')

deg_centrality = degree(Graph)
print("degree centrality: ",list(deg_centrality.values())[:5])
plotd(deg_centrality,"degree ")


eig_centrality = eigen(Graph)
print("eigen centrality: ",list(eig_centrality.values())[:5])
plotd(eig_centrality,"eigen ")


bet_centrality = between(Graph)
print("betweenness centrality: ",list(bet_centrality.values())[:5])
plotd(bet_centrality,"betweenness ")


clo_centrality = close(Graph)
print("closeness centrality: ",list(clo_centrality.values())[:5])
plotd(clo_centrality,"closeness ")

######################################################################################

##Graph Dataset 3
Graph = nx.read_edgelist('p2p-Gnutella04.txt')


deg_centrality = degree(Graph)
print("degree centrality: ",list(deg_centrality.values())[:5])
plotd(deg_centrality,"degree ")


eig_centrality = eigen(Graph)
print("eigen centrality: ",list(eig_centrality.values())[:5])
plotd(eig_centrality,"eigen ")


bet_centrality = between(Graph)
print("betweenness centrality: ",list(bet_centrality.values())[:5])
plotd(bet_centrality,"betweenness ")


clo_centrality = close(Graph)
print("closeness centrality: ",list(clo_centrality.values())[:5])
plotd(clo_centrality,"closeness ")
######################################################################################

##Graph Dataset 4
Graph = nx.read_edgelist('Email-EuAll.txt')


deg_centrality = degree(Graph)
print("degree centrality: ",list(deg_centrality.values())[:5])
plotd(deg_centrality,"degree ")


eig_centrality = eigen(Graph)
print("eigen centrality: ",list(eig_centrality.values())[:5])
plotd(eig_centrality,"eigen ")


bet_centrality = between(Graph)
print("betweenness centrality: ",list(bet_centrality.values())[:5])
plotd(bet_centrality,"betweenness ")


clo_centrality = close(Graph)
print("closeness centrality: ",list(clo_centrality.values())[:5])
plotd(clo_centrality,"closeness ")

######################################################################################
