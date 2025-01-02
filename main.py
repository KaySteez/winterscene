import turtle


screen=turtle.Screen()

t = turtle.Turtle()
t.speed(5)
t.penup()


t.goto(0, 250)
t.pendown()

t.write("HO HO HO MERRY CHRISTMAS!  Starburst THEME!", align="center", font=("lemon milk", 18, "bold"))

t.hideturtle()

screen.screensize(900.900)
screen.bgcolor('hotpink')
t_ground=turtle.Turtle()
t_ground.speed(5.0)
t_ground.pencolor("yellow")
t_ground.fillcolor("yellow")

t_ground.penup()
t_ground.goto(-1000,-100)

t_ground.penup()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)
t_ground.end_fill()

import turtle

screen = turtle.Screen()
screen.bgcolor("hotpink")
t=turtle.Turtle()
t.speed(5.0)

t.penup()
t.goto(-20, -100)
t.pendown()
t.begin_fill()
t.fillcolor("magenta")
t.forward(40)
t.left(90)
t.forward(100)
t.left(90)
t.left(90)
t.forward(100)
t.end_fill()
t.penup()
t.goto(-100, -100)
t.pendown()
t.begin_fill()
t.fillcolor("magenta")
t.setheading(60)
t.forward(200)
t.right(120)
t.forward(200)
t.right(120)
t.forward(200)
t.end_fill()
t.penup()
t.goto(-80, 0)
t.pendown()
t.begin_fill()
t.fillcolor("magenta")
t.setheading(60)
t.forward(160)
t.right(120)
t.forward(160)
t.right(120)
t.forward(160)
t.end_fill()
t.penup()
t.goto(-60, 100)
t.pendown()
t.begin_fill()
t.fillcolor("magenta")
t.setheading(60)
t.forward(120)
t.right(120)
t.forward(120)
t.right(120)
t.forward(120)
t.end_fill()
t.penup()
t.goto(-7, 160)
t.pendown()
t.begin_fill()
t.fillcolor("yellow")
t.setheading(72)
t.forward(30)
t.right(144)
t.forward(30)
t.right(144)
t.forward(30)
t.right(144)
t.forward(30)
t.right(144)
t.forward(30)
t.end_fill()
t.hideturtle()

import turtle

screen = turtle.Screen()
screen.bgcolor("hotpink")
t = turtle.Turtle()
t.speed(5)

t.color("red")





