import turtle

player_one = input("Player 1 uses the w and s keys. Their paddle is on the left. What is the name of this player?")
player_two = input("Player 2 uses the up and down keys. Their paddle is on the right. What is the name of this player?")
difficulty = input("Easy, Medium or Hard? 1 for easy, 2 for medium and 3 for hard")

WIDTH = 800
HEIGHT = 600

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Pong")
wn.setup(WIDTH, HEIGHT)
wn.tracer(0)

score_one = 0  # Score for Paddle One
score_two = 0  # Score for Paddle Two
title = "PONG"
# Paddle One Score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-190, 250)
score_string = "%s" % score_one
score_pen.write(score_string, False, align="left", font=("Arial", 30, "bold"))
score_pen.hideturtle()
# Paddle Two Score
score_pen_two = turtle.Turtle()
score_pen_two.speed(0)
score_pen_two.color("white")
score_pen_two.penup()
score_pen_two.setposition(190, 250)
score_string = "%s" % score_two
score_pen_two.write(score_string, False, align="left", font=("Arial", 30, "bold"))
score_pen_two.hideturtle()
# Title Pong
title_pen = turtle.Turtle()
title_pen.speed(0)
title_pen.color("white")
title_pen.penup()
title_pen.setposition(-43, 250)
score_string = "%s" % title
title_pen.write(score_string, False, align="left", font=("Arial", 30, "bold"))
title_pen.hideturtle()
# Insert Name of Player_1
name_pen = turtle.Turtle()
name_pen.speed(0)
name_pen.color("white")
name_pen.penup()
name_pen.setposition(-275, 280)
score_string = "Player One: %s" % player_one
name_pen.write(score_string, False, align="left", font=("Arial", 18, "bold"))
name_pen.hideturtle()
# Insert Name of Player_2
name_pen = turtle.Turtle()
name_pen.speed(0)
name_pen.color("white")
name_pen.penup()
name_pen.setposition(120, 280)
score_string = "Player Two: %s" % player_two
name_pen.write(score_string, False, align="left", font=("Arial", 18, "bold"))
name_pen.hideturtle()
# Border Pen
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-375, -250)
border_pen.pendown()
border_pen.pensize(3)

for side in range(2):
    border_pen.fd(750)
    border_pen.lt(90)
    for s in range(1):
        border_pen.fd(500)
        border_pen.lt(90)
border_pen.hideturtle()
border_pen.penup()
border_pen.setposition(0, -235)
border_pen.lt(90)

for i in range(19):
    border_pen.pendown()
    border_pen.fd(17)
    border_pen.penup()
    border_pen.fd(8)
    # 20 * 25 = height of border lines --> 500

# Paddle One description
paddle_one = turtle.Turtle()
paddle_one.speed(0)
paddle_one.shape("square")
paddle_one.color("white")
paddle_one.penup()
paddle_one.shapesize(5,1)
paddle_one.setposition(-350, 0)

PADDLE_SPEED = 20

# Paddle Two description
paddle_two = turtle.Turtle()
paddle_two.speed(0)
paddle_two.shape("square")
paddle_two.color("white")
paddle_two.penup()
paddle_two.shapesize(5,1)
paddle_two.setposition(350, 0)

# Pong Ball description
pong_ball = turtle.Turtle()
pong_ball.speed(0)
pong_ball.shape("circle")
pong_ball.color("white")
pong_ball.penup()
pong_ball.shapesize(0.4, 0.4)
pong_ball.goto(0,0)
if difficulty == '1':
    pong_ball.dx = 2
    pong_ball.dy = 2
if difficulty == '2':
    pong_ball.dx = 3
    pong_ball.dy = 3
if difficulty == '3':
    pong_ball.dx = 3.5
    pong_ball.dy = 3.5


def move_up():
    if paddle_one.ycor() < 200:
        y = paddle_one.ycor()
        y += PADDLE_SPEED
        paddle_one.sety(y)


def move_down():
    if paddle_one.ycor() > -200:
        y = paddle_one.ycor()
        y -= PADDLE_SPEED
        paddle_one.sety(y)


def move_up_two():
    if paddle_two.ycor() < 200:
        y = paddle_two.ycor()
        y += PADDLE_SPEED
        paddle_two.sety(y)


def move_down_two():
    if paddle_two.ycor() > -200:
        y = paddle_two.ycor()
        y -= PADDLE_SPEED
        paddle_two.sety(y)


def paddle_ball_collision(t1):
    if (pong_ball.xcor() > 340 and pong_ball.xcor() < 350) and (pong_ball.ycor() < t1.ycor() + 40 and pong_ball.ycor() > t1.ycor() - 40):
        return True
    else:
        return False


def paddle_ball(t1):
    if (pong_ball.xcor() < -340 and pong_ball.xcor() > -350) and (pong_ball.ycor() < t1.ycor() + 40 and pong_ball.ycor() > t1.ycor() - 40):
        return True
    else:
        return False


def exiting():
    exit(0)


wn.listen()
wn.onkey(move_up, "w")
wn.onkey(move_down, "s")
wn.onkey(move_up_two, "Up")
wn.onkey(move_down_two, "Down")
wn.onkey(exiting, "Escape")


# Main loop
while True:
    wn.update()

    pong_ball.setx(pong_ball.xcor() + pong_ball.dx)
    pong_ball.sety(pong_ball.ycor() + pong_ball.dy)
    if pong_ball.ycor() > 245:
        pong_ball.sety(245)
        pong_ball.dy *= -1
    if pong_ball.ycor() < -245:
        pong_ball.sety(-245)
        pong_ball.dy *= -1
    if pong_ball.xcor() > 370:
        pong_ball.goto(0, 0)
        pong_ball.dx *= -1
        score_one += 1
        score_pen.clear()
        score_string = "%s" % score_one
        score_pen.write(score_string, False, align="left", font=("Arial", 30, "bold"))
    if pong_ball.xcor() < -370:
        pong_ball.goto(0, 0)
        pong_ball.dx *= -1
        score_two += 1
        score_pen_two.clear()
        score_string = "%s" % score_two
        score_pen_two.write(score_string, False, align="left", font=("Arial", 30, "bold"))
    if paddle_ball_collision(paddle_two):
        pong_ball.setx(340)
        pong_ball.dx *= -1
    if paddle_ball(paddle_one):
        pong_ball.setx(-340)
        pong_ball.dx *= -1
