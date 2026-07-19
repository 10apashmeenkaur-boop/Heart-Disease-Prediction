import os
from ucimlrepo import fetch_ucirepo
import pandas as pd

# Fetch the official UCI Heart Disease dataset (Cleveland)
heart_disease = fetch_ucirepo(id=45)

X = heart_disease.data.features
y = heart_disease.data.targets

df = pd.concat([X, y], axis=1)
df.columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
              'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

# UCI's target ranges 0-4 (severity); convert to binary: 0 = no disease, 1 = disease
df['target'] = df['target'].apply(lambda x: 1 if x > 0 else 0)

# Drop rows with missing values (a few rows have '?' in ca/thal)
df = df.dropna()

os.makedirs("Notebook_Experiments/Data", exist_ok=True)
df.to_csv("Notebook_Experiments/Data/heart.csv", index=False)
print("Saved:", df.shape)