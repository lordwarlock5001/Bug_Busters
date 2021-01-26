from imageai.Detection import VideoObjectDetection,ObjectDetection
import os
import cv2
class Detect_cars:
    def __init__(self,name):
        self.curD=os.getcwd()
        self.footage=cv2.imread("video/"+name)
        self.detector=ObjectDetection()
        self.detector.setModelTypeAsYOLOv3()
        self.detector.setModelPath(os.path.join(self.curD,"yolo.h5"))
        self.cust=self.detector.CustomObjects(car=True,motorcycle=True,truck=True)
        self.detector.loadModel()

    def detect(self,name):
            image_path=self.detector.detectObjectsFromImage(custom_objects=self.cust,display_percentage_probability=False,display_object_name=False,input_image=self.footage,input_type="array",output_image_path="image.jpg")
            image=cv2.imread("image.jpg")
            cv2.imshow(name,image)
            cv2.waitKey(1000)
            return len(image_path)

