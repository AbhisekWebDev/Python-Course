import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Graphics Demo")
screen.bgcolor("lightblue")

# Create a turtle object
star_turtle = turtle.Turtle()
star_turtle.color("orange")
star_turtle.pensize(3)
star_turtle.speed(5)

# Draw a star
for _ in range(5):
    star_turtle.forward(100)
    star_turtle.right(144)

# Hide the turtle and display the result
star_turtle.hideturtle()

# Close the window when clicked
screen.exitonclick()