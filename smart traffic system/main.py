import numpy
from detect_cars import Detect_cars
import threading
try:
    o1=Detect_cars()
    o2=Detect_cars()
    o3=Detect_cars()
    t1=threading.Thread(target=o1.detect(name="t1"),daemon=True)
    t2=threading.Thread(target=o2.detect(name="t2"),daemon=True)
    t3=threading.Thread(target=o3.detect(name="t3"),daemon=True)

    t1.start()
    t2.start()
    t3.start()
except:
    pass
