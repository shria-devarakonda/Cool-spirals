import tkinter
#import tkinter to avoid the window close instantly after the spiral is rendered
from turtle import *
import random
t = Turtle()
x = 0
setup(500, 500)

t.hideturtle()
t.speed(0)

r = random.randrange(30, 180, 30) 
print(r)
for i in range(100):
    t.forward(5 * i)
    t.right(r)

tkinter.mainloop()
