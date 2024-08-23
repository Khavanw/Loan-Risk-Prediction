# Loan Risk Prediction

## Introduction
This project aims to build a loan risk prediction model using machine learning algorithms. The goal is to predict the likelihood of a loan default based on the borrower's characteristics and loan features.

## Requirements
- Python 3.7+
- pandas
- numpy
- scikit-learn
- xgboost

You can install the required libraries using the command:

```pip install pandas numpy scikit-learn xgboost```

## Project structure
```
loan-risk-prediction/
│
├── best_model/
│   ├── best_pipeline.joblib  
│   ├── best_pipeline.pkl
│   └── random_forest_model.joblib
│
├── data/
│   ├── credit_risk_dataset1.csv
│   ├── credit_risk_dataset2.csv
│   └── loan_data.csv
│
├── images/
│
├── scripts/
│   ├── Credit_Prediction.ipynb
│   ├── Loan_Prediction.ipynb
│   └── pipeline.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```



## Implementation process

1. **Data Collection and Preprocessing**
   - Data cleaning
   - Handling missing values
   - Encoding categorical variables

2. **Exploratory Data Analysis (EDA)**
   - Visualize variable distributions
   - Analyze correlations

3. **Feature Engineering**
   - Create new features
   - Normalize features

4. **Model Building and Training**
   - Logistic Regression
   - Decision Tree
   - Random Forest
   - XGBoost with hyperparameter tuning
   - Support Vector Machine

5. **Model Evaluation**
   - Use metrics such as accuracy, precision, recall, F1-score, and AUC-ROC

## User Guide

1. Clone repository: 
```https://github.com/Khavanw/Loan-Risk-Prediction.git```
2. Setup requirements:
```pip install -r requirements.txt```

## Results All Model Machine Learning

![image](https://github.com/user-attachments/assets/a4361fd0-3ee8-4190-b1b1-57c0c95c1985)

## Hyperparameter Optimization
For XGBoost, we use GridSearchCV to find the optimal hyperparameters. The parameters being tuned include:
- learning_rate
- max_depth
- n_estimators
- subsample


## License
[MIT](https://choosealicense.com/licenses/mit/)
