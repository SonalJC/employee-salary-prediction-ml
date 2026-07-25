# 💼 Employee Salary Prediction using Machine Learning

## 📌 Project Overview

Employee Salary Prediction is an end-to-end Machine Learning project that predicts whether an employee's annual income is **greater than $50K** or **less than or equal to $50K** based on demographic and employment-related information.

The project demonstrates the complete machine learning workflow, including data preprocessing, feature engineering, model training, hyperparameter tuning, model evaluation, and deployment using Streamlit.

---

## 🎯 Project Aim

The objective of this project is to build a machine learning model that classifies employees into two income categories:

- **<=50K**
- **>50K**

using employee-related features such as age, education, occupation, work class, relationship status, and working hours.

---

## 📊 Dataset

**Dataset:** Adult Income Dataset

**Target Variable**

- <=50K
- >50K

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Pickle

---

## 📂 Machine Learning Workflow

✔ Data Cleaning

✔ Exploratory Data Analysis (EDA)

✔ Feature Selection

✔ Category Reduction

✔ One-Hot Encoding

✔ MinMax Scaling

✔ ColumnTransformer

✔ Pipeline

✔ Logistic Regression

✔ Random Forest Classifier

✔ Hyperparameter Tuning using RandomizedSearchCV

✔ Model Evaluation

✔ Streamlit Deployment

---

## 🔍 Exploratory Data Analysis

Performed:

- Missing Value Analysis
- Duplicate Value Check
- Class Distribution
- Categorical Feature Analysis
- Numerical Feature Analysis
- Correlation Heatmap
- Feature Importance

---

## ⚙️ Data Preprocessing

- Removed unnecessary features
- Reduced high-cardinality categorical values
- Applied One-Hot Encoding to categorical features
- Applied MinMax Scaling to numerical features
- Used ColumnTransformer to combine preprocessing steps
- Built a Pipeline for consistent preprocessing and prediction

---

## 🤖 Models Used

### Logistic Regression

Used as a baseline classification model.

### Random Forest Classifier

Selected as the final model due to its superior performance after hyperparameter tuning.

---

## 🎯 Hyperparameter Tuning

RandomizedSearchCV was used to identify the best combination of Random Forest hyperparameters, improving the model's overall performance.

---

## 📈 Model Evaluation

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report

---

## 🌐 Streamlit Application

The trained model was deployed using Streamlit, allowing users to predict employee salary categories through an interactive web application.

---

## 📷 Project Screenshots

### Streamlit Interface

<img width="858" height="827" alt="image" src="https://github.com/user-attachments/assets/4172c924-2e95-4dc8-b64c-2e5135876d91" />

### Confusion Matrix

(Add Screenshot Here)

### Feature Importance

(Add Screenshot Here)

---

## 🚀 Future Improvements

- Handle class imbalance using SMOTE
- Try XGBoost / LightGBM for better performance on imbalanced data
- Try GridSearchCV with narrower param range after RandomizedSearch
- Add batch prediction (CSV upload) in Streamlit app
- Add ROC-AUC curve for better model comparison

---

## 👩‍💻 Author

**Sonal Chauhan**

Final Year B.Tech (Computer Science)

Interested in Machine Learning, Data Science, and AI.
