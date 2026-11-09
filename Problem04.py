# ==========================================
# Problem 04: Interactive State Space Navigation with Battery Monitor
# Description: Simulates an agent navigating through states (0 to 10)
#              towards a goal state while checking battery constraints.
# ==========================================

# Step 1: Define initial and goal states for the navigation environment
initial_state = 0
goal_state = 10

# Step 2: Receive the current battery percentage from the user
battery = int(input("Enter current battery %: "))

print(f"Valid states are from {initial_state} to {goal_state}.")

# Step 3: Check battery level constraint before starting navigation
if battery < 20:
    # Battery below 20% is critically low; agent cannot continue
    print("Warning: Battery low! Going to charging section.")
else:
    # Step 4: Initialize state tracking variables
    input_count = 0
    path = []

    # Step 5: Begin interactive state transition loop
    while True:
        user_input = input("Enter Your current state: ").strip()
        input_count += 1

        # Step 5.1: Validate that input is numeric
        if not user_input.isdigit():
            print("Invalid state. Please enter a valid non-negative integer.")
            continue

        current_state = int(user_input)

        # Step 5.2: Check that current state falls within the allowed environment range
        if current_state < initial_state or current_state > goal_state:
            print(f"Invalid state. Must be between {initial_state} and {goal_state}.")
            continue

        print("Valid state.")
        # Step 5.3: Record valid state in the visited path
        path.append(current_state)

        # Step 5.4: Check whether the agent has reached the goal state
        if current_state == goal_state:
            print(f"Path: {path}")
            print(f"Reached goal state successfully in {input_count} inputs!")
            break
        else:
            print(f"Path: {path}")
            print("Not reached yet. Need to go farther.\n")
