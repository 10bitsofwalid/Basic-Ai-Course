class SecuritySystem:
    def __init__(self, motion, door_open, alarm):
        self.motion = motion
        self.door_open = door_open
        self.alarm = alarm

        self.camera = False
        self.guard_notified = False
        self.team_responds = False

    def activate_camera(self):
        if self.motion:
            self.camera = True

    def apply_rules(self):
        self.activate_camera()

        if self.camera and self.door_open:
            self.alarm = True

        if self.alarm:
            self.guard_notified = True


        if self.guard_notified:
            self.team_responds = True

    def make_decision(self):
        print("\n--- Security Decision ---")

        if self.motion and self.door_open and self.alarm:
            print("High-priority security response required.")
        elif self.motion and self.door_open and not self.alarm:
            print("Generate a security alert and investigate alarm failure.")
        elif self.motion and not self.door_open:
            print("Activate the camera and monitor the area.")
        else:
            print("No motion-related security action is required.")

    def display_facts(self):
        print("\n--- Security Facts ---")
        print("Motion detected:", self.motion)
        print("Door is open:", self.door_open)
        print("Camera activated:", self.camera)
        print("Alarm activated:", self.alarm)
        print("Security guard notified:", self.guard_notified)
        print("Security team responds:", self.team_responds)

motion = input("Is motion detected? (yes/no): ").lower() == "yes"
door_open = input("Is the door open? (yes/no): ").lower() == "yes"
alarm = input("Is the alarm activated? (yes/no): ").lower() == "yes"

security = SecuritySystem(motion, door_open, alarm)

security.apply_rules()
security.make_decision()
security.display_facts()