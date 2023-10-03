import tkinter as tk
# root = tk.Tk()
# root.geometry("600x600")
# frame = tk.Frame()
# frame.master.title("Down left circle")
# canvas = tk.Canvas(frame)
# x1 = 400
# x2 = 500
# y1 = 50
# y2 = 150
# for i in range(5):
#     canvas.create_oval(x1,y1,x2,y2, fill = 'red')
#     x1-=70
#     x2-=70
#     y1+=70
#     y2=y1+100
# frame.pack(expand=True, fill = 'both')
# canvas.pack(expand=True, fill= 'both')
# root.mainloop()


root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("Down left circle")
canvas = tk.Canvas(frame)
x1 = 0
x2 = 100
y1 = 500
y2 = 600
for i in range(5):
    canvas.create_oval(x1,y1,x2,y2, fill = 'red')
    x1+=100
    x2=x1+100
    y1-=100
    y2-=100
frame.pack(expand=True, fill = 'both')
canvas.pack(expand=True, fill= 'both')
root.mainloop()