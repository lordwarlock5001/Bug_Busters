import numpy as np
from detect_cars import Detect_cars
import GUI_signal as gs
import threading
import time
o1 = Detect_cars(name="left.PNG")
o2 = Detect_cars(name="right.PNG")
o3 = Detect_cars(name="front.PNG")
def patttern(dic):
    t1 = threading.Thread(target=gs.start_main, name="t1", args=(0,"left",), daemon=True)
    t1.start()
    t2 = threading.Thread(target=gs.start_main, name="t2", args=(30,"right",), daemon=True)
    t2.start()
    t3 = threading.Thread(target=gs.start_main, name="t3", args=(60,"front",), daemon=True)
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    del t1
    del t2
    del t3
while True:
    v1=o1.detect(name="left")
    v2 = o2.detect(name="right")
    v3 = o3.detect(name="front")
    dic={"left":v1,"right":v2,"front":v3}
    dic=sorted(dic.items(),key=lambda x: x[1], reverse=True)
    patttern(dic)