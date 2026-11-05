states = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("All states:", states)

paths = {
    0: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    1: [2, 3, 4, 5, 6, 7, 8, 9, 10],
    2: [3, 4, 5, 6, 7, 8, 9, 10],
}

initial_state = int(input("Enter Initial State: "))
goal_state = int(input("Enter Goal State: "))
battery = int(input("Enter current battery %: "))

print(f"Selected Path Range: From {initial_state} to {goal_state}")

if battery < 20:
    print("Warning: Battery low! Going to charging section.")

def find_path(start, goal, graph):
    queue = [[start]]
    visited = set()

    if start == goal:
        return [start]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == goal:
                    return new_path
    return None
if initial_state in states and goal_state in states:
    result_path = find_path(initial_state, goal_state, paths)
    if result_path:
        print("Path found:", " -> ".join(map(str, result_path)))
    else:
        print("Not possible: No valid path exists between these states.")
else:
    print("Not possible: Invalid state entered.")
