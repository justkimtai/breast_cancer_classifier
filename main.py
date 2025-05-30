from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

import matplotlib.pyplot as plt
import numpy as np

data = load_breast_cancer()

# Extract features and labels
features = data['data']
labels = data['target']

# Split data for training and testing
train_x, test_x, train_y, test_y = train_test_split(
  features, labels, test_size=0.33, random_state=42
)

# Algorithm for classifying
model = GaussianNB()
model.fit(train_x, train_y)

# Predictions
predictions = model.predict(test_x)
print(predictions[:5])

# Count predictions for each class
unique, counts = np.unique(predictions, return_counts=True)
class_labels = data.target_names  # ['malignant', 'benign']

# Plot bar chart
plt.figure(figsize=(6, 4))
plt.bar(class_labels, counts, color=["red", "green"])
plt.title("Predicted Class Distribution")
plt.xlabel("Tumor Type")
plt.ylabel("Number of Predictions")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("images/predicted_class_distribution.png")

print("📊 Bar chart saved as predicted_class_distribution.png")


# Accuracy score of the prediction operation
accuracy = accuracy_score(test_y, predictions)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Confusion matrix
cm = confusion_matrix(test_y, predictions)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=data.target_names)
disp.plot(cmap=plt.cm.Blues)
plt.title("COnfusion Matrix - Breast Cancer Classification")
plt.savefig("images/confusion_matrix.png")
print("✅ Confusion matrix saved as confusion_matrix.png")
