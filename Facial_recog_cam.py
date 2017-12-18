import cv2
import numpy as np
from Commons import commons

class facial_recog_cam:

    @staticmethod
    def perform_recognition(self):
        recognizer = cv2.createLBPHFaceRecognizer()
        recognizer.load(commons.parsed_dataset + '/trainner.yml')
        faceCascade = cv2.CascadeClassifier(commons.face_detector_path);


        cam = cv2.VideoCapture(0)
        font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
        while True:
            ret, im =cam.read()
            gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            faces=faceCascade.detectMultiScale(gray, 1.2,5)
            for(x,y,w,h) in faces:
                cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
                personid, conf = recognizer.predict(gray[y:y+h,x:x+w])
                if(conf != "" and personid != ""):
                    if personid in commons.name_id_mapping:
                        personname = commons.name_id_mapping[personid]
                else:
                    personname="Unknown"
                cv2.cv.PutText(cv2.cv.fromarray(im),str(personname), (x,y+h),font, 255)
            cv2.imshow('im',im)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
        cam.release()
        cv2.destroyAllWindows()