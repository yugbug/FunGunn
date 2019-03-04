import turtle
import time
import math
import random

start_time = time.time()

back = turtle.Screen()
back.bgcolor("black")
back.title("Space Invaders")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-310, -290)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
    # time.sleep(1)
border_pen.hideturtle()

score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 310)
score_string = "Score: %s" % score
score_pen.write(score_string, False, align="left", font=("Courier", 14, "bold"))
score_pen.hideturtle()

level = 1

level_pen = turtle.Turtle()
level_pen.speed(0)
level_pen.color("white")
level_pen.penup()
level_pen.setposition(-200, 310)
level_string = "Level: %s" % level
level_pen.write(level_string, False, align="left", font=("Courier", 14, "bold"))
level_pen.hideturtle()

player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setheading(90)
player.setposition(0, -250)

PLAYER_SPEED = 15

number_of_invaders = 5
invaders = []

for i in range(number_of_invaders):
    invaders.append(turtle.Turtle())

for invader in invaders:
    invader.color("green")
    invader.shape("circle")
    invader.penup()
    invader.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    invader.setposition(x,y)
    # if y % 10 != 0:
    #     for i in invaders:
    #         y = random.randint(100, 250)
    #         if y % 10 == 0:
    #             invader.setposition(x, y)

invader_speed = 2
invader_down = 40

bullet = turtle.Turtle()
bullet.color("red")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.shapesize(0.3, 0.3)
bullet.hideturtle()

bullet_speed = 35

bullet_state = "ready"

shuttle = turtle.Turtle()
shuttle.color("purple")
shuttle.shape("circle")
shuttle.penup()
shuttle.speed(0)
shuttle.shapesize(1.5, 4)
shuttle.setposition(-320, 290)
shuttle.hideturtle()

SHUTTLE_SPEED = 5


def exiting():
    exit(0)


def move_left():
    x = player.xcor()
    x -= PLAYER_SPEED
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += PLAYER_SPEED
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


def proper_y(n):
    if n % 10 == 0:
        return True
    else:
        return False


back.listen()
back.onkey(exiting, "Escape")
back.onkey(move_left, "Left")
back.onkey(move_right, "Right")
back.onkey(fire_bullet, "space")

#  Main loop of game
while True:
    for invader in invaders:
        elapsed_time = time.time() - start_time
        x = invader.xcor()
        x += invader_speed
        invader.setx(x)

        if invader.xcor() > 280:
            for e in invaders:
                y = e.ycor()
                y -= invader_down
                e.sety(y)
            invader_speed *= -1

        if invader.xcor() < -280:
            for e in invaders:
                y = e.ycor()
                y -= invader_down
                e.sety(y)
            invader_speed *= -1

        if is_collision(bullet, invader):
            bullet.hideturtle()
            bullet_state = "ready"
            invader.hideturtle()
            invaders.pop(invaders.index(invader))
            bullet.setposition(0, -400)
            # #  Need to fix coordinates
            # x = random.randint(-200, 200)
            # # y = random.randint(100, 250)
            # invader.setposition(x, y)
            score += 10
            score_string = "Score: %s" % score
            score_pen.clear()
            score_pen.write(score_string, False, align="left", font=("Courier", 14, "bold"))

        if is_collision(player, invader):
            player.hideturtle()
            invader.hideturtle()
            print("GAME OVER")
            back.title("GAME OVER")
            break

        if time.time() == 0:  # Todo: something with time here
            if shuttle.xcor() < 380:
                x = shuttle.xcor()
                y = shuttle.ycor()
                shuttle.showturtle()
                x += SHUTTLE_SPEED
                shuttle.setposition(x, y)
            if is_collision(shuttle, bullet):
                bullet.hideturtle()
                bullet.setposition(player.xcor(), player.ycor() + 10)
                shuttle.hideturtle()
                shuttle.setposition(-320, 290)
                score += 300
                score_string = "Score: %s" % score
                score_pen.clear()
                score_pen.write(score_string, False, align="left", font=("Courier", 14, "bold"))
            if shuttle.xcor() >= 380:
                shuttle.setposition(-320, 290)

        if invaders == []:
            level += 1
            level_string = "Level: %s" % level
            level_pen.clear()
            level_pen.write(level_string, False, align="left", font=("Courier", 14, "bold"))

    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    if bullet.ycor() > 295:
        bullet.hideturtle()
        bullet_state = "ready"

    if back.title == "GAME OVER":
        print("Your score was " + str(score) + ". Nice job! You reached level " + str(level) + ".")
