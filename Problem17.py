# ==========================================
# Problem 17: Hospital Expert System with Pre-seeded Facts (OOP)
# Description: Demonstrates rule-based deduction starting from a pre-seeded set of facts
#              using a structured HospitalSystem class and forward chaining.
# ==========================================

# Step 1: Define the HospitalSystem class
class HospitalSystem:
    def __init__(self):
        """Initialize initial fact base and domain knowledge rules."""
        # Initial set of observed facts
        self.facts = {
            "PatientCondition_critical",
            "Temperature_high",
            "OxygenLevel_low",
            "Doctor_available",
            "Doctor_notified",
        }

        # Knowledge Base: Production Rules
        self.rules = [
            ({"PatientCondition_critical"}, "Nurse_notified"),
            ({"Temperature_high", "OxygenLevel_low"}, "EmergencyAlert_activated"),
            ({"PatientCondition_critical", "Doctor_available"}, "Doctor_notified"),
            ({"Nurse_notified", "Doctor_notified"}, "EmergencyTeam_alerted")
        ]

    # Step 2: Forward Chaining Engine (Fixed indentation and loop structure)
    def forward_chaining(self):
        """
        Derives new conclusions by firing rules whose antecedent conditions are met.
        Repeats until no new facts can be deduced.
        """
        print("\n--- Running Forward Chaining ---")
        changed = True
        while changed:
            changed = False
            for conditions, conclusion in self.rules:
                # Check if all prerequisite conditions exist in known facts
                if conditions.issubset(self.facts):
                    # Check if conclusion is already known
                    if conclusion not in self.facts:
                        self.facts.add(conclusion)
                        print("New conclusion derived:", conclusion)
                        changed = True

    # Step 3: Method to print all accumulated facts
    def display_results(self):
        """Displays sorted list of all active facts in the system."""
        print("\nFinal Facts and Conclusions:")
        for fact in sorted(self.facts):
            print(" -", fact)


# Backward compatibility alias
SmartHospital = HospitalSystem

# Step 4: Main program execution (Moved out of display_results method)
if __name__ == "__main__":
    # Instantiate the hospital reasoning system
    hospital = HospitalSystem()

    # Step 5: Display initial known facts
    print("Initial Facts:")
    for fact in sorted(hospital.facts):
        print(" -", fact)

    # Step 6: Perform forward chaining inference
    hospital.forward_chaining()

    # Step 7: Display final deduced conclusions
    hospital.display_results()
