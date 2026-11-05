paths = {
    "1": ["A", "C", "H", "I"],
    "2": ["A", "D", "E", "F"],
    "3": ["A", "B", "C"]
}
initial_state = input("Enter Initial State: ").strip().upper()
goal_state = input("Enter Goal State: ").strip().upper()

path_found = False
for path_name, selected_path in paths.items():
    if initial_state in selected_path and goal_state in selected_path:
        initial_index = selected_path.index(initial_state)
        goal_index = selected_path.index(goal_state)

        if initial_index <= goal_index:
            print(f"Path '{path_name}' is possible. Sub-path: {' -> '.join(selected_path[initial_index : goal_index + 1])}")
            path_found = True
            break

if not path_found:
    print("No valid path found between the initial and goal states.")