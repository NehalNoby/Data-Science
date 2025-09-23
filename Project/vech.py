import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# ------------------- DATA -------------------

# Load dataset
df = pd.read_csv("Project/Vehicle_Insurance.csv")
print("Original Data Sample:\n", df.head())
print("\nMissing Values:\n", df.isnull().sum())

# One-Hot Encoding categorical columns
categorical_cols = ["Gender", "Vehicle_Age", "Vehicle_Damage"]
df_encoded = pd.get_dummies(df, columns=categorical_cols)

print("\nAfter Encoding:\n", df_encoded.head())

# Features and Target
X = df_encoded.drop(columns=['Response'])   # Response = target (insurance or not)
y = df['Response']  # keep target as original (0 = No, 1 = Yes)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ------------------- MODEL TRAINING -------------------

model = LogisticRegression(max_iter=1000, solver='lbfgs')
model.fit(X_train, y_train)

# ------------------- EVALUATION -------------------

y_pred = model.predict(X_test)

print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, cmap="Blues", fmt="d", xticklabels=model.classes_, yticklabels=model.classes_)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Vehicle Insurance Prediction")
plt.show()

# ------------------- USER INPUT PREDICTION -------------------

print("\n--- Vehicle Insurance Prediction ---")

gender = input("Enter Gender (Male/Female): ")
age = int(input("Enter Age: "))
driving_license = int(input("Driving License (1=Yes, 0=No): "))
region_code = float(input("Enter Region Code: "))
previously_insured = int(input("Previously Insured (1=Yes, 0=No): "))
vehicle_age = input("Enter Vehicle Age (< 1 Year / 1-2 Year / > 2 Years): ")
vehicle_damage = input("Vehicle Damaged Before? (Yes/No): ")
annual_premium = float(input("Enter Annual Premium: "))
policy_sales_channel = float(input("Enter Policy Sales Channel: "))
vintage = int(input("Enter Vintage (days): "))

# Create user input DataFrame
user_data = pd.DataFrame([{
    "Gender": gender,
    "Age": age,
    "Driving_License": driving_license,
    "Region_Code": region_code,
    "Previously_Insured": previously_insured,
    "Vehicle_Age": vehicle_age,
    "Vehicle_Damage": vehicle_damage,
    "Annual_Premium": annual_premium,
    "Policy_Sales_Channel": policy_sales_channel,
    "Vintage": vintage
}])

# One-hot encode user input
user_data_encoded = pd.get_dummies(user_data)

# Match training columns
user_data_encoded = user_data_encoded.reindex(columns=X.columns, fill_value=0)

# Predict
prediction = model.predict(user_data_encoded)[0]
print(f"\n Prediction: The user will {'take' if prediction==1 else 'not take'} insurance.")
