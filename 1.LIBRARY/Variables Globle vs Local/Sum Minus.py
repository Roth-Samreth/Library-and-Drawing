from tkinter import *
total = 0
root = Tk()
root.geometry("400x400")
frame = Frame()
frame.master.title("Sum Minus")
canvas = Canvas(frame)
result =canvas.create_text(100,100,text="Result", font=(25))
def sum():
    global total
    total+=2      
def Minus():
    global total
    total-=2
frame.pack()
canvas.pack()
def sumMinus(event):
    if event.keysym == "w":
        sum()
    elif event.keysym == "s":
        Minus()
    canvas.itemconfig(result,text=str(total))
root.bind("<Key>",sumMinus)
root.mainloop()