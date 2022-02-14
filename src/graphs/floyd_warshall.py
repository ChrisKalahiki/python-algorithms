def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm
    """
    # Initialize the distance matrix
    distance_matrix = [[float('inf') for _ in range(len(graph))] for _ in range(len(graph))]
    # Initialize the predecessor matrix
    predecessor_matrix = [[None for _ in range(len(graph))] for _ in range(len(graph))]
    # Initialize the distance matrix
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i == j:
                distance_matrix[i][j] = 0
            elif j in graph[i]:
                distance_matrix[i][j] = graph[i][j]
    # Iterate over all vertices
    for k in range(len(graph)):
        # Iterate over all vertices
        for i in range(len(graph)):
            # Iterate over all vertices
            for j in range(len(graph)):
                # If the distance of the adjacent vertex is greater than the distance of the current vertex plus the
                # weight of the edge between the two vertices, update the distance of the adjacent vertex
                if distance_matrix[i][j] > distance_matrix[i][k] + distance_matrix[k][j]:
                    distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j]
                    predecessor_matrix[i][j] = k
    # Iterate over all vertices
    for i in range(len(graph)):
        # Iterate over all vertices
        for j in range(len(graph)):
            # If the distance of the adjacent vertex is greater than the distance of the current vertex plus the
            # weight of the edge between the two vertices, return None
            if distance_matrix[i][j] > distance_matrix[i][i] + distance_matrix[j][j]:
                return None
    return distance_matrix, predecessor_matrix