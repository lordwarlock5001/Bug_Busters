import tkinter as tk
import time
root=tk.Tk()
myCanvas_1 = tk.Canvas(root)
myCanvas_1.grid(row=1,column=1)
myCanvas_2 = tk.Canvas(root)
myCanvas_2.grid(row=2,column=1)
myCanvas_3 = tk.Canvas(root)
myCanvas_3.grid(row=3,column=1)
def create_circle(x, y, r, canvasName,color): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1,fill=color)

create_circle(82, 82, 80, myCanvas_1,"red")
create_circle(82, 82, 80, myCanvas_2,"yellow")
create_circle(82, 82, 80, myCanvas_3,"green")
root.mainloop()