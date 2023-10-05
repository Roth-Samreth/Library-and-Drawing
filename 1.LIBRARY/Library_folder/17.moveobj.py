import tkinter as tk
root = tk.Tk()
root.geometry("1080x600")
frame = tk.Frame()
frame.master.title("Movement")
canvas = tk.Canvas(frame)
move = canvas.create_rectangle(10,10,40,40,fill='red')
canvas.pack(expand=True,fill='both')
frame.pack(expand=True,fill='both')
root.bind("<KeyPress>")
if "<KeyPress-Up>":
    canvas.move(move,0,-10)
if "<D<KeyPress-Down>":
    canvas.move(move,0,10)
root.mainloop()
