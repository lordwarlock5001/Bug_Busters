import cv2
class Detect_cars:
    def __init__(self):
        self.cap=cv2.VideoCapture("video/test_footage.mp4")
        self.car_cass=cv2.CascadeClassifier('cars.xml')

    def detect(self):
        while True:
            ret, frames = self.cap.read()

            # convert to gray scale of each frames
            gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

            # Detects cars of different sizes in the input image
            cars = self.car_cass.detectMultiScale(gray, 1.1, 1)

            # To draw a rectangle in each cars
            for (x, y, w, h) in cars:
                cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 0, 255), 2)

                # Display frames in a window
            cv2.imshow('video2', frames)
            #cv2.waitKey(1)
            # Wait for Esc key to stop
            if cv2.waitKey(33) == 27:
                break

    # De-allocate any associated memory usage
    cv2.destroyAllWindows()

obj=Detect_cars()
obj.detect()