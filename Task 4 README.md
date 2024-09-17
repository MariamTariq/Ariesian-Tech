# Customer Travel Prediction
This project aims to predict customer behavior based on travel-related features using a **Random Forest Classifier**. The code includes data exploration, preprocessing, model building, and evaluation steps using the `Customertravel.csv` dataset.
## Table of Contents
- [Installation](#installation)
- [Dataset](#dataset)
- [Project Workflow](#project-workflow)
- [Results](#results)
## Installation
To run this project, you need Python and the required libraries installed. Install the necessary dependencies using the following command:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```
## Dataset
The dataset used in this project is `Customertravel.csv`. Make sure to adjust the file path in the code to point to the location of your dataset if necessary.
## Project Workflow
### 1. Importing Libraries
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
```
### 2. Loading the Dataset
```python
file_path = 'Customertravel.csv'
df = pd.read_csv(file_path)
```
This loads the dataset into a pandas DataFrame for further analysis.
### 3. Data Exploration
- Display the first 5 rows of the dataset using `df.head()`.
- Print dataset info (`df.info()`), check for missing values, and display a statistical summary of numerical columns.
- Visualize the distribution of the target variable (`Target`) using a count plot.
- Plot the distribution of the `Age` column.
### 4. Data Preprocessing
- **Handling Missing Values**:
  - Missing values in numerical columns are filled with the median.
  - Missing values in categorical columns are filled with the mode.  
- **Encoding Categorical Variables**:
  - Categorical features are converted into numerical using `LabelEncoder`.
- **Feature and Target Separation**:
  - Features (`X`) are separated from the target variable (`y`).
```python
X = df.drop('Target', axis=1)
y = df['Target']
```
- **Train-Test Split**:
  - The dataset is split into training and testing sets (70% training, 30% testing).
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```
- **Feature Scaling**:
  - Standard scaling is applied to normalize the feature values.
```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```
### 5. Building and Training the Model
A **Random Forest Classifier** is created and trained on the scaled training data.
```python
model = RandomForestClassifier(random_state=42)
model.fit(X_train_scaled, y_train)
```
### 6. Model Evaluation
- **Predictions**:
  The model makes predictions on the test data.
```python
y_pred = model.predict(X_test_scaled)
```
- **Accuracy**:
  The accuracy of the model is calculated.
```python
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy*100:.2f}%")
```
- **Classification Report**:
  A detailed classification report is generated.
```python
print(classification_report(y_test, y_pred))
```
- **Confusion Matrix**:
  A confusion matrix is visualized to understand the model's performance.
```python
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.show()
```
- **Feature Importance**:
  The importance of each feature is visualized.
```python
sns.barplot(x=model.feature_importances_, y=X.columns)
plt.title('Feature Importance')
plt.show()
```
## Results
- **Accuracy**: The model's accuracy is displayed after evaluation.
- **Classification Report**: Key metrics like precision, recall, and F1-score are presented.
- **Confusion Matrix**: A heatmap provides insights into true positive, false positive, true negative, and false negative rates.
- **Feature Importance**: A bar plot shows the significance of each feature in predicting customer behavior.
Here are the visual results of this thorough analysis.

![Figure_1 task 4](https://github.com/user-attachments/assets/e88fe3d6-3e83-48c7-aaf0-5c330063b759)
![Figure_2 task 4](https://github.com/user-attachments/assets/49afa991-0c04-439c-a74b-9a06d66519e1)
![Figure_3 task 4](https://github.com/user-attachments/assets/6702b9cd-4de5-4d19-855a-2d6e29b8526b)
![Figure_4 task 4](https://github.com/user-attachments/assets/f26acd32-c93d-4771-821d-06b6b2b90c67)
![Figure_5 task 4](https://github.com/user-attachments/assets/087ada29-c367-4ec6-829f-c52cd17af71e)



