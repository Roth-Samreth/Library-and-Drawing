import tkinter as tk
def Circle(event):
    print("I clicked circle ")
def rect(event):
    print("I clicked on rectangle ")
def square(event):
    print("I clicked on square")
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("X and Y event checker")
canvas = tk.Canvas(frame)
canvas.create_oval(50,50,100,100, fill ='red', tag= "circle")
canvas.create_rectangle(350,50,450,150, fill='blue', tag= "square")
canvas.create_rectangle(100,300,500,400, fill='yellow',tag= "rectangle")
canvas.tag_bind("circle","<Button-1>",Circle)
canvas.tag_bind("square","<Button-1>",square)
canvas.tag_bind("rectangle","<Button-1>",rect)
frame.pack(expand=True, fill= 'both')
canvas.pack(expand=True, fill='both')
root.mainloop()