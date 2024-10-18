import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=100, height=100, startx = 0, starty = 0)
tina = turtle.Turtle()

i = 0
tri = 3
rect = 4
pent = 5
hex = 6
hept = 7
oct = 8
sides = hept
angle = 360/sides
def draw_polygon(sides):
    for i in range(10):
        tina.forward(i*1.5)
        tina.left(angle)


draw_polygon(sides)






turtle.exitonclick()