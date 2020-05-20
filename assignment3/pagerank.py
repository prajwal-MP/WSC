import networkx as nx
def pagerank(G, alpha=0.85,weight='weight'):
    """Returns the PageRank of the nodes in the graph.
    INPUT
    ----------
    G : graph
      A NetworkX graph
    OUTPUT
    -------
    nodes with PageRank as value
    """

    if not G.is_directed():
        D = G.to_directed()
    else:
        D = G
    tol=1.0e-6
    max_iter=100
    W = nx.stochastic_graph(D, weight=weight)
    N = W.number_of_nodes()
    x = dict.fromkeys(W, 1.0 / N)
    p = dict.fromkeys(W, 1.0 / N)

    dangling_weights = p
    dangling_nodes = [n for n in W if W.out_degree(n, weight=weight) == 0.0]

    for _ in range(max_iter):
        xlast = x
        x = dict.fromkeys(xlast.keys(), 0)
        danglesum = alpha * sum(xlast[n] for n in dangling_nodes)
        for n in x:
            for nbr in W[n]:
                x[nbr] += alpha * xlast[n] * W[n][nbr][weight]
            x[n] += danglesum * dangling_weights.get(n, 0) + (1.0 - alpha) * p.get(n, 0)
        err = sum([abs(x[n] - xlast[n]) for n in x])
        if err < N * tol:
            return x
    raise nx.PowerIterationFailedConvergence(max_iter)
