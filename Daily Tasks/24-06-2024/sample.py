import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('sample_dataset.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())
print()

# Summary statistics
summary_stats = df.describe()

# Mean and standard deviation of Sepal Length
mean_sepal_length = summary_stats.loc['mean', 'Sepal Length (cm)']
std_dev_sepal_length = summary_stats.loc['std', 'Sepal Length (cm)']

print(f"Mean of Sepal Length: {mean_sepal_length}")
print(f"Standard deviation of Sepal Length: {std_dev_sepal_length}")
print()

# Check for missing values
missing_values = df.isnull().sum()

if missing_values.sum() > 0:
    df = df.dropna()  # Drop rows with missing values

# Mapping dictionary
species_map = {'FlowerA': 0, 'FlowerB': 1, 'FlowerC': 2}

# Apply mapping to the 'Species' column
df['Species'] = df['Species'].map(species_map)

# Splitting the dataset
X = df.drop('Species', axis=1)
y = df['Species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

# Initialize the classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Visualize the trained decision tree
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=X.columns, class_names=list(species_map.keys()), filled=True)
plt.title("Decision Tree Visualization")
plt.show()

# Predicting on the test set
y_pred = clf.predict(X_test)

# Compute accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of the decision tree classifier: {accuracy}")
print()

# Classification report
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=species_map.keys()))
print()

# Confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
