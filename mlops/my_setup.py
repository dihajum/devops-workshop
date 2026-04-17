import mlflow
mlflow.set_tracking_uri("http://192.168.0.102:5000")
mlflow.enable_system_metrics_logging()
