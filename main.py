from Training_data import training_data
from Commons import commons
import sys
from Facial_recog_cam import facial_recog_cam
from Facial_recog_path import facial_recog_path

if __name__ == '__main__':

    # first initialize, all common variables
    commons.initialize(commons)

    print "1. Populate data "
    print "2. Perform facial recognition from front camera"
    print "3. Perform facial recognition from a set of images"
    print "4. Exit"
    # user console
    while True:
        rawuserinput = raw_input("\n Please enter one of the above commands:\n")

        if rawuserinput != "":
            if rawuserinput == "1":
                # take input from user , for name
                person_name = raw_input('Enter your name')
                commons.person_id_count = commons.person_id_count + 1

                # store the mapping in dict
                commons.name_id_mapping[commons.person_id_count] = person_name

                # call func to populate data set by capturing images
                training_data.train_data(training_data,commons.person_id_count)

            elif rawuserinput == "2":
                facial_recog_cam.perform_recognition()
            elif rawuserinput == "3":
                path = raw_input("Enter path..")
                facial_recog_path.perform_operation(path)
            elif rawuserinput == "4":
                print "EXIT ! On user input"
                sys.exit(0)