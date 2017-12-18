import cv2,os
import numpy as np
from PIL import Image
import shutil

class commons:

    face_detector_path = "cascade-files/haarcascades/haarcascade_frontalface_default.xml"
    max_training_data_count = 20
    name_id_mapping = {}
    person_id_count = 0

    datasetpath = "dataset/"
    parsed_dataset = "trainner/"

    @staticmethod
    def directory_creations(path):
        if os.path.exists(path):
            shutil.rmtree(path, ignore_errors=True)
            os.makedirs(path)
        else:
            os.makedirs(path)


    # I will create a directory structure for you, and initialize all required variables
    @staticmethod
    def initialize(self):

        # creates dir structure
        self.directory_creations(self.datasetpath)
        self.directory_creations(self.parsed_dataset)

        # initialize, changing variables
        self.max_training_data_count = 0
        self.name_id_mapping = {}
        self.person_id_count = 0