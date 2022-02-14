def breadth_first_search(graph, start, end):
    """
    Breadth First Search Algorithm.
    """
    queue = []
    queue.append(start)
    visited = set()
    visited.add(start)
    while queue:
        current = queue.pop(0)
        if current == end:
            return True
        for node in graph[current]:
            if node not in visited:
                queue.append(node)
                visited.add(node)
    return False