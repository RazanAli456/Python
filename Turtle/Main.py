import turtle
turtle.Screen().bgcolor("green")
turtle.Screen().title("Drawing a hexagon")
turtle.Screen().setup(width=400,height=300)
sides=6
angle=360/sides
draw=turtle.Turtle()
for i in range(sides):
    draw.forward(80)
    draw.right(angle)
turtle.done()
