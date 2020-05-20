def degree(G):
    """    
    INPUT
    ----------
    G : graph
      A networkx graph
    OUTPUT
    -------
    nodes with degree centrality as the value.
    """
    if len(G) <= 1:
        return {n: 1 for n in G}

    s = 1.0 / (len(G) - 1.0)
    centrality = {n: d * s for n, d in G.degree()}
    return centrality