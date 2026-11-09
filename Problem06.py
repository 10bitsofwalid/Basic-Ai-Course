# ==========================================
# Problem 06: Breadth-First Search (BFS) Pathfinding with Battery Constraint
# Description: Implements Breadth-First Search (BFS) to find a valid path
#              between graph states, subject to minimum battery constraints.
# ==========================================

# Step 1: Define state space and graph adjacency list (directed edges)
states = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
paths = {
    0: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    1: [2, 3, 4, 5, 6, 7, 8, 9, 10],
    2: [3, 4, 5, 6, 7, 8, 9, 10],
}

# Step 2: Define the BFS pathfinding algorithm
def find_path(start, goal, graph):
    """
    Finds the shortest path from start node to goal node using Breadth-First Search.
    Returns the path as a list of nodes, or None if no path exists.
    """
    if start == goal:
        return [start]

    queue = [[start]]
    visited = {start}

    while queue:
        path = queue.pop(0)
        current_node = path[-1]

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)

                if neighbor == goal:
                    return new_path

                visited.add(neighbor)
                queue.append(new_path)

    return None

# Step 3: Display available states and collect user inputs
print("All states:", states)
initial_state = int(input("Enter Initial State: "))
goal_state = int(input("Enter Goal State: "))
battery = int(input("Enter current battery %: "))

print(f"Selected Path Range: From {initial_state} to {goal_state}")

# Step 4: Verify battery constraint before navigation
if battery < 20:
    print("Warning: Battery low! Going to charging section.")
else:
    # Step 5: Validate that initial and goal states are within the valid state space
    if initial_state in states and goal_state in states:
        # Step 6: Execute BFS to find a valid path
        result_path = find_path(initial_state, goal_state, paths)
        if result_path:
            print("Path found:", " -> ".join(map(str, result_path)))
        else:
            print("Not possible: No valid path exists between these states.")
    else:
        print("Not possible: Invalid state entered.")
