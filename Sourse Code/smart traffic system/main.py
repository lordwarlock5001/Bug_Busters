from detect_cars import Detect_cars
import GUI_signal as gs
import threading
import time
o1 = Detect_cars(name="left.PNG")
o2 = Detect_cars(name="right.PNG")
o3 = Detect_cars(name="front.PNG")
sp=[0,20,50]
def patttern(dic):
    k=0
    j=0
    ii=0
    for i in dic:
        t1 = threading.Thread(target=gs.start_main, name="t1", args=(sp[ii], i[0],(60-sp[ii])-j), daemon=True)
        t1.start()
        k+=30
        j+=7
        ii+=1
    time.sleep(k-30)
while True:
    v1=o1.detect(name="left")
    v2 = o2.detect(name="right")
    v3 = o3.detect(name="front")
    dic={"left":v1,"right":v2,"front":v3}
    dic=sorted(dic.items(),key=lambda x: x[1], reverse=True)
    patttern(dic)