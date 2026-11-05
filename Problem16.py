class SmartHospital:
    def __init__(self):
        self.facts = {
        "PatientCondition_critical",
        "Temperature_high",
        "OxygenLevel_low",
        "Doctor_available"
        }


for conditions, conclusion in self.rules:
    if conditions.issubset(self.facts):
        if conclusion not in self.facts:
            self.facts.add(conclusion)
print("New conclusion:", conclusion)
changed = True

def display_results(self):
    print("\nFinal Facts and Conclusions:")
    for fact in sorted(self.facts):
        print(fact)


# Main program
hospital = SmartHospital()

print("Initial Facts:")
print(hospital.facts)

hospital.forward_chaining()
hospital.display_results()