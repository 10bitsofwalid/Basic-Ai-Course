class SmartHospital:
    def __init__(self):
        self.facts = set()
        self.rules = [
            ({"PatientCondition_critical"}, "Nurse_notified"),
            ({"Temperature_high", "OxygenLevel_low"}, "EmergencyAlert_activated"),
            ({"PatientCondition_critical", "Doctor_available"}, "Doctor_notified"),
            ({"Nurse_notified", "Doctor_notified"}, "EmergencyTeam_Alert")
        ]

    def get_input(self):
        print("Enter Patient Information:")
        condition = input("Is patient critical? (yes/no): ").strip().lower()
        temperature = input("Is temperature high? (yes/no): ").strip().lower()
        oxygen = input("Is oxygen level low? (yes/no): ").strip().lower()
        doctor = input("Is doctor available? (yes/no): ").strip().lower()

        if condition == "yes":
            self.facts.add("PatientCondition_critical")
        if temperature == "yes":
            self.facts.add("Temperature_high")
        if oxygen == "yes":
            self.facts.add("OxygenLevel_low")
        if doctor == "yes":
            self.facts.add("Doctor_available")

    def forward_chaining(self):
        changed = True
        while changed:
            changed = False
            for conditions, conclusion in self.rules:
                if conditions.issubset(self.facts):
                    if conclusion not in self.facts:
                        self.facts.add(conclusion)
                        print("New conclusion:", conclusion)
                        changed = True

    def make_decision(self):
        print("\n--- Decisions & Final Actions ---")

        is_critical = "PatientCondition_critical" in self.facts
        is_oxygen_low = "OxygenLevel_low" in self.facts
        is_emergency_alert = "EmergencyAlert_activated" in self.facts
        is_doctor_available = "Doctor_available" in self.facts
        is_high_temp = "Temperature_high" in self.facts

        if is_critical and is_oxygen_low and is_emergency_alert:
            print("Decision 1: Immediate emergency response required.")

        elif is_critical and is_doctor_available and not is_oxygen_low:
            print("Decision 2: Urgent doctor review required.")

        elif is_critical and not is_doctor_available:
            print("Decision 3: Notify the nurse and escalate the case to the emergency team.")

        elif is_high_temp and not is_critical:
            print("Decision 4: Monitor the patient and arrange a medical assessment.")

        elif not is_critical and not is_high_temp:
            print("Decision 5: No emergency condition identified by these rules.")

        else:
            print("No specific decision rule matched the current state.")

    def display_results(self):
        print("\nFinal Facts and Conclusions:")
        for fact in sorted(self.facts):
            print(fact)

if __name__ == "__main__":
    hospital = SmartHospital()
    hospital.get_input()
    print("\nInitial Facts:", hospital.facts)
    print("\nForward Chaining Results:")
    hospital.forward_chaining()
    hospital.make_decision()
    hospital.display_results()
