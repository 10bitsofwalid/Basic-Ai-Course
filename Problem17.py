class HospitalSystem:
    def __init__(self):
        self.facts = {
            "PatientCondition_critical",
            "Temperature_high",
            "OxygenLevel_low",
            "Doctor_available",
            "Doctor_notified",
        }
        self.rules = [
            ({"PatientCondition_critical"}, "Nurse_notified"),
                ({"Temperature_high", "OxygenLevel_low"},"EmergencyAlert_activated"),
                ({"PatientCondition_critical", "Doctor_available"},"Doctor_notified"),
                    ({"Nurse_notified", "Doctor_notified"},"EmergencyTeam_alerted")
                    ]
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
def display_results(self):
    print("\nFinal Facts and Conclusions:")
    for fact in sorted(self.facts):
        print(fact)

        hospital = SmartHospital()

    print("Initial Facts:")
    print(hospital.facts)

    hospital.forward_chaining()
    hospital.display_results()
