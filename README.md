# Chronic-Kidney-Disease
This project develops a predictive model for Chronic Kidney Disease (CKD) using machine learning to aid early diagnosis and intervention, enhancing patient outcomes and reducing costs. Using a dataset of 400 patients with 26 features, including age, blood pressure, and lab results, the model predicts CKD presence.


Chronic Kidney Disease Prediction

Project Overview
This project aims to develop a predictive model for Chronic Kidney Disease (CKD) using various machine learning algorithms. The primary goal is to assist healthcare providers in the early diagnosis and intervention of CKD, ultimately improving patient outcomes and reducing healthcare costs.

Problem Description
Chronic Kidney Disease is a progressive condition where the kidneys lose function over time, often without noticeable symptoms in the early stages. The dataset used in this project contains medical records of 400 patients with 26 features including age, blood pressure, various lab test results, and specific conditions or observations. The primary variable of interest is whether a patient has CKD.

![image](https://github.com/user-attachments/assets/edc0efba-87a9-418e-8c01-55df1c94ebe2)


Methodology
The project follows the CRISP-DM framework:
1. Business Understanding: Define objectives for predicting CKD and understand the business requirements.
2. Data Understanding: Collect and explore relevant data sources.
3. Data Preparation: Clean, preprocess, and transform data for modeling.
4. Modeling: Train various machine learning models including K-Nearest Neighbors, Naive Bayes, Logistic Regression, and Random Forest.
5. Evaluation: Assess model performance using accuracy, sensitivity, specificity, and ROC curves.
6. Deployment: Integrate the model into clinical workflows for real-time CKD risk assessment.

Key Findings
1. Data Imbalance: The dataset has a higher prevalence of CKD cases (248) compared to non-CKD cases (150).
2. Feature Importance: Key features influencing CKD include blood pressure, blood glucose, and serum creatinine levels.
3. Model Performance: The Random Forest model achieved the highest accuracy (99.68% on training data and 98.75% on test data), followed by K-Nearest Neighbors, Naive Bayes, and Logistic Regression.

Data Preprocessing
1. Handling Missing Data: Employed techniques such as random sampling and mode imputation to handle missing values.
2. Encoding Categorical Variables: Used LabelEncoder to transform non-numeric categories into numerical format.
3. Feature Scaling: Applied StandardScaler to normalize numerical features.

Modeling and Evaluation
1. K-Nearest Neighbors (KNN): Achieved 97.18% accuracy on training data and 96.25% on test data.
2. Naive Bayes: Achieved 96.56% accuracy on training data and 96.25% on test data.
3. Logistic Regression: Achieved 90.31% accuracy on training data and 92.50% on test data.
4. Random Forest: Achieved 99.68% accuracy on training data and 98.75% on test data.

Deployment
The CKD prediction model can be integrated into healthcare systems for real-time risk assessment, helping in early identification of at-risk patients. Benefits include improved patient care, optimized healthcare resource allocation, and reduced healthcare costs.

Conclusion
Our CKD prediction model facilitates early identification of at-risk patients, enabling timely interventions and personalized care. This not only enhances patient outcomes but also optimizes the use of healthcare resources, contributing to more efficient and cost-effective healthcare delivery.

Acknowledgments
Submitted By: Rutvi Sutariya
Guided By: Prof. Mahmoud Daneshmand
Course: MIS637 Data Analysis and Machine Learning

Dataset
The dataset used in this project is publicly available on Kaggle: [Chronic Kidney Disease Dataset](https://www.kaggle.com/datasets/mansoordaku/ckdisease)
