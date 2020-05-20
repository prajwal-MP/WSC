import networkx as nx
import matplotlib.pyplot as plt

from pagerank import pagerank
from HITS import hits
fig_count = 0#counter for naming plots

###plotd - 
#input G = Centrality values
#      S = Type of centrality
#output  
#      A plot of score

def plotd(G,s):
    global fig_count
    plt.plot(G.values())
    plt.ylabel('score ')#y axis
    plt.xlabel('Node number ')#x axis
    plt.title(s+'score of network')#title	
    #uncomment line below to see the plot
    #plt.show()
    plt.savefig(s+str(fig_count))#saving plot
    fig_count+=1
    #comment the lines below to see the plot
    plt.clf()
    plt.cla()
    plt.close()#closing plot

Graph = nx.read_edgelist('p2p-Gnutella04.txt')

hubs, authorities = hits(Graph, max_iter = 200) 
plotd(hubs,"hubs")
plotd(authorities,"authorities")
print("Hub Scores: ", hubs.values()[:5]) 
print("Authority Scores: ", authorities.values()[:5]) 

pr=pagerank(Graph,0.4)
print("PageRank: ",pr.values()[:5])
plotd(pr,"pagerank")