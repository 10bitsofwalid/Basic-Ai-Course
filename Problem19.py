class Security_System:
    def __init__(self, motion_detected, door_open, alarm_activated, camera_activated, guard_notified, team_responded):
        self.motion_detected = motion_detected
        self.door_open = door_open
        self.camera_activated = camera_activated
        self.alarm_activated = alarm_activated
        self.guard_notified = guard_notified
        self.team_responded = team_responded

    def rules(self):
        if self.motion_detected:
            self.camera_activated = True
        if self.camera_activated and self.door_open:
            self.alarm_activated= True
        if self.alarm_activated:
            self.guard_notified= True
        if self.guard_notified:
            self.team_responded = True

    def decision(self):
        if self.motion_detected and self.door_open and self.alarm_activated:
            print("High Priority Security Response Required.")
        elif (self.motion_detected and self.door_open and not self.alarm_activated):
            print("Generate a security alert and investigate the alarm failure")
        elif self.motion_detected and not self.door_open:
            print("Activate the camera and monitor the area")
        else:
            print("No motion-related security action is required")

    def display(self):
        print("Motion Detected:", self.motion_detected)
        print("Camera Activated:", self.camera_activated)
        print("Door Open:", self.door_open)
        print("Security Alarm Activated:", self.alarm_activated)
        print("Security Guard Notified:", self.guard_notified)
        print("Security Team Responded:", self.team_responded)

        print("\nDecision:")
        self.decision()

print("\nSystem 1")
system1 = Security_System(True, False, True, False, True, True)
system1.rules()
system1.display()

print("\nSystem 02")
system2 = Security_System(False, True, True, True, True, False)
system2.rules()
system2.display()

print("\nSystem 03")
system2 = Security_System(True, True, True, True, True, False)
system2.rules()
system2.display()

print("\nSystem 04")
system2 = Security_System(False, False, False, True, False, False)
system2.rules()
system2.display()