import tkinter as tk
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("Drop down circle")
canvas =tk.Canvas(frame)
x1 = 250
x2 = 350
y1 = 50
y2 = 150
for i in range(5):
    canvas.create_oval(x1,y1,x2,y2,fill = 'red')
    y1+=100
    y2= y1+100
frame.pack(expand=True,fill='both')
canvas.pack(expand=True,fill = 'both')
root.mainloop()