from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
import joblib
from pathlib import Path
import mlflow
import mlflow.sklearn

# Configure mlflow tracking (using SQLite database)
mlflow.set_tracking_uri("sqlite:///mlflow.db")

# Group related training runs under one experiment
mlflow.set_experiment("iris-classification")



"""Train an Iris classifier, report its accuracy, and save it to models/."""
iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data,
    iris.target,
    test_size=0.2,
    random_state=42,
    stratify=iris.target,
)

n_estimators= 10
random_state= 42

model_parameters= {
    "model_type": "RandomForestClassifier",
    "n_estimators": n_estimators,
    "random_state": random_state,
    "test_size": 0.2    
}
# Start a tracked training run
with mlflow.start_run() as run:
    # Record the rtraining configuration before model fitting
    mlflow.log_params(model_parameters)

    # Build classifier using selected parameters
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    print(f"Test accuracy: {accuracy}")

    # Calcualte the precision
    precision = precision_score(y_test, predictions, average="macro", zero_division=0)
    print(f"Precision: {precision}")

    # Calculate the recall
    recall = recall_score(y_test, predictions, average="macro", zero_division=0)
    print(f"Recall: {recall}")

    mlflow.log_metrics({
        "test_accuracy":accuracy,
        "test_precision": precision,
        "test_recall": recall
    })

    # Save the trained model locally
    model_dir = Path(__file__).resolve().parent / "models"
    model_dir.mkdir(parents=True, exist_ok=True)
    model_path = model_dir / "iris_random_forest_model.joblib"
    joblib.dump(model, model_path)
    print(f"Model saved to: {model_path}")

    # Log the model to MLflow
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model",
        skops_trusted_types=["sklearn.tree._tree.Tree"]
    )
    print("✅ Model logged to MLflow")

    run_id = run.info.run_id
    print(f"MLflow Run ID: {run_id}")

# Register the model and set champion alias (outside the run context)
try:
    client = mlflow.MlflowClient()
    model_uri = f"runs:/{run_id}/model"
    
    # Register the model
    registered_model = mlflow.register_model(
        model_uri=model_uri,
        name="iris-classifier"
    )
    print(f"✅ Model registered as iris-classifier version {registered_model.version}")
    
    # Set champion alias
    client.set_registered_model_alias(
        name="iris-classifier",
        alias="champion",
        version=registered_model.version
    )
    print(f"✅ Set champion alias to version {registered_model.version}")
except Exception as e:
    print(f"⚠️  Warning: Could not register model or set alias: {e}")

print(f"Training completed successfully!")