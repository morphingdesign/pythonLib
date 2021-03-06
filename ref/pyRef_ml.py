# -----------------------------------------------------------
# pyRef_ml.py
# v.1.0
# Updated: 20210212
# -----------------------------------------------------------

"""
Outline of data science & machine learning operations.
"""

# -----------------------------------------------------------
# LIBRARY ACCESS )))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# For use with IPython interactivity, such as Jupyter notebook.
%matplotlib inline

# -----------------------------------------------------------
# LIBRARY ACCESS )))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# PLOT FORMATTING ))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

# Clear formatting for Seaborn-based plots
sns.set_style('whitegrid')

# -----------------------------------------------------------
# PLOT FORMATTING ))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# DATAFRAME OPERATIONS )))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------




# -----------------------------------------------------------
# DATAFRAME OPERATIONS )))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# MODEL PREP )))))))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

# Train/test split.
from sklearn.model_selection import train_test_split
X = df_features
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

#************************************************************
# Scale data.
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# Fit only on the training features, not test features
scaler.fit(features)
scaler.transform(features)

#************************************************************

# -----------------------------------------------------------
# MODEL PREP )))))))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# MODELS )))))))))))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

# CLASSIFICATION MODELS

# Support Vector Classifier (SVC) Model
from sklearn.svm import SVC
model = SVC()

# K-Nearest Neighbor (KNN) Classifier Model
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1))

# -----------------------------------------------------------
# MODELS )))))))))))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# MODEL TRAINING & TESTING )))))))))))))))))))))))))))) START
# -----------------------------------------------------------

# Model training

model.fit(X_train, y_train)


# Model testing

pred = model.predict(X_test)

# -----------------------------------------------------------
# MODEL TRAINING & TESTING )))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# MODEL EVALUATION )))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

# Classification Model Evaluation
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, pred))
print('\n')
print(classification_report(y_test, pred))

# -----------------------------------------------------------
# MODEL EVALUATION )))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# DATA ACCESS ))))))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

# NEW DATA
# Generate sample sets using NumPy.
# Evenly spaced numbers over specified interval.
sample_set = np.linspace(-1, 1, 10)  # 10 values from -1 to 1

#************************************************************
# DATA SETS
# Import available datasets from SciKit.
from sklearn.datasets import <dataset_name>

# Generate binary classification data blobs.
from sklearn.datasets import make_blobs
# Specify num of samples, features, centers, and rand state.
data = make_blobs(n_samples=50, n_features=2, centers=2, random_state=75)

# -----------------------------------------------------------
# DATA ACCESS ))))))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------