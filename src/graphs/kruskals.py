def kruskals(graph):
    """
    Returns the minimum spanning tree of a graph using Kruskal's algorithm.
    """
    # Initialize the minimum spanning tree.
    mst = []
    # Initialize the set of vertices.
    vertices = set(graph.keys())
    # Sort the edges in non-decreasing order.
    edges = sorted(graph.values(), key=lambda edge: edge.weight)
    # Iterate over the edges.
    while edges:
        # Get the first edge.
        edge = edges.pop(0)
        # Get the vertices of the edge.
        u, v = edge.vertices
        # Check if the vertices are in the same set.
        if u.root is not v.root:
            # Add the edge to the minimum spanning tree.
            mst.append(edge)
            # Merge the sets.
            u.root, v.root = v.root, u.root
            # Remove the edge from the set of edges.
            edges.remove(edge)
    # Return the minimum spanning tree.
    return mst