# import tkinter
# import random
# c = tkinter.Canvas(width = 400, height = 300)
# c.pack()

# def klik(event):
#     global x, y, farba, circ, r
#     r = 50      #circle diameter
#     x, y = event.x, event.y     #clicked position
#     color = '#{:06x}'.format(random.randrange(256 ** 3))        #random  color picker
#     circ = c.create_oval(x - r, y - r, x + r, y + r, fill=color)         #print circle
#     print(x, y, farba)      #check clicked coordinates, not important
#     if r < 50:      #reset size after each circle
#         r = 50
#     shrink()

# def shrink():
#     global circ, x, y, r
#     print(r)        #check if countdown runs correctly
#     if r > 0:
#         r -= 1      #diameter shrinking
#         c.coords(circ, x-r, y-r, x+r, y+r)      #changing circle size
#         c.after(100, shrink)        #timer, size 1pt smaller until size is 0

# c.bind('<Button-1>', klik)
# tkinter.mainloop()

import tkinter as tk
import random
root = tk.Tk()
root.geometry('600x600')
frame = tk.Frame()
frame.master.title('Game UI')
canvas = tk.Canvas(frame)
colors = ['red','green','blue','pink']
def draw(event):
      canvas.create_oval(event.x-25,event.y-25,event.x+25,event.y+25,fill=colors[random.randint(0,len(colors)-1)])
      
canvas.create_rectangle(0,0,600,600, fill='white', tags='value')
canvas.tag_bind('value','<Button-1>', draw)
frame.pack(expand=True,fill='both')
canvas.pack(expand=True,fill='both')
root.mainloop()