import streamlit as st
from sklearn.datasets import load_breast_cancer
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Load and train model
data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.3, random_state=42)
model = GaussianNB()
model.fit(X_train, y_train)

# UI
st.title("Breast Cancer Prediction App")
st.write("Enter tumor measurements to predict malignancy:")

# Feature sliders (simplified example)
mean_radius = st.slider("Mean Radius", float(X_train[:, 0].min()), float(X_train[:, 0].max()))
mean_texture = st.slider("Mean Texture", float(X_train[:, 1].min()), float(X_train[:, 1].max()))
input_data = np.array([[mean_radius, mean_texture] + [0]*(30-2)])  # filler for 28 other features

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    st.success(f"Prediction: {'Benign' if prediction else 'Malignant'}")
