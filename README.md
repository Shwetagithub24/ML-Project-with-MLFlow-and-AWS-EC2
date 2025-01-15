# ML-Project-with-MLFlow-and-AWS-EC2

## Workflow


1. Update config.yaml in config folder
2. Update schema.yaml
3. Update params.yaml  
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py



# Dagshub
# MLFlow Tracking URI
- import dagshub
- dagshub.init(repo_owner='Shwetagithub24' repo_name='ML-Project-with-MLFlow-and-AWS-EC2', mlflow=True)

- import mlflow
- with mlflow.start_run():
-  mlflow.log_param('parameter name', 'value')
-  mlflow.log_metric('metric name', 1)

# set MLFLOW_TRACKING_URI=https://dagshub.com/Shwetagithub24/ML-Project-with-MLFlow-and-AWS-EC2.mlflow

# set MLFLOW_TRACKING_USERNAME = "Shwetagithub24"
# set MLFLOW_TRACKING_PASSWORD = "Swamisamarth@11"
