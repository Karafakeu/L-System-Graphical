from turtle import Screen, Turtle
import random

def draw_lsystem(LString, angle, length, turtle, colorCodes, randomly):
    turtle.pencolor("black")
    stack = []
    min_x, min_y, max_x, max_y = 0, 0, 0, 0

    skip = False
    # main loop for drawing
    for index, letter in enumerate(LString):
        angleFactor = angle // 10
        # because of coloring
        if skip:
            skip = False
            continue
        if letter == "C":
            currentColorCode = LString[index + 1]
            if currentColorCode in colorCodes: # C used to identify color
                skip = True
                turtle.pencolor(colorCodes[currentColorCode].lower())
            else: # if C is only used as a letter and not to identify color
                skip = False
                turtle.forward(length)
        elif letter == "+":
            newAngle = angle + (random.randint(-angleFactor, angleFactor) if randomly else 0)
            turtle.right(newAngle)
        elif letter == "-":
            newAngle = angle + (random.randint(-angleFactor, angleFactor) if randomly else 0)
            turtle.left(newAngle)
        elif letter == "[":
            stack.append((turtle.pos(), turtle.heading()))
        elif letter == "]":
            pos, heading = stack.pop()
            turtle.penup()
            turtle.setpos(pos)
            turtle.setheading(heading)
            turtle.pendown()
        else:
            turtle.forward(length)
    
        # save the coordinates of the drawing to scale the picture later
        x, y = turtle.pos()
        min_x, min_y = min(min_x, x), min(min_y, y)
        max_x, max_y = max(max_x, x), max(max_y, y)

    return min_x, min_y, max_x, max_y

def drawSystem(LString, angle, length, colorCodes, randomly):
    # definitions
    screen = Screen()
    screen.mode("world")
    turtle = Turtle()

    # more definitions
    screen.title("L-System Graphical Representation")
    turtle.shape("circle")
    turtle.shapesize(0.25)
    turtle.setheading(90)
    turtle.speed(9999)
    turtle.pensize(2)

    # whole functionality
    # draw the shape
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    min_x, min_y, max_x, max_y = draw_lsystem(LString, angle, length, turtle, colorCodes, randomly)

    # scale the world
    screen.setworldcoordinates(min_x, min_y, max_x, max_y)

    turtle.hideturtle()
    screen.exitonclick()