import sys
from HSD.components import data_ingestion
from HSD.components.data_transforamation import DataTransformation
from HSD.logger import logging
from HSD.exception import CustomException
from HSD.components.data_ingestion import DataIngestion
from HSD.entity.config_entity import (DataIngestionConfig, DataTransformationConfig)
from HSD.entity.artifact_entity import (DataIngestionArtifacts, DataTransformationArtifacts)

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()

    
    def start_data_ingestion(self)->DataIngestionArtifacts:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:
            logging.info("Getting the data from GCloud Storage bucket")
            data_ingestion = DataIngestion(data_ingestion_config= self.data_ingestion_config)

            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train and valid from GCloud Storage")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifacts
        
        except Exception as e:
            raise CustomException(e, sys) from e
    
    def run_pipeline(self):
        logging.info("Entered the run_pipeline method of TrainPipeline class")
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            
            logging.info("Exited the run_pipeline method of TrainPipeline class")
        
        except Exception as e:
            raise CustomException(e, sys) from e
        
    

    def start_data_transformation(self, data_ingestion_artifacts = DataIngestionArtifacts) -> DataTransformationArtifacts:
        logging.info("Entered the start_data_transformation method of TrainPipeline class")
        try:
            data_transformation = DataTransformation(
                data_ingestion_artifacts = data_ingestion_artifacts,
                data_transformation_config=self.data_transformation_config
            )

            data_transformation_artifacts = data_transformation.initiate_data_transformation()
            
            logging.info("Exited the start_data_transformation method of TrainPipeline class")
            return data_transformation_artifacts

        except Exception as e:
            raise CustomException(e, sys) from e
        
    

    def run_pipeline(self):
        logging.info("Entered the run_pipeline method of TrainPipeline class")
        try:
            data_ingestion_artifacts = self.start_data_ingestion()

            data_transformation_artifacts = self.start_data_transformation(
                data_ingestion_artifacts=data_ingestion_artifacts
            )

            '''model_trainer_artifacts = self.start_model_trainer(
                data_transformation_artifacts=data_transformation_artifacts
            )

            model_evaluation_artifacts = self.start_model_evaluation(model_trainer_artifacts=model_trainer_artifacts,
                                                                    data_transformation_artifacts=data_transformation_artifacts
            ) 

            if not model_evaluation_artifacts.is_model_accepted:
                raise Exception("Trained model is not better than the best model")
            
            model_pusher_artifacts = self.start_model_pusher()
'''




            logging.info("Exited the run_pipeline method of TrainPipeline class") 

        except Exception as e:
            raise CustomException(e, sys) from e


