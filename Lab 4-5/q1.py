building = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1]
]

rows = len(building)
cols = len(building[0])

def grid_to_graph(grid):
    graph = {}
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                neighbors = []
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        neighbors.append((nr, nc))
                graph[(r,c)] = neighbors
    return graph

def bfs(graph, start, goal):
    visited = []
    queue = []
    came_from = {}
    visited.append(start)
    queue.append(start)
    came_from[start] = None

    while queue:
        node = queue.pop(0)
        print("Visiting:", node)
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = came_from[node]
            path.reverse()
            print("Shortest path:", path)
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
                came_from[neighbor] = node
    print("Goal not found")
    return None

graph = grid_to_graph(building)
start_node = (0,0)
goal_node = (3,3)
bfs(graph, start_node, goal_node)
