from Commons import commons
import cv2
import os
import numpy as np
from PIL import Image

class training_data:

    @staticmethod
    def train_data(self,id):
        try:
            cam = cv2.VideoCapture(0)
        except:
            print "EXCEPTION ! Front camera is busy"

        detector = cv2.CascadeClassifier(commons.face_detector_path)

        training_data_count = 0
        while (True):
            ret, img = cam.read()
            try:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            except:
                print "EXCEPTION ! OpenCV error occured"
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

                # incrementing sample number
                training_data_count = training_data_count + 1
                try:
                    # saving the captured face in the dataset folder
                    cv2.imwrite(commons.datasetpath + "/User." + str(id) + '.' + str(training_data_count) + ".jpg", gray[y:y + h, x:x + w])
                    cv2.imshow('frame', img)
                except:
                    print "EXCEPTION ! OpenCV error occured"
            try:
                # wait for 100 miliseconds
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                # break if required no of samples shave been captured
                elif training_data_count > commons.max_training_data_count:
                    break
            except:
                print "EXCEPTION ! OpenCV error occured on timeout"

        try:
            cam.release()
            cv2.destroyAllWindows()
        except:
            print "EXCEPTION ! Cannot release cam"