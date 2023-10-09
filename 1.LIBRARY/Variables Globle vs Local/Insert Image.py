import tkinter as tk
from PIL import Image, ImageTk
window = tk.Tk()
window.title('Image')
window.geometry('1024x600')
frame = tk.Frame(window, width=1024, height=600)
frame.pack()
getImageFile = Image.open('Image/Cover.jpg')
img = ImageTk. PhotoImage(getImageFile)
label = tk.Label(frame, image=img)
label.pack()
window.mainloop()
