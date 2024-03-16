class MedicalAgent:
    def __init__(self):
        # defining all known diseases, tests, symptoms, etc.
        self.rules = {
            "Acute appendicitis": {
                "Symptoms": ["Fever", "Pain in Abdomen especially ILIAC FOSSA", "Vomiting"],
                "Tests": ["High TLC", "High Neutrophils", "High ESR"],
                "Action": "Surgery"
            },
            "Pneumonia": {
                "Symptoms": ["Fever", "Cough (with sputum)", "Pain in chest"],
                "Tests": ["High TLC", "High Neutrophils", "High ESR", "Pneumonic patch on X-ray"],
                "Action": "Antibiotics"
            }
        }

    def diagnose_disease(self, symptoms, tests):
        # can store multiple diseases if multiple diseases match symptoms, tests
        possible_diseases = []
        actions = set()

        for key, value in self.rules.items():
            if all(symptom in symptoms for symptom in value["Symptoms"]) and \
                    all(test in tests for test in value["Tests"]):
                actions = [value["Action"]]
                possible_diseases = [key]
                break
            elif any(symptom in symptoms for symptom in value["Symptoms"]) and \
                    any(test in tests for test in value["Tests"]):
                possible_diseases.append("Possibly " + key)
                actions.add("Tentatively " + value["Action"])

        if len(possible_diseases) > 0:
            diseases_str = ", ".join(possible_diseases)
            action_str = ", ".join(actions)
            return (diseases_str, action_str)
        else:
            return ("No matching disease found", "No action")


agent = MedicalAgent()
# symptoms = ["Fever", "Pain in Abdomen especially ILIAC FOSSA"]
# tests = ["High TLC", "High Neutrophils", "High ESR"]
# symptoms = ["Fever", "Pain in Abdomen especially ILIAC FOSSA", "Vomiting"]
# tests = ["High TLC", "High Neutrophils", "High ESR"]
symptoms = ["Fever", "Cough (with sputum)", "Pain in chest"]
tests = ["High TLC", "High Neutrophils", "High ESR", "Pneumonic patch on X-ray"]
diagnosis, action = agent.diagnose_disease(symptoms, tests)
print("Diagnosis:", diagnosis)
print("Action:", action)
