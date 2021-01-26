import numpy
from detect_cars import Detect_cars
o1=Detect_cars(name="left.PNG")
o2=Detect_cars(name="right.PNG")
o3=Detect_cars(name="front.PNG")
v1=o1.detect(name="t1")
v2 = o2.detect(name="t2")
v3 = o3.detect(name="t3")
print(v1,",",v2,",",v3,",")
