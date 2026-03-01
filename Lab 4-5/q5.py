graph = {
    'S': {'A': 3, 'B': 6, 'C': 5},
    'A': {'D': 9, 'E': 8},
    'B': {'F': 12, 'G': 14},
    'C': {'H': 7},
    'H': {'I': 5, 'J': 6},
    'I': {'K': 1},
    'J': {},
    'K': {},
    'L': {},
    'M': {},
    'D': {},
    'E': {},
    'F': {},
    'G': {},
}

heuristic = {
    'S': 7, 'A': 6, 'B': 8, 'C': 5,
    'D': 9, 'E': 7, 'F': 12, 'G': 14,
    'H': 4, 'I': 2, 'J': 1,
    'K': 0, 'L': 0, 'M': 0
}

def best_first_search(graph, start, goal):
    frontier = [(start, heuristic[start], 0, [start])]
    visited = set()
    came_from = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current_node, _, cost, path = frontier.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            return path, cost

        for neighbor, weight in graph.get(current_node, {}).items():
            if neighbor not in visited:
                came_from[neighbor] = current_node
                frontier.append((neighbor, heuristic.get(neighbor, 0), cost + weight, path + [neighbor]))

    return None, 0

def multi_goal_search(start, goals):
    current = start
    remaining_goals = set(goals)
    full_path = [start]
    total_cost = 0

    while remaining_goals:
        shortest_path = None
        shortest_cost = float('inf')
        reached_goal = None

        for goal in remaining_goals:
            path, cost = best_first_search(graph, current, goal)
            if path and cost < shortest_cost:
                shortest_path = path
                shortest_cost = cost
                reached_goal = goal

        if shortest_path is None:
            break

        full_path += shortest_path[1:]
        total_cost += shortest_cost
        current = reached_goal
        remaining_goals.remove(reached_goal)

        print("Reached Goal:", reached_goal)
        print("Current Path:", full_path)
        print("Total Cost So Far:", total_cost)
        print()

    return full_path, total_cost

print("Enhanced Maze Navigation")
print("Start Node: S")

goals = ['K', 'G']

path, cost = multi_goal_search('S', goals)

print("Final Path Covering All Goals:", path)
print("Total Cost:", cost)
