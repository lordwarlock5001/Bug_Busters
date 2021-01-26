from imageai.Detection import VideoObjectDetection,ObjectDetection
import os
import cv2
import numpy as np
class Detect_cars:
    def __init__(self):
        self.curD=os.getcwd()
        self.footage=cv2.VideoCapture("video/test_footage.mp4")
        self.detector=ObjectDetection()
        self.detector.setModelTypeAsYOLOv3()
        self.detector.setModelPath(os.path.join(self.curD,"yolo.h5"))
        self.cust=self.detector.CustomObjects(car=True,motorcycle=True,truck=True)
        self.detector.loadModel()

    def detect(self):
        while True:
            suc,frame=self.footage.read()

            image_path=self.detector.detectObjectsFromImage(custom_objects=self.cust,display_percentage_probability=False,display_object_name=False,input_image=frame,input_type="array",output_image_path="image.jpg")
            print(len(image_path))
            image=cv2.imread("image.jpg")
            cv2.imshow("image",image)
            k = cv2.waitKey(1) & 0xFF
            # press 'q' to exit
            if k == ord('q'):
                break
obj=Detect_cars()
obj.detect()