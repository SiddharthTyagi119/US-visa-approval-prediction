from dataclasses import dataclass
from us_visa.exception import USvisaException
from us_visa.logger import logging

@dataclass
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str 