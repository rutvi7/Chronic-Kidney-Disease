# -*- coding: utf-8 -*-
"""Finalproject_MIS637-B_Group-4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RA3wK2FGzsUacmz-VjYpRobjp6fREwRc
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import warnings
warnings.filterwarnings('ignore')
plt.style.use('fivethirtyeight')
sns.set()
plt.style.use('ggplot')

# %matplotlib inline

df = pd.read_csv("kidney_disease.csv")
df.head()

# finding if it is a binary classification or multi class classification
df['classification'].value_counts()

df.shape

#removeing unwanted
df.drop('id',axis=1,inplace=True)

df.head()

print(df.columns)

df.columns=['age','blood_pressure','specific_gravity','albumin','sugar','red_blood_cells','pus_cell','pus_cell_clumps','bacteria','blood_glucose_random','BUN','serum_creatinine','superoxide_dismutase','potassium','haemoglobin','packed_cell_volume','white_blood_cell_count','red_blood_cell_count','hypertension','diabetes_mellitus','coronary_artary_disease','appetite','peda_edema','aanemia','class']
df.head()

#checking for density
df.describe()

#checking for information of data
df.info()

#converting object column to numeric column
df['packed_cell_volume']= pd.to_numeric(df['packed_cell_volume'],errors = 'coerce')
df['white_blood_cell_count']= pd.to_numeric(df['white_blood_cell_count'],errors = 'coerce')
df['red_blood_cell_count']= pd.to_numeric(df['red_blood_cell_count'],errors = 'coerce')
#df['packed_cell_volume']= pd.to_numeric(df['packed_cell_volume'],errors = 'coerce')
df.info()

df.columns

cat_cols = [col for col in df.columns if df[col].dtype =='object']
num_cols = [col for col in df.columns if df[col].dtype !='object']

cat_cols

num_cols

#ckd = chronic kidney disease
for col in cat_cols:
    print(f"{col} has {df[col].unique()}")

df['diabetes_mellitus'].replace(to_replace = {'\tno':'no','\tyes':'yes',' yes':'yes'},inplace = True)
df['coronary_artary_disease'].replace(to_replace = {'\tno':'no','\tyes':'yes',' yes':'yes'},inplace = True)
df['class']= df['class'].replace(to_replace={'ckd\t':'ckd','notckd':'not ckd'})
df['class']= df['class'].map({'ckd':0,'not ckd':1})
df['class']=pd.to_numeric(df['class'],errors= 'coerce')

cols = ['diabetes_mellitus','coronary_artary_disease','class']
for col in cols:
    print(f"{col} has {df[col].unique()}")

#creating figure to check for distributions numerical values
plt.figure(figsize = (20,15))
plotnumber = 1
for column in num_cols:
    if plotnumber <=14:
        ax = plt.subplot(3, 5, plotnumber)
        sns.distplot(df[column],color='blue')
        plt.xlabel(column)
    plotnumber += 1
plt.tight_layout()
plt.show()

#creatinf figure to check for distributions categorical
plt.figure(figsize = (20,15))
plotnumber = 1
for column in cat_cols:
    if plotnumber <=14:
        ax = plt.subplot(3, 5, plotnumber)
        sns.countplot(x= column, data =df ,palette = 'Set2')
        plt.xlabel(column)
    plotnumber += 1
plt.tight_layout()
plt.show()

#correlation matrix

# Select only numeric columns
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Generate correlation matrix
corr_matrix = numeric_df.corr()

# Plot correlation matrix heatmap
plt.figure(figsize=(15, 8))
sns.heatmap(corr_matrix, annot=True, cmap='YlGnBu', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

#corr_matrix = df.corr()

# EDA

def voilin(col):
    fig  = px.violin(df, y=col, x='class', color='class', box=True, template='plotly_dark')
    return fig.show()

def kde(col):
    grid = sns.FacetGrid(df, hue='class', height = 6, aspect = 2)
    grid.map(sns.kdeplot, col)
    grid.add_legend()

def scatter_plot(col1, col2):
    fig  = px.scatter(df, x=col1, y=col2, color="class",  template='plotly_dark')
    return fig.show()

kde('red_blood_cell_count')

# Data preprocessing

# checking for missing value
df.isnull().sum().sort_values(ascending=False)

df[num_cols].isnull().sum()

df[cat_cols].isnull().sum()

df.head()

# two method
# radom sampling->higer null value
# mean/mode-> lower null value

def random_sampling(feature):
    random_sample = df[feature].dropna().sample(df[feature].isna().sum())
    random_sample.index = df[df[feature].isnull()].index
    df.loc[df[feature].isnull(), feature] = random_sample

def impute_mode(feature):
    mode = df[feature].mode()[0]
    df[feature] = df[feature].fillna(mode)

# random sampling for numerical value
for col in num_cols:
    random_sampling(col)

df[num_cols].isnull().sum()

random_sampling('red_blood_cells')
random_sampling('pus_cell')

for col in cat_cols:
    impute_mode(col)

df[cat_cols].isnull().sum()

# Feature Encoding

for col in cat_cols:
    print(f"{col} has {df[col].nunique()}")

# label_encoder
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

for col in cat_cols:
    df[col] = le.fit_transform(df[col])

df.head()

# Model Building

X = df.drop('class', axis = 1)
y = df['class']

X

y

from sklearn.model_selection import train_test_split

X_train,X_test, y_train, y_test =  train_test_split(X,y, test_size = 0.2, random_state = 0)

# Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
random_seed = 42
rand_clf = RandomForestClassifier(criterion = "gini", max_depth = 10, max_features="sqrt", min_samples_leaf= 1, min_samples_split= 7, n_estimators = 400)
rand_clf.fit(X_train, y_train)
rand_clf_acc = accuracy_score(y_test, rand_clf.predict(X_test))
print(f"Training Accuracy of Random Forest is {accuracy_score(y_train, rand_clf.predict(X_train))}")
print(f"Testing Accuracy of Random Forest is {accuracy_score(y_test, rand_clf.predict(X_test))}")

print(f"Confusion Matrix of Random Forest is \n {confusion_matrix(y_test, rand_clf.predict(X_test))}\n")
print(f"Classification Report of Random Forest is \n{classification_report(y_test, rand_clf.predict(X_test))}")

# logistic regression

from sklearn.linear_model import LogisticRegression
random_seed = 42
lr = LogisticRegression()
lr.fit(X_train, y_train)
lr_acc = accuracy_score(y_test, lr.predict(X_test))
print(f"Training Accuracy of LR is {accuracy_score(y_train, lr.predict(X_train))}")
print(f"Testing Accuracy of LR is {accuracy_score(y_test, lr.predict(X_test))}")

print(f"Confusion Matrix of LR is \n {confusion_matrix(y_test, lr.predict(X_test))}\n")
print(f"Classification Report of LR is \n{classification_report(y_test, lr.predict(X_test))}")

scaler = StandardScaler() # scaling
x_train_scaled = scaler.fit_transform(X_train)
x_test_scaled = scaler.transform(X_test)

# Naive_bayes algorithm

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import GridSearchCV
#from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
random_seed = 42
# Initialize Gaussian Naive Bayes classifier
nb = GaussianNB( )

# No parameters to tune for Gaussian Naive Bayes, but we'll define an empty parameter grid for consistency
parameter = { }

# Define the grid search with cross-validation
grid_search = GridSearchCV(nb, parameter)
grid_search.fit(X_train, y_train)

# Print the best hyperparameters and the corresponding best score
print(grid_search.best_params_)
print(grid_search.best_score_)


#nb = GaussianNB()

# Fit the classifier to the scaled training data
nb.fit(x_train_scaled, y_train)

# Evaluate the classifier on the test data
nb_acc = accuracy_score(y_test, nb.predict(x_test_scaled))

# Print accuracy and other evaluation metrics
print(f"Training Accuracy of Naive Bayes is {accuracy_score(y_train, nb.predict(x_train_scaled))}")
print(f"Testing Accuracy of Naive Bayes is {accuracy_score(y_test, nb.predict(x_test_scaled))}")

print(f"Confusion Matrix of Naive Bayes is \n {confusion_matrix(y_test, nb.predict(x_test_scaled))}\n")
print(f"Classification Report of Naive Bayes is \n{classification_report(y_test, nb.predict(x_test_scaled))}")

# KNN

scaler = StandardScaler() # scaling
x_train_scaled = scaler.fit_transform(X_train)
x_test_scaled = scaler.transform(X_test)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

knn = KNeighborsClassifier()
knn.fit(x_train_scaled, y_train)

knn_acc = accuracy_score(y_test, knn.predict(x_test_scaled))
print(f"Training Accuracy of KNN is {accuracy_score(y_train, knn.predict(x_train_scaled))}")
print(f"Testing Accuracy of KNN is {accuracy_score(y_test, knn.predict(x_test_scaled))}")

print(f"Confusion Matrix of KNN is \n {confusion_matrix(y_test, knn.predict(x_test_scaled))}\n")
print(f"Classification Report of KNN is \n{classification_report(y_test, knn.predict(x_test_scaled))}")

# model comparison

models = pd.DataFrame({
    'Model':['KNN', 'Random Forest Classifier', 'Naive_bayes', 'Logistic Regression'],
    'Score':[lr_acc,knn_acc, rand_clf_acc,nb_acc]
})

models.sort_values(by='Score', ascending = False)

import pickle
from sklearn import metrics
plt.figure(figsize=(8,5))
models = [
{
    'label': 'LR',
    'model': lr,
},
{
    'label': 'KNN',
    'model': knn,
},
{
    'label': 'RF',
    'model': rand_clf,
},
{
    'label':'nb',
    'model':nb,
}
]
for m in models:
    model = m['model']
    model.fit(X_train, y_train)
    y_pred=model.predict(x_test_scaled)
    fpr1, tpr1, thresholds = metrics.roc_curve(y_test, model.predict_proba(x_test_scaled)[:,1])
    auc = metrics.roc_auc_score(y_test,model.predict(x_test_scaled))
    plt.plot(fpr1, tpr1, label='%s - ROC (area = %0.2f)' % (m['label'], auc))

plt.plot([0, 1], [0, 1],'r--')
plt.xlim([-0.01, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('1 - Specificity (False Positive Rate)', fontsize=12)
plt.ylabel('Sensitivity (True Positive Rate)', fontsize=12)
plt.title('ROC - Kidney Disease Prediction', fontsize=12)
plt.legend(loc="lower right", fontsize=12)
plt.savefig("roc_kidney.jpeg", format='jpeg', dpi=400, bbox_inches='tight')
plt.show()