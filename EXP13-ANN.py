# 1. Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression

# 2. Load the dataset
data = pd.read_csv("diabetes_data.csv")

# 3. Display dataset
print("First 5 rows:")
print(data.head())

# 4. Dataset information
print("\nDataset shape:")
print(data.shape)

print("\nDataset information:")
print(data.info())

print("\nMissing values:")
print(data.isnull().sum())

# 5. Separate input and output
X = data.drop("Outcome", axis=1)
y = data["Outcome"]

print("\nInput columns:")
print(X.columns)

print("\nOutput column:")
print(y.name)

# 6. Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 7. Standardize the input data
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 8. Train the model
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# 9. Make predictions
y_pred = model.predict(X_test)

# 10. Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)
print("Accuracy percentage:", accuracy * 100, "%")

# 11. Confusion matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# 12. Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 13. Predict a new patient's outcome
new_patient = np.array([[2, 120, 70, 25, 100, 30.5, 0.45, 35]])

new_patient_scaled = scaler.transform(new_patient)

prediction = model.predict(new_patient_scaled)

if prediction[0] == 1:
    print("\nPrediction: Diabetic")
else:
    print("\nPrediction: Not Diabetic")
