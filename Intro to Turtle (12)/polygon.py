import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()

num_sides = 8
side_length = 20
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.left(angle)


turtle.done()