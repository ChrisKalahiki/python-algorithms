def bellman_ford(graph, source):
    """
    Bellman-Ford algorithm for finding the shortest path from source to all other vertices in a graph.
    :param graph: a graph represented as a dictionary of dictionaries
    :param source: the source vertex
    :return: a dictionary of shortest paths from source to all other vertices in the graph
    """
    # Initialize distances to all vertices as infinite
    distances = {vertex: float('inf') for vertex in graph}
    # Set the distance of source to 0
    distances[source] = 0
    # Iterate over all vertices
    for _ in range(len(graph) - 1):
        # Iterate over all edges in the graph
        for vertex in graph:
            # Iterate over all adjacent vertices of the current vertex
            for adjacent_vertex in graph[vertex]:
                # If the distance of the adjacent vertex is greater than the distance of the current vertex plus the
                # weight of the edge between the two vertices, update the distance of the adjacent vertex
                if distances[adjacent_vertex] > distances[vertex] + graph[vertex][adjacent_vertex]:
                    distances[adjacent_vertex] = distances[vertex] + graph[vertex][adjacent_vertex]
    # Iterate over all edges in the graph
    for vertex in graph:
        # Iterate over all adjacent vertices of the current vertex
        for adjacent_vertex in graph[vertex]:
            # If the distance of the adjacent vertex is greater than the distance of the current vertex plus the
            # weight of the edge between the two vertices, return None
            if distances[adjacent_vertex] > distances[vertex] + graph[vertex][adjacent_vertex]:
                return None
    return distances