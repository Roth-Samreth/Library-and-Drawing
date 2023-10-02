import tkinter as tk
import random
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("Loop draw shape")
canvas = tk.Canvas(frame)
x1 = y1 = 0
y2 = x2 = 60

for j in range(10):
    for i in range(10):
        color = ["red", "yellow", "blue", "green", "yellow"]
        rancolor = random.randint(0, len(color)-1)
        canvas.create_rectangle(x1, y1, x2, y2, fill=color[rancolor])
        y1 += 60
        y2 = y1+60
    x1 += 60
    x2 = x1+60
    y1 = 0
    y2 = y1+60   
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()
