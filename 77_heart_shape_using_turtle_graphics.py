import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Graphics - Heart Shape")
screen.bgcolor("white")

# Create a turtle object
heart_turtle = turtle.Turtle()
heart_turtle.color("red")
heart_turtle.pensize(3)
heart_turtle.speed(5)

# Move the turtle to the starting position
heart_turtle.penup()
heart_turtle.goto(0, -200)
heart_turtle.pendown()

# Function to draw a heart shape
def draw_heart():
    heart_turtle.begin_fill()
    heart_turtle.left(140)
    heart_turtle.forward(224)
    for _ in range(200):
        heart_turtle.right(1)
        heart_turtle.forward(2)
    heart_turtle.left(120)
    for _ in range(200):
        heart_turtle.right(1)
        heart_turtle.forward(2)
    heart_turtle.forward(224)
    heart_turtle.end_fill()

# Draw the heart
draw_heart()

# Hide the turtle and finish
heart_turtle.hideturtle()

# Close the window when clicked
screen.exitonclick()
