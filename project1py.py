import turtle

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("black")
turtle.speed(0)

# Draw a flower pattern
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for _ in range(36):
    for _ in range(6):
        turtle.color(colors[_ % 7])
        turtle.forward(100)
        turtle.left(60)
    turtle.right(10)

# Exit on click
turtle.exitonclick()
