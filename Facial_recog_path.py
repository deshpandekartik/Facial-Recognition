import cv2
import numpy as np
from Commons import commons
import os

class facial_recog_path:

    @staticmethod
    def perform_operation(self, person_folder_path):
        recognizer = cv2.createLBPHFaceRecognizer()
        recognizer.load(commons.parsed_dataset + '/trainner.yml')

        for filename in os.listdir(person_folder_path):
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):

                font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
                # Create the cascade
                faceCascade = cv2.CascadeClassifier(commons.face_detector_path)

                # Read the image
                image = cv2.imread(person_folder_path + "/" + filename)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                # DETECT faces in image
                faces = faceCascade.detectMultiScale(gray, 1.3, 5)

                for (x, y, w, h) in faces:

                    cv2.rectangle(image, (x, y), (x + w, y + h), (225, 0, 0), 2)
                    personid, conf = recognizer.predict(gray[y:y + h, x:x + w])
                    if (conf != "" and personid != ""):
                        if personid in commons.name_id_mapping:
                            personname = commons.name_id_mapping[personid]
                            cv2.cv.PutText(cv2.cv.fromarray(im), str(personname), (x, y + h), font, 255)
                cv2.imshow('im', image)
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break

        cv2.destroyAllWindows()