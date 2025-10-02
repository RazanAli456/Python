import turtle

turtle.Screen().bgcolor("Green")
turtle.Screen().title("Drawing A Star")
Draw=turtle.Turtle()

Draw.forward(100)
Draw.left(120)
Draw.forward(100)
Draw.left(120)
Draw.forward(100)
Draw.penup()
Draw.right(150)
Draw.forward(60)
Draw.pendown()
Draw.right(90)
Draw.forward(100)
Draw.right(120)
Draw.forward(100)
Draw.right(120)
Draw.forward(100)

turtle.done()