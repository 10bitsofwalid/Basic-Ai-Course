initial_state = 0
goal_state = 10
battery = int(input("Enter current battery %: "))

print(f"Valid states are from {initial_state} to {goal_state}.")

if battery < 20:
    print("Warning: Battery low! Going to charging section.")
else:
    input_count = 0
    path = []

    while True:
        user_input = input("Enter Your current state: ")
        input_count += 1

        if not user_input.isdigit():
            print("Invalid state.")
            continue

        current_state = int(user_input)

        if current_state < initial_state or current_state > goal_state:
            print("Invalid state.")
            continue

        print("Valid state.")
        path.append(current_state)

        if current_state == goal_state:
            print(f"Path: {path}")
            print(f"Reached goal state successfully in {input_count} inputs!")
            break
        else:
            print(f"Path: {path}")
            print("Not reached yet. Need to go farther.\n")