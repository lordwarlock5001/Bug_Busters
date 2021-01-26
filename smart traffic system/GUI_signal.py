import tkinter as tk
class GUI_signal:
    def __init__(self):
        self.root = tk.Tk()
        self.myCanvas_1 = tk.Canvas(self.root)
        self.myCanvas_1.grid(row=1, column=1)
        self.myCanvas_2 = tk.Canvas(self.root)
        self.myCanvas_2.grid(row=2, column=1)
        self.myCanvas_3 = tk.Canvas(self.root)
        self.myCanvas_3.grid(row=3, column=1)
    def create_circle(self,x, y, r, canvasName, color):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1, fill=color)
    def start_(self):
        self.create_circle(82, 82, 80, self.myCanvas_1,"red")
        self.create_circle(82, 82, 80, self.myCanvas_2,"yellow")
        self.create_circle(82, 82, 80, self.myCanvas_3,"green")
        self.root.mainloop()
    def change_state(self,fst,snd,trd):
        self.create_circle(82, 82, 80, self.myCanvas_1, fst)
        self.create_circle(82, 82, 80, self.myCanvas_2, snd)
        self.create_circle(82, 82, 80, self.myCanvas_3, trd)
