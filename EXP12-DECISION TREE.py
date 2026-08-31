# Decision Tree Classifier - Pure Python

# Dataset
# [Age, Income, Credit Score]
X = [
    [25, 30000, 600],
    [35, 50000, 700],
    [45, 80000, 750],
    [23, 25000, 580],
    [40, 60000, 720],
    [30, 40000, 650],
    [50, 90000, 780],
    [28, 35000, 620],
    [38, 55000, 710],
    [55, 95000, 800]
]

# 1 = Approved, 0 = Rejected
Y = [0, 1, 1, 0, 1, 0, 1, 0, 1, 1]

# Simple decision rules
def predict(age, income, credit):
    if credit >= 700:
        return "APPROVED"
    elif income >= 50000 and credit >= 650:
        return "APPROVED"
    else:
        return "REJECTED"

# Display training data
print("Loan Training Data")
print("------------------")

for i in range(len(X)):
    status = "Approved" if Y[i] == 1 else "Rejected"
    print(X[i], "->", status)

# Test new customer
print("\nNew Loan Application")
print("--------------------")

age = 32
income = 45000
credit = 680

print("Age:", age)
print("Income:", income)
print("Credit Score:", credit)

result = predict(age, income, credit)

print("Loan Status:", result)
