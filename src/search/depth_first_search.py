def depth_first_search(graph, start, end):
    """
    Depth First Search Algorithm.
    """
    stack = []
    stack.append(start)
    visited = set()
    visited.add(start)
    while stack:
        current = stack.pop()
        if current == end:
            return True
        for node in graph[current]:
            if node not in visited:
                stack.append(node)
                visited.add(node)
    return False