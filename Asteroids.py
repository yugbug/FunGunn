import turtle

wn = turtle.Screen()
wn.title("ASTEROIDS")
wn.setup(800,600)
wn.bgcolor("black")
wn.tracer(0)

ship_pen = turtle.Turtle()
ship_pen.penup()
ship_pen.speed(0)
ship_pen.shapesize(1.2, 1.75)
ship_pen.setposition(0, 0)
ship_pen.color("white", "black")
ship_pen.begin_fill()
ship_pen.turtlesize(1.2, 1.75)
ship_pen.end_fill()
SHIP_SPEED = 10


def move_left():
    x = ship_pen.xcor()
    if x > -375:
        x -= SHIP_SPEED
        ship_pen.setx(x)


def move_right():
    x = ship_pen.xcor()
    if x < 375:
        x += SHIP_SPEED
        ship_pen.setx(x)



def move_up():
    y = ship_pen.ycor()
    if y < 275:
        y += SHIP_SPEED
        ship_pen.sety(y)

wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")

while True:
    wn.update()
