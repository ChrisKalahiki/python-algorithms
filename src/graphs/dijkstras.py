def dijkstras(graph, start, end):
    """
    Dijkstra's algorithm for finding the shortest path between two nodes.
    :param graph: The graph to search through.
    :param start: The starting node.
    :param end: The ending node.
    :return: The shortest path between the two nodes.
    """
    # Initialize the distance to the start node to 0.
    distance = {start: 0}
    # Initialize the nodes to search through.
    nodes = graph.nodes
    # Initialize the visited nodes.
    visited = set()
    # Initialize the path.
    path = []
    # Initialize the current node.
    current = start
    # While there are still nodes to search through.
    while nodes:
        # If the current node is the ending node.
        if current == end:
            # Return the path.
            return path
        # If the current node has already been visited.
        if current in visited:
            # Remove the current node from the nodes to search through.
            nodes.remove(current)
            # Continue to the next iteration.
            continue
        # Add the current node to the visited nodes.
        visited.add(current)
        # Get the edges of the current node.
        edges = graph.edges[current]
        # For each edge.
        for edge in edges:
            # Get the weight of the edge.
            weight = edges[edge]
            # If the distance to the end node is greater than the weight of the edge.
            if distance[end] > distance[current] + weight:
                # Set the distance to the end node to the weight of the edge.
                distance[end] = distance[current] + weight
                # Set the path to the current node.
                path = [current]
                # Set the current node to the edge.
                current = edge
                # Break out of the loop.
                break