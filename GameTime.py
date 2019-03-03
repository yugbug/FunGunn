import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Game")
wn.setup(800, 600)
wn.tracer(0)

bg_pen = turtle.Turtle()
bg_pen.penup()
bg_pen.color("white")
bg_pen.goto(-350,-250)
bg_pen.pendown()

for side in range(2):
    bg_pen.fd(700)
    bg_pen.lt(90)
    for side in range(1):
        bg_pen.fd(500)
        bg_pen.lt(90)


bg_pen.penup()
bg_pen.goto(0,-250)
bg_pen.pendown()
bg_pen.lt(90)

for side in range(38):
    bg_pen.fd(10)
    bg_pen.penup()
    bg_pen.fd(3.25)
    bg_pen.pendown()
bg_pen.hideturtle()
bg_pen.penup()
bg_pen.goto(-350, -60)
bg_pen.color("red")
bg_pen.pendown()
bg_pen.fd(120)
bg_pen.penup()
bg_pen.goto(350, -60)
bg_pen.pendown()
bg_pen.fd(120)

while True:
    wn.update()