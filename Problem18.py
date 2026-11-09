# ==========================================
# Problem 18: Full Clinical Decision Support System (Interactive Forward Chaining)
# Description: Takes patient assessment inputs from the user, applies forward-chaining
#              rules to deduce internal state facts, and outputs medical emergency decisions.
# ==========================================

# Step 1: Define the SmartHospital class with knowledge base rules
class SmartHospital:
    def __init__(self):
        """Initialize empty facts set and define domain production rules."""
        self.facts = set()

        # Knowledge Base: (Set of Antecedents, Inferred Consequent)
        self.rules = [
            ({"PatientCondition_critical"}, "Nurse_notified"),
            ({"Temperature_high", "OxygenLevel_low"}, "EmergencyAlert_activated"),
            ({"PatientCondition_critical", "Doctor_available"}, "Doctor_notified"),
            ({"Nurse_notified", "Doctor_notified"}, "EmergencyTeam_Alert")
        ]

    # Step 2: Interactive input method to acquire clinical observations
    def get_input(self):
        """Prompt user for current patient observations and update facts set."""
        print("Enter Patient Information:")
        condition = input("Is patient critical? (yes/no): ").strip().lower()
        temperature = input("Is temperature high? (yes/no): ").strip().lower()
        oxygen = input("Is oxygen level low? (yes/no): ").strip().lower()
        doctor = input("Is doctor available? (yes/no): ").strip().lower()

        # Assert initial facts based on positive user responses
        if condition == "yes":
            self.facts.add("PatientCondition_critical")
        if temperature == "yes":
            self.facts.add("Temperature_high")
        if oxygen == "yes":
            self.facts.add("OxygenLevel_low")
        if doctor == "yes":
            self.facts.add("Doctor_available")

    # Step 3: Forward Chaining Engine
    def forward_chaining(self):
        """
        Iteratively fires matching production rules until fixed point is reached.
        Deduces intermediate and high-level medical state facts.
        """
        changed = True
        while changed:
            changed = False
            for conditions, conclusion in self.rules:
                # If all premise conditions are currently asserted
                if conditions.issubset(self.facts):
                    # If this is a new derived conclusion
                    if conclusion not in self.facts:
                        self.facts.add(conclusion)
                        print("New conclusion derived:", conclusion)
                        changed = True

    # Step 4: Medical Decision Making based on accumulated facts
    def make_decision(self):
        """Evaluate final set of facts against decision protocols."""
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

    # Step 5: Report all facts and derived conclusions
    def display_results(self):
        """Display summary of all facts in the knowledge base."""
        print("\nFinal Facts and Conclusions:")
        for fact in sorted(self.facts):
            print(" -", fact)


# Step 6: Main application execution flow
if __name__ == "__main__":
    # Instantiate clinical expert system
    hospital = SmartHospital()

    # Step 6.1: Collect patient clinical findings
    hospital.get_input()
    print("\nInitial Facts:", hospital.facts)

    # Step 6.2: Infer facts using forward chaining
    print("\nForward Chaining Results:")
    hospital.forward_chaining()

    # Step 6.3: Determine clinical actions
    hospital.make_decision()

    # Step 6.4: Print final state summary
    hospital.display_results()
