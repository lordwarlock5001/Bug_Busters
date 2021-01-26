import numpy as np
import cv2
img = cv2.imread('test.PNG', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 600, 200)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 20, minLineLength=400, maxLineGap=50)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
cv2.imshow("Result Image", img)
cv2.waitKey(0)