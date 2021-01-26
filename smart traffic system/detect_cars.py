from imageai.Detection import VideoObjectDetection,ObjectDetection
import os
import cv2
# Get current working directory
curDir = os.getcwd()
# Initialize video capture (webcam)
camera = cv2.VideoCapture("video/test_footage.mp4")
# Initialize imageAI objects and files
detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(curDir, "yolo.h5"))
detector.loadModel()
# Start object detection and print frames
video_path = detector.detectObjectsFromVideo(camera_input=camera,
                                output_file_path=os.path.join(curDir, "cam1")
                                , frames_per_second=4, log_progress=True)
print(video_path)