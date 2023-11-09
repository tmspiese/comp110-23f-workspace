"""Turtle Tutorial."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
bob:Turtle = Turtle()

leo.speed(5)

leo.penup()
leo.goto(-175,0)
leo.pendown()

colormode(255)
leo.pencolor(48,25,52)

leo.fillcolor(0,0,0)
leo.begin_fill()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

leo.end_fill()
leo.hideturtle()

bob.speed(20)

bob.penup()
bob.goto(-175,0)
bob.pendown()

bob.pencolor(255,0,0)
side_length: int = 300

i = 0
while(i < 150):

    bob.forward(side_length)
    bob.left(122)
    i = i + 1
    side_length = side_length * 0.97

bob.hideturtle()


done()