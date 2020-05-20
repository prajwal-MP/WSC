def between(G):
    r"""
    INPUT
    ----------
    G : graph
      A NetworkX graph.
    Output
    -------
    nodes with betweenness centrality as the value.
    """
    betweenness = dict.fromkeys(G, 0.0)
    nodes = G
    for s in nodes:
        # shortest paths
        S, P, sigma = shortest_path(G, s)
        delta = dict.fromkeys(S, 0)
        while S:
            w = S.pop()
            coeff = (1.0 + delta[w]) / sigma[w]
            for v in P[w]:
                delta[v] += sigma[v] * coeff
            if w != s:
                betweenness[w] += delta[w]
    scale = 1.0 / ((len(G) - 1) * (len(G) - 2))
    for v in betweenness:
        betweenness[v] *= scale
    return betweenness

def shortest_path(G, s):
    S = []
    P = {}
    for v in G:
        P[v] = []
    sigma = dict.fromkeys(G, 0.0)    # sigma[v]=0 for v in G
    D = {}
    sigma[s] = 1.0
    D[s] = 0
    Q = [s]
    while Q:   # use BFS to find shortest paths
        v = Q.pop(0)
        S.append(v)
        Dv = D[v]
        sigmav = sigma[v]
        for w in G[v]:
            if w not in D:
                Q.append(w)
                D[w] = Dv + 1
            if D[w] == Dv + 1:   # this is a shortest path, count paths
                sigma[w] += sigmav
                P[w].append(v)  # predecessors
    return S, P, sigma
