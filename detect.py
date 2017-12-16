import cv2
import sys
import os
import shutil

CASCADE_DIR = "cascade-files/haarcascades/"

def detect_face(imagePath):

    # haarcascade_frontalface_default.xml is a frontal face detection xml file from opencv
    face_cascade_path = CASCADE_DIR + "haarcascade_frontalface_default.xml"

    # Create the cascade
    faceCascade = cv2.CascadeClassifier(face_cascade_path)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    print faces
    print("Found {0} faces!".format(len(faces)))

    for (x, y, w, h) in faces:
    	img = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Faces found", image)
    cv2.waitKey(0)

def create_dataset(person_folder_path):
    personname = os.path.basename(os.path.normpath(person_folder_path))

    DATASETPATH = "dataset/" + personname + "/"
    sampleNum = 0

    if not os.path.exists(DATASETPATH):
        os.makedirs(DATASETPATH)
    else:
        shutil.rmtree(DATASETPATH, ignore_errors=True)

    for filename in os.listdir(person_folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            face_cascade_path = CASCADE_DIR + "haarcascade_frontalface_default.xml"

            # Create the cascade
            faceCascade = cv2.CascadeClassifier(face_cascade_path)

            # Read the image
            image = cv2.imread(person_folder_path + "/" + filename)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # DETECT faces in image
            faces = faceCascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder
                cv2.imwrite(DATASETPATH + "record-" + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

if __name__ == '__main__':
    if len(sys.argv) != 2:
    	print "ERROR ! Please enter a image path"
    	#sys.exit(0)

    #IMAGEPATH = sys.argv[1]
    IMAGEPATH = "sample_images/test1.jpg"
    #detect_face(IMAGEPATH)
    create_dataset("sample_images/kartik/")