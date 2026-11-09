# ==========================================
# Problem 16: Smart Hospital Knowledge Base & Forward Chaining Engine
# Description: Implements a forward-chaining inference engine using propositional
#              rules and fact sets to infer hospital emergency responses.
# ==========================================

# Step 1: Define the SmartHospital class with fact and rule bases
class SmartHospital:
    def __init__(self):
        """Initialize the initial known facts and production rules."""
        # Known baseline patient facts
        self.facts = {
            "PatientCondition_critical",
            "Temperature_high",
            "OxygenLevel_low",
            "Doctor_available"
        }

        # Knowledge Base Rules: (Antecedent Conditions Set, Consequent Conclusion)
        self.rules = [
            ({"PatientCondition_critical"}, "Nurse_notified"),
            ({"Temperature_high", "OxygenLevel_low"}, "EmergencyAlert_activated"),
            ({"PatientCondition_critical", "Doctor_available"}, "Doctor_notified"),
            ({"Nurse_notified", "Doctor_notified"}, "EmergencyTeam_Alerted")
        ]

    # Step 2: Forward Chaining Inference Engine
    def forward_chaining(self):
        """
        Applies forward chaining to repeatedly evaluate rules against current facts
        until no new conclusions can be derived (fixed-point iteration).
        """
        print("\n--- Running Forward Chaining ---")
        changed = True
        while changed:
            changed = False
            for conditions, conclusion in self.rules:
                # If all antecedents of the rule are satisfied in current facts
                if conditions.issubset(self.facts):
                    # If conclusion has not already been derived
                    if conclusion not in self.facts:
                        self.facts.add(conclusion)
                        print("New conclusion derived:", conclusion)
                        changed = True  # Trigger another iteration to find dependent conclusions

    # Step 3: Display all final facts and conclusions
    def display_results(self):
        """Display all initial and derived facts in alphabetical order."""
        print("\nFinal Facts and Conclusions:")
        for fact in sorted(self.facts):
            print(" -", fact)


# Step 4: Main program execution
if __name__ == "__main__":
    # Instantiate the smart hospital expert system
    hospital = SmartHospital()

    # Step 5: Display initial facts before inference
    print("Initial Facts:")
    for fact in sorted(hospital.facts):
        print(" -", fact)

    # Step 6: Execute forward chaining inference
    hospital.forward_chaining()

    # Step 7: Display final deduced state
    hospital.display_results()
