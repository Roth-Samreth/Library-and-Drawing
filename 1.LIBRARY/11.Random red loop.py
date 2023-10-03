import tkinter as tk
import random
root = tk.Tk()
root.geometry("700x300")
frame = tk.Frame()
canvas = tk.Canvas(frame)
x1 = 0
x2 = 60
y1 = 20
y2 = 80
ranindex = random.randint(0,9)
for i  in range(10):
    if ranindex == i:
        canvas.create_oval(x1,y1,x2,y2, fill= 'red')
    else:    
        canvas.create_oval(x1,y1,x2,y2, fill= 'blue')
    x1+=60
    x2= x1 +60
frame.pack(expand=True,fill='both')
canvas.pack(expand=True, fill='both')
root.mainloop()
