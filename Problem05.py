states = ["S0","S1", "S2", "S3", "S4", "S5", "S6","S7","S8","S9","S10"]
print("Available states:", states)

start_state = input("Enter start state: ").strip()
end_state = input("Enter end state: ").strip()

if start_state not in states or end_state not in states:
    print("Invalid states entered")
else:
    start_idx = states.index(start_state)
    end_idx = states.index(end_state)

    if start_idx < end_idx:
        path_sequence = states[start_idx : end_idx + 1]
        print(f"Possible path: {' -> '.join(path_sequence)}")
    else:
        print("Not possible")