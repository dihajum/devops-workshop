import mlflow
import pandas as pd
import my_setup
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)


mlflow.set_experiment("Simple Model")

model_uri = "models:/m-fc2046295ed34969bfff912bdfad983b"

# Load the Iris dataset
X, y = datasets.load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Load the model back for predictions as a generic Python Function model
loaded_model = mlflow.pyfunc.load_model(model_uri)

predictions = loaded_model.predict(X_test)

iris_feature_names = datasets.load_iris().feature_names

result = pd.DataFrame(X_test, columns=iris_feature_names)
result["actual_class"] = y_test
result["predicted_class"] = predictions

print(result[:4])
