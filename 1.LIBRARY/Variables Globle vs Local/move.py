

import tkinter as tk

window = tk.Tk()
window.geometry('600x400')
window.title('Event')

#frame
frame = tk.Frame(window, width=600, height=400)
frame.pack()

#canvas
canvas = tk.Canvas(frame, width=600, height=400, bg="pink")
canvas.pack()

id = canvas.create_oval(10, 10, 60, 60, fill='red')


def moveRight():
    if canvas.coords(id)[2] < 590:
        canvas.move(id, +10, 0)
def moveLeft():
    if canvas.coords(id)[0] > 10:
        canvas.move(id, -10, 0)
def moveUp():
    if canvas.coords(id)[1] > 10:
        canvas.move(id, 0, -10)
def moveDown():
    if canvas.coords(id)[3] < 390:
        canvas.move(id, 0, +10)

def move(event):
    if event.keysym == "d":
        moveRight()
    elif event.keysym == 'a':
        moveLeft()
    elif event.keysym == 'w':
        moveUp()
    elif event.keysym == 's':
        moveDown()
window.bind('<Key>', move)




window.bind('<Right>')

window.mainloop()