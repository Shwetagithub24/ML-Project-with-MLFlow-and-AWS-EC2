from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from mlProject import logger
from pathlib import Path

STAGE_NAME = "Model Trainer Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(Self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
