# Tash Me with a Click
# 
# Update your Tash Me program ( copy your old program here )to put 
# the moustache where you click on the screen.
#
# Hint: See 08a_More Turtle Programs, section 'Click on the Screen'
 
... # Your code here

import turtle
turtle.setup(525, 250, startx = 0, starty = 0)
tina = turtle.Turtle()
tina.speed(1000000000000000000000000000000000000000000)

def circle_fractal():
    for i in range(10000000000000000000000000000000000000000000000000000000000000000000):
        print("loop iteration", i)
        tina.pencolor("green")
        tina.circle(i*0.1)
