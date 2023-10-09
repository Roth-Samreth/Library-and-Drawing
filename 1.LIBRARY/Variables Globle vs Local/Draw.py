import tkinter as tk
import random 

color = ['red', 'blue', 'pink', 'black', 'purple', 'yellow', 'orange', 'green', 'brown']

def draw(event):

    canvas.create_oval(event.x - 10, event.y-10, event.x+20, event.y+20, fill=random.choice(color), outline='')
window = tk.Tk()
window.title('Draw Picture')
window.geometry('1000x600')
frame = tk.Frame(window, width=1000, height=600)
frame.pack()
canvas = tk.Canvas(frame, width=1000, height=600, bg='pink')
canvas.pack(pady=30)
canvas.bind('<B1-Motion>', draw)
window.mainloop()