"""Turtle Project (Harry Potter Horcrux in simple frame)."""


__author__ = "730684472"

from turtle import Turtle, colormode, done, tracer, update


def square(square: Turtle, x: float, y: float, width: int, r: int, g: int, b: int, forward_pen: int, speed: int, i: int) -> None:
    """Creates a filled square. Parameters(turtle,x-start,y-start,width-pensize,r-red,g-green,b-blue, forward_pen-length, speed-draw speed, i-counter)."""
    square.penup()  # lines 9-13 move pen, aim direction, and insert speed from function call
    square.goto(x, y)
    square.setheading(0.0)
    square.pendown()
    square.speed(speed)

    colormode(255)  # set line color 
    if (r == 105 and g == 105 and b == 105):  # if r = 105, g =105, and b = 105 the color is gray so I want a black border from function call
        square.pencolor(r - 105, g - 105, b - 105)  # set outline color to black from function call
        square.width(width)  # set a seeable width from function call

    square.fillcolor(r, g, b)  # lines 20-21 set and fill color from function call
    square.begin_fill()
        
    while (i < 4):  # i starts at 0 and we need 4 lines
        square.forward(forward_pen)  # pen goes forward from function call
        square.right(90)  # line turns 90 degrees
        i = i + 1
    square.end_fill()  # stop filling
    square.hideturtle()  # hide turtle


def triangle(triangle: Turtle, x: float, y: float, width: int, r: int, g: int, b: int, forward_pen: int, speed: int, i: int) -> None:
    """Creates a white hollow triangle.Parameters(turtle,x-start,y-start,width-pensize,r-red,g-green,b-blue, forward_pen-length, speed-draw speed, i-counter)."""
    triangle.penup()  # lines 34-38 move pen, aim direction, and insert draw speed from function call
    triangle.goto(x, y)
    triangle.setheading(180)
    triangle.pendown()
    triangle.speed(speed)

    colormode(255)  # lines 40-42 set color and line width from function call
    triangle.pencolor(r, g, b)
    triangle.width(width)
 
    while (i < 3):  # i starts at 0 and a triangle has 3 sides, once i = 3 the loop will stop
        triangle.forward(forward_pen)  # pen moves forward from function call
        triangle.right(120)  # pen rotates 120 degrees
        i = i + 1  
    triangle.hideturtle()  # hides turtle


def line(line: Turtle, x: float, y: float, width: int, r: int, g: int, b: int, forward_pen: int, speed: int, i: int) -> None:
    """Create a line. Parameters(turtle,x-start,y-start,width-pensize,r-red,g-green,b-blue, forward_pen-length, speed-draw speed, i-counter)."""
    line.penup()  # lines 53-57 move pen, aim direction, and insert speed from function call
    line.goto(x, y)
    line.setheading(270)
    line.pendown()
    line.speed(speed)

    colormode(255)  # lines 59-61 set color and line width from function call
    line.pencolor(r, g, b)
    line.width(width)

    line.forward(forward_pen)  # pen moves forward from function call
    line.hideturtle()  # hide turtle


def circle(circle: Turtle, x: float, y: float, width: int, r: int, g: int, b: int, radius: int, speed: int, i: int) -> None:
    """Creates a hollow cricle. Parameters(turtle,x-start,y-start,width-pensize,r-red,g-green,b-blue, radius = radius of circle, speed-draw speed, i-counter)."""
    circle.penup()  # lines 68-72 move pen, aim direction, and set speed from function call
    circle.goto(x, y)
    circle.setheading(0.0)
    circle.pendown()
    circle.speed(speed)

    colormode(255)  # lines 74-76 set line color and width from function call
    circle.pencolor(r, g, b)
    circle.width(width)

    circle.circle(radius)  # uses circle function and the radius parameter from function call to draw a circle 


def main() -> None:
    """The entry point of my scene."""
    tracer(0, 0)
    spiral: Turtle = Turtle()
    square(spiral, -200, 200, 5, 105, 105, 105, 400, 25, 0)  # gray outter square
    square(spiral, -150, 150, 1, 0, 0, 0, 300, 25, 0)  # black inner square
    triangle(spiral, 125, -125, 10, 255, 255, 255, 250, 25, 0)  # white triangle
    line(spiral, 0, 85, 10, 255, 255, 255, 200, 25, 0)  # white line
    circle(spiral, 0, -120, 10, 255, 255, 255, 70, 25, 0)  # white circle
    update()
    done()


if (__name__ == "__main__"):
    main()