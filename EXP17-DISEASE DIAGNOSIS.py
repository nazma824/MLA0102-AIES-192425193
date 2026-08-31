# Medical Expert System
# Rule-Based Disease Inference

# Knowledge Base: Disease -> Symptoms
rules = {
    "Flu": ["fever", "cough", "body_pain", "fatigue"],

    "Common Cold": ["cough", "runny_nose", "sneezing", "sore_throat"],

    "Malaria": ["fever", "chills", "sweating", "headache"],

    "Dengue": ["high_fever", "severe_headache", "joint_pain", "skin_rash"],

    "Diabetes": [
        "frequent_urination",
        "excessive_thirst",
        "increased_hunger",
        "weight_loss"
    ],

    "Hypertension": [
        "high_blood_pressure",
        "headache",
        "dizziness",
        "blurred_vision"
    ]
}


# Function to infer disease
def diagnose(patient_symptoms):

    disease_scores = {}

    for disease, symptoms in rules.items():

        # Count how many symptoms match
        matched = set(patient_symptoms) & set(symptoms)

        if len(matched) > 0:
            disease_scores[disease] = len(matched)

    # No matching disease
    if not disease_scores:
        return None

    # Find the disease with maximum matching symptoms
    max_score = max(disease_scores.values())

    possible_diseases = []

    for disease, score in disease_scores.items():
        if score == max_score:
            possible_diseases.append((disease, score))

    return possible_diseases


# Main program
print("==========================================")
print("       MEDICAL EXPERT SYSTEM")
print("==========================================")

print("\nEnter symptoms separated by commas.")
print("You do NOT need to enter all symptoms.")

print("\nExample:")
print("fever, cough")
print("or")
print("frequent_urination, excessive_thirst")

user_input = input("\nEnter patient symptoms: ")

# Convert input into a list
patient_symptoms = [
    symptom.strip().lower()
    for symptom in user_input.split(",")
]

# Diagnose
result = diagnose(patient_symptoms)


# Display result
print("\n==========================================")
print("              DIAGNOSIS")
print("==========================================")

if result:

    for disease, score in result:
        print("Possible Disease :", disease)
        print("Matching Symptoms:", score)

else:
    print("No matching disease found.")

print("\nDiagnosis completed.")
