# Vehicle Fault Diagnosis - AT2 Q4

# Facts
facts = {
    "DoesNotStart(Car101)",
    "DimHeadlights(Car101)"
}

# Rules
rules = [
    ("BatteryProblem(Car101)",
     {"DoesNotStart(Car101)", "DimHeadlights(Car101)"}),

    ("BatteryInspection(Car101)",
     {"BatteryProblem(Car101)"}),

    ("MarkForService(Car101)",
     {"BatteryInspection(Car101)"})
]

# Forward Chaining
print("===== VEHICLE FAULT DIAGNOSIS =====")
print("\nInitial Facts:")

for fact in facts:
    print("-", fact)

print("\nInference:")

changed = True

while changed:
    changed = False

    for conclusion, conditions in rules:
        if conditions.issubset(facts) and conclusion not in facts:
            facts.add(conclusion)
            print("=>", conclusion)
            changed = True

# Final Output
print("\n===== FINAL RESULT =====")

if "BatteryProblem(Car101)" in facts:
    print("Car101 has a battery problem.")

if "BatteryInspection(Car101)" in facts:
    print("Car101 requires battery inspection.")

if "MarkForService(Car101)" in facts:
    print("Car101 should be marked for service.")
