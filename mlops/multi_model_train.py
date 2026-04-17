import mlflow
import mlflow.sklearn
import my_setup
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from mlflow.models import infer_signature
import warnings

# Suppress the MLflow model config warning if present
warnings.filterwarnings("ignore", message=".*Failed to log model config as params.*")

mlflow.set_experiment("Model Guide Search")

# Model configurations
model_configs = [
    {"model_type": "RandomForest", "n_estimators": 100, "max_depth": 10},
    {"model_type": "RandomForest", "n_estimators": 200, "max_depth": 20},
    {"model_type": "LogisticRegression", "C": 1.0, "solver": "lbfgs"},
    {"model_type": "LogisticRegression", "C": 0.1, "solver": "saga"},
    {"model_type": "SVM", "kernel": "rbf", "C": 1.0},
    {"model_type": "SVM", "kernel": "linear", "C": 0.5},
]

# Performance metrics (simulated)
accuracy_scores = [0.92, 0.94, 0.88, 0.86, 0.90, 0.87]
precision_scores = [0.91, 0.93, 0.87, 0.85, 0.89, 0.86]
recall_scores = [0.93, 0.95, 0.89, 0.87, 0.91, 0.88]
f1_scores = [0.92, 0.94, 0.88, 0.86, 0.90, 0.87]

# Model metadata
versions = ["v1.0", "v1.1", "v1.0", "v2.0", "v1.0", "v1.1"]
environments = [
    "production",
    "staging",
    "production",
    "development",
    "staging",
    "production",
]
frameworks = ["sklearn", "sklearn", "sklearn", "sklearn", "sklearn", "sklearn"]

# Create dummy training data
X_train = np.random.rand(100, 10)
y_train = np.random.randint(0, 2, 100)

# Create input example for model signature
input_example = pd.DataFrame(X_train[:5], columns=[f"feature_{i}" for i in range(10)])

for i, config in enumerate(model_configs):
    with mlflow.start_run():
        # Create and train model based on type
        if config["model_type"] == "RandomForest":
            model = RandomForestClassifier(
                n_estimators=config["n_estimators"],
                max_depth=config["max_depth"],
                random_state=42,
            )
            mlflow.log_param("n_estimators", config["n_estimators"])
            mlflow.log_param("max_depth", config["max_depth"])
        elif config["model_type"] == "LogisticRegression":
            model = LogisticRegression(
                C=config["C"],
                solver=config["solver"],
                random_state=42,
                max_iter=1000,  # Increase iterations for convergence
            )
            mlflow.log_param("C", config["C"])
            mlflow.log_param("solver", config["solver"])
        else:  # SVM
            model = SVC(
                kernel=config["kernel"],
                C=config["C"],
                random_state=42,
                probability=True,  # Enable probability estimates
            )
            mlflow.log_param("kernel", config["kernel"])
            mlflow.log_param("C", config["C"])

        # Log common parameters
        mlflow.log_param("model_type", config["model_type"])

        # Fit model
        model.fit(X_train, y_train)

        # Get predictions for signature
        predictions = model.predict(X_train[:5])

        # Create model signature
        signature = infer_signature(X_train[:5], predictions)

        # Log metrics
        mlflow.log_metric("accuracy", accuracy_scores[i])
        mlflow.log_metric("precision", precision_scores[i])
        mlflow.log_metric("recall", recall_scores[i])
        mlflow.log_metric("f1_score", f1_scores[i])

        # Log tags
        mlflow.set_tag("version", versions[i])
        mlflow.set_tag("environment", environments[i])
        mlflow.set_tag("framework", frameworks[i])

        # Log the model with signature and input example
        model_name = f"{config['model_type']}_model_{i}"
        mlflow.sklearn.log_model(
            model,
            name=model_name,
            signature=signature,
            input_example=input_example,
            registered_model_name=f"SearchGuide{config['model_type']}",
        )