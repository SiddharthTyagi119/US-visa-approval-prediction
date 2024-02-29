from us_visa.pipeline.training_pipeline import TrainPipeline
from us_visa.exception import USvisaException
from us_visa.logger import logging

pipline  = TrainPipeline()
pipline.run_pipeline()