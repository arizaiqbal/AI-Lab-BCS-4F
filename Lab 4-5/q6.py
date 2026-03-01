import random
import time

graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {}
}

heuristic = {'A': 14, 'B': 12, 'C': 11, 'D': 6, 'E': 4, 'F': 11, 'G': 0}

def a_star(graph, start, goal):
    frontier = [(start, heuristic[start])]
    visited = set()
    g_costs = {start: 0}
    came_from = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current_node, current_f = frontier.pop(0)

        if current_node in visited:
            continue

        print("Expanding:", current_node, "g:", g_costs[current_node], "f:", current_f)
        visited.add(current_node)

        if current_node == goal:
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = came_from[node]
            path.reverse()
            return path, g_costs[goal]

        for neighbor, cost in graph[current_node].items():
            new_g = g_costs[current_node] + cost
            f_cost = new_g + heuristic[neighbor]

            if neighbor not in g_costs or new_g < g_costs[neighbor]:
                g_costs[neighbor] = new_g
                came_from[neighbor] = current_node
                frontier.append((neighbor, f_cost))

    return None, None

def random_edge_change():
    nodes = list(graph.keys())
    while True:
        u = random.choice(nodes)
        if graph[u]:
            v = random.choice(list(graph[u].keys()))
            break
    old_cost = graph[u][v]
    change = random.randint(-3, 5)
    new_cost = max(1, old_cost + change)
    graph[u][v] = new_cost
    print("\nEdge cost changed:", u, "→", v, old_cost, "→", new_cost)

def dynamic_a_star(start, goal):
    current = start
    total_path = [start]
    total_cost = 0

    while current != goal:
        path, cost = a_star(graph, current, goal)
        if not path:
            print("No path found")
            return

        if len(path) > 1:
            next_node = path[1]
            step_cost = graph[current][next_node]

            total_cost += step_cost
            total_path.append(next_node)
            current = next_node

            print("Moving to:", next_node, "Total Cost:", total_cost)

            if random.random() < 0.5:
                random_edge_change()

            time.sleep(1)

    print("\nFinal Optimal Path:", total_path)
    print("Final Total Cost:", total_cost)

print("Dynamic A* Search Started")
dynamic_a_star('A', 'G')
