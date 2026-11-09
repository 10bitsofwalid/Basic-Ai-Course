# ==========================================
# Problem 15: Security Expert System with Forward Reasoning (OOP)
# Description: Models a physical security system that applies logical inference rules
#              to deduce actions (camera, alarm, guard, team) and make decisions.
# ==========================================

# Step 1: Define the SecuritySystem class
class SecuritySystem:
    def __init__(self, motion, door_open, alarm):
        """Initialize known initial facts of the security environment."""
        self.motion = motion
        self.door_open = door_open
        self.alarm = alarm

        # Deduced internal states
        self.camera = False
        self.guard_notified = False
        self.team_responds = False

    # Step 2: Rule sub-routine to activate camera if motion is detected
    def activate_camera(self):
        """Rule 1: If motion detected -> Activate camera."""
        if self.motion:
            self.camera = True

    # Step 3: Forward chaining rule application
    def apply_rules(self):
        """Apply sequential inference rules to update system state."""
        # Rule 1: Motion activates camera
        self.activate_camera()

        # Rule 2: If camera is active and door is open -> Trigger alarm
        if self.camera and self.door_open:
            self.alarm = True

        # Rule 3: If alarm is triggered -> Notify security guard
        if self.alarm:
            self.guard_notified = True

        # Rule 4: If guard is notified -> Security response team responds
        if self.guard_notified:
            self.team_responds = True

    # Step 4: Decision-making logic based on inferred facts
    def make_decision(self):
        """Synthesize overall security decision based on fact state."""
        print("\n--- Security Decision ---")

        if self.motion and self.door_open and self.alarm:
            print("Decision: High-priority security response required.")
        elif self.motion and self.door_open and not self.alarm:
            print("Decision: Generate a security alert and investigate alarm failure.")
        elif self.motion and not self.door_open:
            print("Decision: Activate the camera and monitor the area.")
        else:
            print("Decision: No motion-related security action is required.")

    # Step 5: Report current and deduced facts
    def display_facts(self):
        """Display summary of all facts in the knowledge base."""
        print("\n--- Security Facts ---")
        print("Motion detected:       ", self.motion)
        print("Door is open:          ", self.door_open)
        print("Camera activated:      ", self.camera)
        print("Alarm activated:       ", self.alarm)
        print("Security guard notified:", self.guard_notified)
        print("Security team responds: ", self.team_responds)


# Step 6: Collect sensor inputs from the user
print("Enter Security Sensor Inputs:")
motion = input("Is motion detected? (yes/no): ").strip().lower() == "yes"
door_open = input("Is the door open? (yes/no): ").strip().lower() == "yes"
alarm = input("Is the alarm activated? (yes/no): ").strip().lower() == "yes"

# Step 7: Instantiate SecuritySystem with initial sensor facts
security = SecuritySystem(motion, door_open, alarm)

# Step 8: Apply reasoning rules, evaluate decisions, and display results
security.apply_rules()
security.make_decision()
security.display_facts()
