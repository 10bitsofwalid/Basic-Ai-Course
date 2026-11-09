# ==========================================
# Problem 07: Multi-Route Sub-Path Finder
# Description: Searches across multiple predefined routes to locate
#              a valid sequential path between an initial and a goal state.
# ==========================================

# Step 1: Predefine available routes in a dictionary mapping route IDs to state lists
paths = {
    "1": ["A", "C", "H", "I"],
    "2": ["A", "D", "E", "F"],
    "3": ["A", "B", "C"]
}

# Step 2: Get initial and goal states from the user, normalizing to uppercase
initial_state = input("Enter Initial State: ").strip().upper()
goal_state = input("Enter Goal State: ").strip().upper()

# Step 3: Iterate through all available routes to search for a viable transition
path_found = False
for path_name, selected_path in paths.items():
    # Step 3.1: Check if both start and goal nodes belong to this specific route
    if initial_state in selected_path and goal_state in selected_path:
        initial_index = selected_path.index(initial_state)
        goal_index = selected_path.index(goal_state)

        # Step 3.2: Verify that start node appears before or at goal node (forward direction)
        if initial_index <= goal_index:
            sub_path = selected_path[initial_index : goal_index + 1]
            print(f"Path '{path_name}' is possible. Sub-path: {' -> '.join(sub_path)}")
            path_found = True
            break

# Step 4: If no route satisfies the start-to-goal condition, inform the user
if not path_found:
    print("No valid path found between the initial and goal states.")
