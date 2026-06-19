Titanic Survival Prediction using Decision Tree Classifier

📌 Project Overview

This project implements a Decision Tree Classification Algorithm to predict whether a passenger survived the Titanic disaster based on passenger information such as class, gender, age, and fare.
The project demonstrates the complete machine learning workflow, including data preprocessing, feature selection, model training, prediction, evaluation, and visualization.

🎯 Objective

To build a classification model capable of predicting passenger survival using historical Titanic passenger data.

📊 Dataset Information

The dataset contains information about Titanic passengers, including:
Passenger Class (Pclass)
Gender (Sex)
Age
Fare
Survival Status (Target Variable)
Target Variable
Value	Meaning
0	Did Not Survive
1	Survived

🛠 Technologies Used

Python
Pandas
Matplotlib
Scikit-Learn

📋 Project Workflow

1. Data Collection
Loaded the Titanic dataset using Pandas.

2. Data Preprocessing
Handled missing values
Selected important features
Converted categorical values into numerical format
Example:
Male → 0
Female → 1


3. Feature Selection
Selected the following features:
Pclass
Sex
Age
Fare
These features were used to predict survival.

4. Train-Test Split
The dataset was divided into:
80% Training Data
20% Testing Data
This allows the model to learn from one portion of the data and be evaluated on unseen data.

5. Model Building
Created a Decision Tree Classifier using Scikit-Learn.

6. Model Training
Trained the model using the training dataset.

7. Prediction
Predicted passenger survival on the testing dataset.

8. Model Evaluation
Evaluated model performance using:

Accuracy Score
Classification Report
Confusion Matrix

9. Decision Tree Visualization
Visualized the decision-making process of the model using a Decision Tree diagram.

🌳 What is a Decision Tree?

A Decision Tree is a supervised machine learning algorithm that makes decisions using a tree-like structure.
It works by asking a sequence of questions and splitting the data into smaller groups until a prediction can be made.

Example:
Gender = Female?

├── Yes → Higher chance of survival

└── No

    Age < 10?

    ├── Yes → Survived

    └── No → Not Survived

📈 Results

The model successfully learned patterns from passenger data and predicted survival outcomes with good accuracy.
The visualization clearly shows how the Decision Tree makes decisions based on different passenger attributes.

🎓 Learning Outcomes

Through this project, I learned:

Supervised Machine Learning
Classification Algorithms
Decision Tree Classifier
Data Preprocessing
Handling Missing Values
Feature Selection
Train-Test Split
Model Evaluation
Accuracy Measurement
Decision Tree Visualization

🚀 Future Improvements

Hyperparameter Tuning
Random Forest Implementation
Feature Engineering
Cross Validation
Comparison with other Classification Algorithms


👩‍💻 Author

E. Logeswari
B.E. Robotics and Automation
Machine Learning Internship Project
