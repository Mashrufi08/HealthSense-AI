import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv('heart.csv')

# Drop unnecessary columns
df = df.drop(['id', 'dataset'], axis=1)

# Handle missing values
df = df.fillna(df.median(numeric_only=True))

# Encode categorical columns
le = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col].astype(str))

# Target: 0 = no disease, 1 = disease
df['num'] = df['num'].apply(lambda x: 1 if x > 0 else 0)

X = df.drop('num', axis=1)
y = df['num']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"Model Accuracy: {round(accuracy*100, 2)}%")

joblib.dump(model, 'heart_model.pkl')
joblib.dump(list(X.columns), 'columns.pkl')
print("Model saved successfully!")
print("Columns:", list(X.columns))