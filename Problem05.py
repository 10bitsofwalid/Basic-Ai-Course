# ==========================================
# Problem 05: Linear State Space Sequential Path Finder
# Description: Checks if a forward sequential path exists between two named
#              states (e.g., S0 to S10) and prints the transition path.
# ==========================================

# Step 1: Define the available ordered sequence of states
states = ["S0", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]
print("Available states:", states)

# Step 2: Prompt user for the start and end states (convert to uppercase for robustness)
start_state = input("Enter start state: ").strip().upper()
end_state = input("Enter end state: ").strip().upper()

# Step 3: Validate that both entered states exist in the predefined state list
if start_state not in states or end_state not in states:
    print("Invalid states entered. Both states must belong to the available list.")
else:
    # Step 4: Determine the index positions of start and end states
    start_idx = states.index(start_state)
    end_idx = states.index(end_state)

    # Step 5: Verify that transition is forward-moving (start comes before or at end)
    if start_idx <= end_idx:
        # Step 6: Slice the path from start to end (inclusive) and print formatted route
        path_sequence = states[start_idx : end_idx + 1]
        print(f"Possible path: {' -> '.join(path_sequence)}")
    else:
        # Backward transitions are not permitted in this forward sequence
        print("Not possible: End state occurs before start state in the linear sequence.")
