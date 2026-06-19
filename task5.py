# Import Libraries

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

df = pd.read_csv("Titanic-Dataset.csv")

# Display first 5 rows
print("First 5 Rows:\n")
print(df.head())

# --------------------------------------------------
# Dataset Information
# --------------------------------------------------

print("\nDataset Information:\n")
print(df.info())

# --------------------------------------------------
# Handle Missing Values
# --------------------------------------------------

df['Age'].fillna(df['Age'].mean(), inplace=True)

# --------------------------------------------------
# Convert Categorical Data
# --------------------------------------------------

df['Sex'] = df['Sex'].map({
    'male': 0,
    'female': 1
})

# --------------------------------------------------
# Feature Selection
# --------------------------------------------------

X = df[['Pclass', 'Sex', 'Age', 'Fare']]

y = df['Survived']

# --------------------------------------------------
# Split Dataset
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# --------------------------------------------------
# Create Decision Tree Model
# --------------------------------------------------

model = DecisionTreeClassifier(
    criterion='gini',
    max_depth=4,
    random_state=42
)

# --------------------------------------------------
# Train Model
# --------------------------------------------------

model.fit(X_train, y_train)

# --------------------------------------------------
# Prediction
# --------------------------------------------------

y_pred = model.predict(X_test)

# --------------------------------------------------
# Accuracy
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:")
print(accuracy)

# --------------------------------------------------
# Classification Report
# --------------------------------------------------

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# --------------------------------------------------
# Confusion Matrix
# --------------------------------------------------

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# --------------------------------------------------
# Visualize Decision Tree
# --------------------------------------------------

plt.figure(figsize=(15, 8))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=['Not Survived', 'Survived'],
    filled=True,
    rounded=True
)

plt.title("Titanic Survival Prediction - Decision Tree")

plt.show()