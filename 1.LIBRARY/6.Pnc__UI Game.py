import tkinter as tk
import random
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("UI Game")
canvas = tk.Canvas(frame)
# canvas.create_rectangle(50, 550, 550, 50, fill='red')
# canvas.create_rectangle(100, 500, 500, 100, fill='blue')
# canvas.create_rectangle(150, 450, 450, 150, fill='green')
# canvas.create_rectangle(200, 400, 400, 200, fill='yellow')
# canvas.create_rectangle(250, 350, 350, 250, fill='green')
x1 = y1 = 100
x2 = y2 = 500
color = ["red","yellow","blue","green","yellow"]

for i in range(5):
    rancolor = random.randint(0,len(color)-1)
    canvas.create_rectangle(x1,x1,x2,x2, fill= color[rancolor])
    x1+= 50
    x2-= 50
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()
