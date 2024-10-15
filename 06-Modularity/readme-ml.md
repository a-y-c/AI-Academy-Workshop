# Exercise: Modularity in Python with Machine Learning

## Objective
The goal of this exercise is to practice modular programming in Python by creating and using modules, with a focus on machine learning components. This will help you understand how to organize your code into reusable and maintainable components.

## Instructions

1. **Create a Data Processing Module:**

   - Create a new Python file named `data_processing.py`.
   - In this file, define the following functions:
     - `load_data(file_path)`: Loads data from a CSV file.
     - `preprocess_data(data)`: Preprocesses the data (e.g., handling missing values, scaling features).

2. **Create a Machine Learning Module:**

   - Create another Python file named `ml_model.py`.
   - In this file, define the following functions:
     - `train_model(X_train, y_train)`: Trains a machine learning model.
     - `evaluate_model(model, X_test, y_test)`: Evaluates the trained model on test data.

3. **Create a Main Program:**

   - Create a new Python file named `main.py`.
   - In this file, import the functions from `data_processing.py` and `ml_model.py`.
   - Use these functions to perform the following tasks:
     - Load and preprocess the data.
     - Split the data into training and testing sets.
     - Train a machine learning model.
     - Evaluate the model on the test data.

## Example Code

### data_processing.py
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(data):
    data = data.dropna()
    X = data.drop('target', axis=1)
    y = data['target']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return train_test_split(X_scaled, y, test_size=0.2, random_state=42)
```

### ml_model.py
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_model(X_train, y_train):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print(f"Classification Report:\n{classification_report(y_test, y_pred)}")
```


### main.py
```python
from data_processing import load_data, preprocess_data
from ml_model import train_model, evaluate_model

# Load and preprocess data
file_path = 'data.csv'
data = load_data(file_path)
X_train, X_test, y_train, y_test = preprocess_data(data)

# Train and evaluate model
model = train_model(X_train, y_train)
evaluate_model(model, X_test, y_test)
```

## Conclusion
By completing this exercise, you will gain hands-on experience with modular programming in Python, specifically in the context of machine learning. This will help you write more organized, reusable, and maintainable code.

Happy coding!
