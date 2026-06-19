## **TASK 5 – DECISION TREE CLASSIFIER**



1\. Aim



To build a Decision Tree Classification model that can predict a category based on input features.



Example:



\* Predict whether a passenger survived the Titanic disaster.

\* Output:



&#x20; \* Survived = Yes

&#x20; \* Survived = No



This is a Classification Problem because the output is a category, not a numerical value.





2\. What is a Decision Tree?



A Decision Tree is a supervised machine learning algorithm used for classification and prediction.



It works like a flowchart:



Example:



Passenger Age < 10?

│

├── Yes → Survived

│

└── No

│

├── Female → Survived

│

└── Male → Not Survived



The model asks questions and makes decisions step by step until it reaches a final prediction.







3\. Why Decision Tree?



Advantages:



1\. Easy to understand

2\. Easy to visualize

3\. Works with numerical and categorical data

4\. No need for feature scaling

5\. Good for beginners



Applications:



\* Medical diagnosis

\* Customer segmentation

\* Loan approval

\* Spam detection

\* Fraud detection

\* Survival prediction







4\. Dataset Used



Titanic Dataset



Features:



1\. Pclass



&#x20;  \* Passenger class

&#x20;  \* 1 = First Class

&#x20;  \* 2 = Second Class

&#x20;  \* 3 = Third Class



2\. Sex



&#x20;  \* Male

&#x20;  \* Female



3\. Age



&#x20;  \* Passenger age



Target Variable:



Survived



0 = No



1 = Yes







5\. Libraries Used



import pandas as pd



Used for:



\* Reading dataset

\* Handling tables





import matplotlib.pyplot as plt



Used for:



\* Plotting graphs

\* Visualizing tree





from sklearn.model\_selection import train\_test\_split



Used for:



\* Splitting dataset into training and testing





from sklearn.preprocessing import LabelEncoder



Used for:



\* Converting text into numbers



Example:



Male → 0



Female → 1





from sklearn.tree import DecisionTreeClassifier



Used for:



\* Creating decision tree model





from sklearn.metrics import accuracy\_score



Used for:



\* Checking model performance





from sklearn.tree import plot\_tree



Used for:



\* Visualizing decision tree







6\. Data Preprocessing



Step 1:



Load dataset



df = pd.read\_csv("Titanic.csv")





Step 2:



Select important columns



features = \["Pclass","Sex","Age"]



target = "Survived"





Step 3:



Handle missing values



df\["Age"].fillna(df\["Age"].median(), inplace=True)



Reason:



Some age values may be missing.



Median replaces missing values safely.





Step 4:



Convert text into numbers



LabelEncoder()



Male → 0



Female → 1



Machine Learning models cannot understand text.





7\. Input and Output



X = Features



Contains:



Pclass



Sex



Age





y = Target



Contains:



Survived







8\. Train-Test Split



X\_train, X\_test, y\_train, y\_test = train\_test\_split()



Purpose:



Training Set



Used for learning



Testing Set



Used for evaluation



Common split:



80% Training



20% Testing







9\. Creating Decision Tree Model



model = DecisionTreeClassifier()



This creates an empty decision tree.







10\. Training the Model



model.fit(X\_train, y\_train)



What happens?



The model studies:



Passenger Class



Gender



Age



and learns patterns that affect survival.







11\. Prediction



y\_pred = model.predict(X\_test)



The model predicts:



Survived = 1



or



Not Survived = 0



for unseen passengers.







12\. Accuracy Calculation



accuracy = accuracy\_score(y\_test, y\_pred)



Formula:



Accuracy =

Correct Predictions





Total Predictions



×100



Example:



90 correct out of 100



Accuracy = 90%





13\. Visualizing Decision Tree



plot\_tree(model)



Shows:



Root Node



Branches



Leaf Nodes



Decision Rules



Example:



Sex <= 0.5?



├── Yes → Not Survived



└── No → Survived





14\. Understanding Tree Components



Root Node



First decision point.





Internal Node



Intermediate decision.





Branch



Path connecting nodes.





Leaf Node



Final prediction.





15\. Workflow of Task 5



Step 1:

Load Titanic Dataset



↓



Step 2:

Handle missing values



↓



Step 3:

Convert text into numbers



↓



Step 4:

Separate Features and Target



↓



Step 5:

Split into Train and Test



↓



Step 6:

Create Decision Tree



↓



Step 7:

Train Model



↓



Step 8:

Predict Results



↓



Step 9:

Calculate Accuracy



↓



Step 10:

Visualize Tree









