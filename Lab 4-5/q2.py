graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H'],
    'G': [],
    'H': []
}

def dls(graph, node, goal, depth, path, visited):
    print(f"  Visiting: {node} (depth={len(path)-1})")
    if node == goal:
        return path
    if depth == 0:
        return None
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            visited.add(neighbor)
            result = dls(graph, neighbor, goal, depth - 1, path + [neighbor], visited)
            if result:
                return result
            visited.discard(neighbor)
    return None


for limit in [2, 3]:
    print(f"\n Depth Limit = {limit} ")
    result = dls(graph, 'A', 'H', limit, ['A'], {'A'})
    if result:
        print("Path found:", result)
    else:
        print(f"Goal not found within depth {limit}")
