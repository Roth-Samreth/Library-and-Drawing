import tkinter as tk

root = tk.Tk()
root.geometry("700x500")
frame = tk.Frame()
frame.master.title("Hello My first window")
canvas = tk.Canvas(frame)
canvas.create_rectangle(0, 0, 50, 100, fill="#000")
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()
