import networkx as nx
from math import sqrt

def eigen(G, max_iter=100):
    r"""
    Input
    ----------
    G : graph
      A networkx graph
    max_iter : 
      Maximum number of iterations in power method.
    output
    -------
    nodes with eigenvector centrality as the value.
    """
    tol = 1.0e-6#tolerance value
    # initial vector 
    nstart = {v: 1 for v in G}
    # Normalize the initial vector 
    nstart_sum = sum(nstart.values())
    x = {k: (v*1.0) / nstart_sum for k, v in nstart.items()}
    
    nnodes = G.number_of_nodes()
    # make up to max_iter iterations
    weight = None
    for i in range(max_iter):
        xlast = x
        x = xlast.copy()  # Start with xlast
        for n in x:
            for nbr in G[n]:
                w = G[n][nbr].get(weight, 1) if weight else 1
                x[nbr] += xlast[n] * w
        # Normalize the vector
        norm = sqrt(sum(z ** 2 for z in x.values())) or 1
        x = {k: (v*1.0) / norm for k, v in x.items()}
        if sum(abs(x[n] - xlast[n]) for n in x) < nnodes * tol:
            return x
