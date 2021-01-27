import tkinter as tk
import time
import threading
class GUI_signal:
    def __init__(self,name):
        self.root = tk.Tk()
        self.seco=0
        self.label_name=tk.Label(self.root,text=name)
        self.label_name.grid(row=1,column=1)
        self.label_timer=tk.Label(self.root,text="00",font=("",50),fg="#009933")
        self.label_timer.grid(row=2,column=1)
        self.myCanvas_1 = tk.Canvas(self.root,width=102,height=102)
        self.myCanvas_1.grid(row=3, column=1)
        self.myCanvas_2 = tk.Canvas(self.root,width=102,height=102)
        self.myCanvas_2.grid(row=4, column=1)
        self.myCanvas_3 = tk.Canvas(self.root,width=102,height=102)
        self.myCanvas_3.grid(row=5, column=1)
    def timer(self,sec,dele):
        s=0
        self.change_state("red","grey","grey")
        while s<=sec:
            self.label_timer.configure(text=sec-s)
            print(s)
            time.sleep(1)
            s+=1
        s=0
        self.change_state("grey", "yellow", "grey")
        while s<=5:
            time.sleep(1)
            s += 1
        self.change_state("grey","grey","green")
        self.green_red(dele)
    def create_circle(self,x, y, r, canvasName, color):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1, fill=color)
    def start_(self):
        self.create_circle(52, 52, 50, self.myCanvas_1,"red")
        self.create_circle(52, 52, 50, self.myCanvas_2,"yellow")
        self.create_circle(52, 52, 50, self.myCanvas_3,"green")

    def change_state(self,fst,snd,trd):
        self.create_circle(52, 52, 50, self.myCanvas_1, fst)
        self.create_circle(52, 52, 50, self.myCanvas_2, snd)
        self.create_circle(52, 52, 50, self.myCanvas_3, trd)
    def start_loop(self):
        self.root.mainloop()
    def change_in_pattern(self):
        pass
    def __del__(self):
        self.root.destroy()
    def green_red(self,dele):
        s = 0
        while s <= 30:
            time.sleep(1)
            s += 1
        self.change_state("grey", "yellow", "grey")
        s = 0
        while s <= 5:
            time.sleep(1)
            s += 1
        self.change_state("red", "grey", "grey")
        s = 5
        while s <= dele:
            self.label_timer.configure(text=dele-s)
            time.sleep(1)
            s += 1
        self.root.destroy()
def start_main(sec,name,dele):
    obj=GUI_signal(name)
    obj.start_()
    if sec==0:
        obj.change_state("grey","grey","green")
        t1 = threading.Thread(target=obj.green_red,args=(dele,), name="t1", daemon=True)
        t1.start()
    else:
        t1=threading.Thread(target=obj.timer,name="t1",args=(sec,dele,),daemon=True)
        t1.start()
    obj.start_loop()


