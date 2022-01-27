def depth_first_traversal(graph, source):
    """Use stack to traverse a graph."""
    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        neighbors = graph[current]
        for neighbor in neighbors:
            stack.append(neighbor)


graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": [], "e": ["b"], "f": ["d"]}
