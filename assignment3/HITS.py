import networkx as nx
def hits(G, max_iter=100, tol=1.0e-8, nstart=None, normalized=True):
    """
    Input
    ----------
    G : graph
      A NetworkX graph
    max_iter : integer, optional
      Maximum number of iterations in power method.
    Output
    -------
       Two dictionaries keyed by node containing the hub and authority
       values.
    """
    h = dict.fromkeys(G, 1.0 / G.number_of_nodes())
    for _ in range(max_iter):  # up to max_iter iterations
        hlast = h
        h = dict.fromkeys(hlast.keys(), 0)
        a = dict.fromkeys(hlast.keys(), 0)
        for n in h:
            for nbr in G[n]:
                a[nbr] += hlast[n] * G[n][nbr].get("weight", 1)
        for n in h:
            for nbr in G[n]:
                h[n] += a[nbr] * G[n][nbr].get("weight", 1)
        s = 1.0 / max(h.values())
        for n in h:
            h[n] *= s
        s = 1.0 / max(a.values())
        for n in a:
            a[n] *= s
        err = sum([abs(h[n] - hlast[n]) for n in h])
        if err < tol:
            break
    s = 1.0 / sum(a.values())
    for n in a:
        a[n] *= s
    s = 1.0 / sum(h.values())
    for n in h:
        h[n] *= s
    return h, a