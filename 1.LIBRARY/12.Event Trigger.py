import tkinter as tk
def eventTriger(event):
    print("I clicked at ",event.x,event.y)
root = tk.Tk()
root.geometry("400x400")
frame = tk.Frame()
frame.master.title("X and Y event checker")
canvas = tk.Canvas(frame)
canvas.create_oval(50,50,300,300, fill ='red', tag= "Mytarget")
canvas.tag_bind("Mytarget","<Button-1>",eventTriger)
frame.pack(expand=True, fill= 'both')
canvas.pack(expand=True, fill='both')
root.mainloop()