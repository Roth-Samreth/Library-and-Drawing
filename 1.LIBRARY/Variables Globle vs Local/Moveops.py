import tkinter as tk

def button_clicked():
    print("Button Clicked!")

window = tk.Tk()
window.geometry('500x500')
frame = tk.Frame(window, width=500, height=500)
frame.pack()

canvas = tk.Canvas(frame, width=500, height=500)
canvas.pack()

ball = canvas.create_oval(190, 190, 210, 210, fill="green")
wall = canvas.create_rectangle(300, 50, 320,300 , fill="black", tags="wall")
def changeball(event):
    oval_coords = canvas.coords(ball)
    wall_coords = canvas.coords(wall)
    if event.keysym == "Right":
        if (oval_coords[2]< wall_coords[0] or oval_coords[1]>=wall_coords[3] or oval_coords[3] <= wall_coords[1] or oval_coords[0]>=wall_coords[2] ):
            canvas.move(ball, 10, 0)
    elif event.keysym == "Left":
        if (oval_coords[0]> wall_coords[2] or oval_coords[1]>=wall_coords[3] or oval_coords[3] <= wall_coords[1] or oval_coords[0]<wall_coords[2] ):
            canvas.move(ball, -10, 0)
    elif event.keysym == "Up":
        if (oval_coords[2]<= wall_coords[0] or oval_coords[1]>wall_coords[3] or oval_coords[3] <= wall_coords[1] or oval_coords[0]>=wall_coords[2] ):
            canvas.move(ball, 0, -10)
    elif event.keysym == "Down":
        if (oval_coords[2]<= wall_coords[0] or oval_coords[1]>=wall_coords[3] or oval_coords[3] < wall_coords[1] or oval_coords[0]>=wall_coords[2] ):
            canvas.move(ball, 0, 10)          

window.bind("<Key>", changeball)

window.mainloop()