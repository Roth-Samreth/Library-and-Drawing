import tkinter as tk
import random
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("UI Oval")
canvas = tk.Canvas(frame)
x1 = y1 = 100
x2 = y2 = 500
color = ["red","yellow","blue","green","yellow"]
for i in range(5):
    rancolor = random.randint(0,len(color)-1)
    canvas.create_oval(x1,x1,x2,x2, fill= color[rancolor])
    x1+= 50
    x2-= 50
canvas.pack(expand=True, fill = 'both')
frame.pack(expand=True, fill= "both")
root.mainloop()