def topological_sort(graph):
    """
    Topological sort of a directed acyclic graph.
    """
    # Initialize the stack.
    stack = []
    # Initialize the visited set.
    visited = set()
    # Iterate over the vertices.
    for vertex in graph:
        # Check if the vertex is not visited.
        if vertex not in visited:
            # Visit the vertex.
            visit(vertex, graph, stack, visited)
    # Return the stack.
    return stack