import tkinter as tk
root=  tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("Line circle")
canvas = tk.Canvas(frame)
x1 =50
x2 = 150
y1 =250
y2 = 350
for i in range(5):
    canvas.create_oval(x1,y1,x2,y2, fill = 'blue')
    x1 +=100
    x2 = x1+100
frame.pack(expand=True, fill= 'both')
canvas.pack(expand=True, fill='both')
root.mainloop()
