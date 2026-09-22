import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1)

colors = ["RED"]

# Person's name
name = "SUMIT"

# Display colourful name above the heart
t.penup()

# Calculate starting position so the name is centered
letter_width = 25
start_x = -(len(name) * letter_width) / 2
y_position = 300

for letter in name:
    t.goto(start_x, y_position)

    # Random heart-like color
    t.color(random.choice(colors))

    t.write(letter,
            align="center",
            font=("Arial", 28, "bold"))

    start_x += letter_width


# Draw the heart
for i in range(120):
    t.penup()
    t.goto(0, 0)

    angle = i * (math.pi * 2) / 120

    # Original heart coordinates
    x = 16 * (math.sin(angle) ** 3) * 12

    y = (13 * math.cos(angle)
         - 5 * math.cos(2 * angle)
         - 2 * math.cos(3 * angle)
         - math.cos(4 * angle)) * 12

    # Rotate heart
    new_x = -y
    new_y = x

    c = random.choice(colors)
    t.color(c)
    t.pendown()

    t.goto(new_y, -new_x)

    for _ in range(8):
        t.forward(6)
        t.backward(6)
        t.right(90)

turtle.done()
