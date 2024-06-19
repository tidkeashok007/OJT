import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('heart_disease.csv')

# Handle missing values
data.dropna(inplace=True)

# Check the distribution of the target variable
print(data['target'].value_counts())

# Simulate data for the missing class (target = 0)
if len(data['target'].value_counts()) == 1:
    # Assuming 'target' = 1 exists, we will create synthetic data for 'target' = 0
    num_samples = data['target'].value_counts().values[0]  # Number of samples to generate
    synthetic_data = data.copy()
    synthetic_data['target'] = 0  # Set target to 0

    # Randomize numerical features slightly
    numerical_features = ['age', 'chol', 'trestbps', 'thalach', 'oldpeak']
    for feature in numerical_features:
        synthetic_data[feature] = synthetic_data[feature] * np.random.uniform(0.9, 1.1, size=num_samples)

    # Combine original and synthetic data
    data = pd.concat([data, synthetic_data], ignore_index=True)

# Encode categorical variables (sex column)
data = pd.get_dummies(data, columns=['sex'], drop_first=True)

# Scale numerical features
scaler = StandardScaler()
numerical_features = ['age', 'chol', 'trestbps']
data[numerical_features] = scaler.fit_transform(data[numerical_features])

# Perform basic exploratory data analysis
# Visualize correlations
plt.figure(figsize=(12, 10))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Split the data into training and testing sets
X = data.drop('target', axis=1)
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model if there are at least two classes in the target variable
if len(np.unique(y_train)) > 1 and len(np.unique(y_test)) > 1:
    model = LogisticRegression(penalty='l1', solver='liblinear')
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred)

    print(f'Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}, F1-score: {f1}, ROC-AUC: {roc_auc}')

    # Plot the ROC curve
    fpr, tpr, _ = roc_curve(y_test, model.predict_proba(X_test)[:,1])
    plt.figure()
    plt.plot(fpr, tpr, label='ROC curve')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend(loc='best')
    plt.show()

    # Interpret the coefficients
    coefficients = pd.DataFrame({'feature': X.columns, 'coefficient': model.coef_[0]})
    print(coefficients)

    # Calculate odds ratios
    odds_ratios = np.exp(coefficients['coefficient'])
    print(odds_ratios)
else:
    print("The target variable does not contain at least two classes.")