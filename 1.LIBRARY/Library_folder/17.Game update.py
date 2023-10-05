import tkinter as tk
import random
def winCheck(event):
    canvas.itemconfig(rectangle,fill='yellow')
    canvas.create_text(350, 200, text="You win!", font=("Purisa", 26))
root = tk.Tk()
root.geometry("700x300")
frame = tk.Frame()
canvas = tk.Canvas(frame)
x1 = 50
x2 = 110
ranindex = random.randint(0, 9)
for i in range(10):
    if ranindex == i:
        rectangle=canvas.create_oval(x1, 20, x2, 80, fill='blue', tag="win")
    else:
        canvas.create_oval(x1, 20, x2, 80, fill='blue')
    x1 += 60
    x2 = x1 + 60
canvas.tag_bind("win", "<Button-1>", winCheck)
frame.pack(expand=True, fill='both')
canvas.pack(expand=True, fill='both')
root.mainloop()
