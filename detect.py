import cv2
import sys

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


if __name__ == '__main__':
    if len(sys.argv) != 2:
    	print "ERROR ! Please enter a image path"
    	#sys.exit(0)

    #IMAGEPATH = sys.argv[1]
    IMAGEPATH = "sample_images/test2.jpg"
    detect_face(IMAGEPATH)


