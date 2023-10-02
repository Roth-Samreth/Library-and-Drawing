import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
frame = tk.Frame()
frame.master.title("Oval")
canvas = tk.Canvas(frame)
canvas.create_oval(250, 250, 350, 350, fill='#ff00ff')
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()
