import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# ------------------- DATA -------------------

columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
df = pd.read_csv("Programs/car.data", names=columns)

# One-Hot Encoding (convert categorical features into dummy variables)
df_encoded = pd.get_dummies(df, columns=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety'])

print("One-Hot Encoded Data Sample:\n", df_encoded.head())

# Features and Target
X = df_encoded.drop(columns=['class'])
y = df['class']   # keep target labels as original

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ------------------- MODEL TRAINING -------------------

model = LogisticRegression(max_iter=1000, solver='lbfgs', multi_class='multinomial')
model.fit(X_train, y_train)

# ------------------- EVALUATION -------------------

y_pred = model.predict(X_test)

print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, cmap="Blues", fmt="d", xticklabels=model.classes_, yticklabels=model.classes_)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Car Evaluation (Logistic Regression + One-Hot Encoding)")
plt.show()

# ------------------- USER INPUT PREDICTION -------------------

print("\n--- Car Evaluation Prediction ---")

buying = input("Enter buying value (vhigh, high, med, low): ")
maint = input("Enter maint value (vhigh, high, med, low): ")
doors = input("Enter number of doors (2, 3, 4, 5more): ")
persons = input("Enter persons (2, 4, more): ")
lug_boot = input("Enter lug_boot size (small, med, big): ")
safety = input("Enter safety level (low, med, high): ")

user_data = pd.DataFrame([{
    "buying": buying,
    "maint": maint,
    "doors": doors,
    "persons": persons,
    "lug_boot": lug_boot,
    "safety": safety
}])

# One-hot encode user input
user_data_encoded = pd.get_dummies(user_data)

# Match training columns
user_data_encoded = user_data_encoded.reindex(columns=X.columns, fill_value=0)

# Predict
prediction = model.predict(user_data_encoded)[0]
print(f"\n Prediction: The car is classified as '{prediction}'")
