import numpy as np
from detect_cars import Detect_cars
import GUI_signal as gs
import threading
import time
o1 = Detect_cars(name="left.PNG")
o2 = Detect_cars(name="right.PNG")
o3 = Detect_cars(name="front.PNG")
while True:
    v1=o1.detect(name="left")
    v2 = o2.detect(name="right")
    v3 = o3.detect(name="front")
    dic={"left":v1,"right":v2,"front":v3}
    dic=sorted(dic.items(),key=lambda x: x[1], reverse=True)
    gs.start_main()