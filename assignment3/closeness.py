import networkx as nx
import functools
def close(G):
    r"""
    INPUT
    ----------
    G : graph
      A NetworkX graph
    OUTPUT
    -------
    nodes : dictionary
      Dictionary of nodes with closeness centrality as the value.
    """
    if G.is_directed():
        G = G.reverse()  # create a reversed graph view

    path_length = nx.single_source_shortest_path_length
    nodes = G.nodes
    closeness_centrality = {}
    for n in nodes:
        sp = path_length(G, n)
        totsp = sum(sp.values())
        len_G = len(G)
        _closeness_centrality = 0.0
        if totsp > 0.0 and len_G > 1:
            _closeness_centrality = (len(sp) - 1.0) / totsp
            s = (len(sp) - 1.0) / (len_G - 1)
            _closeness_centrality *= s
        closeness_centrality[n] = _closeness_centrality
    return closeness_centrality
