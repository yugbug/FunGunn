import turtle
import random
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Fun Gun By Guy")
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

# Create Door One and Door Two
bg_pen.lt(90)
bg_pen.hideturtle()
bg_pen.penup()
bg_pen.goto(-350, -90)
bg_pen.color("red")
bg_pen.pendown()
bg_pen.fd(180)
bg_pen.penup()
bg_pen.goto(350, -90)
bg_pen.pendown()
bg_pen.fd(180)
bg_pen.penup()
# Bullets Shot Pen
bullets_shot = 0
bs_pen = turtle.Turtle()
bs_pen.speed(0)
bs_pen.color("white")
bs_pen.penup()
bs_pen.setposition(-350, 250)
bs_pen.hideturtle()
bs_string = "Bullets Shot: %s" % bullets_shot
bs_pen.write(bs_string, False, align="left",  font=("Courier", 20, "bold"))
# Title Pen
title = "FunGun"
t_pen = turtle.Turtle()
t_pen.speed(0)
t_pen.color("red")
t_pen.penup()
t_pen.setposition(-55, 250)
t_pen.hideturtle()
t_string = "%s" % title
t_pen.write(t_string, False, align="left", font=("Courier", 30, "bold"))
# Score Pen
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(225, 250)
score_string = "Score: %s " % score
score_pen.write(score_string, False, align="left", font=("Courier", 20, "bold"))
score_pen.hideturtle()
# Lives Pen
lives = 3
lives_pen = turtle.Turtle()
lives_pen.speed(0)
lives_pen.color("white")
lives_pen.penup()
lives_pen.setposition(105, 250)
lives_string = "Lives: %s" % lives
lives_pen.write(lives_string, False, align="left", font=("Courier", 20, "bold"))
lives_pen.hideturtle()
# Smiley Pen
smile = ":)))"
smile_pen = turtle.Turtle()
smile_pen.speed(0)
smile_pen.color("white")
smile_pen.penup()
smile_pen.setposition(-140, 250)
lives_string = "%s" % smile
smile_pen.write(lives_string, False, align="left", font=("Courier", 20, "bold"))
smile_pen.hideturtle()
# Create One part to Gun through rectangle
gun_pen = turtle.Turtle()
gun_pen.color("red")
gun_pen.shape("square")
gun_pen.shapesize(0.25, 1.75)
gun_pen.penup()
gun_pen.setposition(150,10)
# Create other part to gun
other_gun_pen = turtle.Turtle()
other_gun_pen.color("red")
other_gun_pen.shape("square")
other_gun_pen.shapesize(0.25, 1)
other_gun_pen.penup()
other_gun_pen.setposition(158, 5)
# Create Final part to gun
final_gun_pen = turtle.Turtle()
final_gun_pen.color("red")
final_gun_pen.shape("square")
final_gun_pen.penup()
final_gun_pen.shapesize(0.3, 0.6)
final_gun_pen.setposition(162,-2.4)  # All Gun parts are created.
# Create Bullet
fire = "ready"
bullet = turtle.Turtle()
bullet.penup()
bullet.color("red")
bullet.shape("circle")
bullet.shapesize(0.3, 0.3)
bullet.speed(0)
bullet.hideturtle()
BULLET_SPEED = 20
GUN_SPEED = 10
turn = "left"
# Triangle enemies

number_of_enemies = 5
enemy_speed = 0.8
enemies = []

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for tr_enemy in enemies:
    tr_enemy.penup()
    tr_enemy.color("green")
    tr_enemy.shape("triangle")
    tr_enemy.shapesize(1, 1)
    tr_enemy.speed(0)
    tr_enemy._rotate(90)
    tr_enemy.setx(-350)
    tr_enemy.sety(random.randint(-85, 85))
    x = tr_enemy.xcor()
    y = tr_enemy.ycor()


def fire_bullets():
    global fire
    global bullets_shot
    global percent
    if fire == "ready":
        fire = "fire"
        x = gun_pen.xcor()
        y = gun_pen.ycor()
        bullet.setposition(x,y)
        bullets_shot += 1
        bs_pen.clear()
        bs_string = "Bullets Shot: %s" % bullets_shot
        bs_pen.write(bs_string, False, align="left", font=("Courier", 20, "bold"))
        percent = score / bullets_shot


def turn_right():
    global turn
    if turn == "left":
        turn = "right"
        x = other_gun_pen.xcor()
        x -= 15
        other_gun_pen.setx(x)
        final_gun_pen.setx(x-4)


def turn_left():
    global turn
    if turn == "right":
        turn = "left"
        x = other_gun_pen.xcor()
        x += 15
        other_gun_pen.setx(x)
        final_gun_pen.setx(x+4)


def move_up():
    y = gun_pen.ycor()
    y += GUN_SPEED
    if y < 90:
        gun_pen.sety(y)
        other_gun_pen.sety(y-5)
        final_gun_pen.sety(y-12.4)
        bullet.sety(y)


def move_down():
    y = gun_pen.ycor()
    y -= GUN_SPEED
    if y > -90:
        gun_pen.sety(y)
        other_gun_pen.sety(y-5)
        final_gun_pen.sety(y-12.4)
        bullet.sety(y)


def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


wn.listen()
wn.onkey(fire_bullets, "space")
wn.onkey(turn_right, "Right")
wn.onkey(turn_left, "Left")
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")

# total_percent = (score / bullets_shot) / 5
# per_pen = turtle.Turtle()
# per_pen.speed(0)
# per_pen.color("white")
# per_pen.penup()
# per_pen.setposition(-140, 250)
# percentage_string = "Shooting Percentage: %s" % total_percent
# per_pen.write(percentage_string, False, align="left", font=("Courier", 20, "bold"))

while True:
    wn.update()
    for tr_enemy in enemies:
        x = tr_enemy.xcor()
        x += enemy_speed
        tr_enemy.setx(x)
        if is_collision(gun_pen, tr_enemy):
            # tr_enemy.hideturtle()
            # enemies.pop(enemies.index(tr_enemy))
            tr_enemy.setx(-350)
            tr_enemy.sety(random.randint(-85, 85))
            lives -= 1
            lives_pen.clear()
            lives_string = "Lives: %s" % lives
            lives_pen.write(lives_string, False, align="left", font=("Courier", 20, "bold"))
        if is_collision(other_gun_pen, tr_enemy):
            # tr_enemy.hideturtle()
            # enemies.pop(enemies.index(tr_enemy))
            tr_enemy.setx(-350)
            tr_enemy.sety(random.randint(-85, 85))
            lives -= 1
            lives_pen.clear()
            lives_string = "Lives: %s" % lives
            lives_pen.write(lives_string, False, align="left", font=("Courier", 20, "bold"))
        if is_collision(final_gun_pen, tr_enemy):
            # tr_enemy.hideturtle()
            # enemies.pop(enemies.index(tr_enemy))
            tr_enemy.setx(-350)
            tr_enemy.sety(random.randint(-85,85))
            lives -=1
            lives_pen.clear()
            lives_string = "Lives: %s" % lives
            lives_pen.write(lives_string, False, align="left", font=("Courier", 20, "bold"))
        if is_collision(bullet, tr_enemy):
            # tr_enemy.hideturtle()
            enemy_speed += 0.025
            bullet.hideturtle()
            bullet.setposition(gun_pen.xcor(), gun_pen.ycor())
            fire = "ready"
            # enemies.pop(enemies.index(tr_enemy))
            tr_enemy.setx(-350)
            tr_enemy.sety(random.randint(-85,85))
            score += 5
            score_pen.clear()
            score_string = "Score: %s " % score
            score_pen.write(score_string, False, align="left", font=("Courier", 20, "bold"))
            # percent = score / bullets_shot
        if tr_enemy.xcor() > 350:
            # tr_enemy.hideturtle()
            # enemies.pop(enemies.index(tr_enemy))
            lives -= 1
            lives_pen.clear()
            lives_string = "Lives: %s" % lives
            lives_pen.write(lives_string, False, align="left", font=("Courier", 20, "bold"))
            tr_enemy.setx(-350)
            tr_enemy.sety(random.randint(-85, 85))
    if lives <= 0:
        total_percent = percent / 5
        print("GAME OVER \nYour final score was " + str(score))
        print("Your percentage of shooting enemies with bullets was " + str(total_percent) + "0%")
        # d = shelve.open('score.txt') Todo: Figure out high score
        # d['score'] = score
        # score = d['score']
        # print(score)
        # d.close()
        exit(0)
    if fire == "fire" and turn == "left":
        if bullet.xcor() <= 200:
            bullet.showturtle()
            x = bullet.xcor()
            x -= BULLET_SPEED
            bullet.setx(x)
        else:
            x = bullet.xcor()
            x += BULLET_SPEED
            bullet.setx(x)
    if bullet.xcor() < -350:
        bullet.hideturtle()
        fire = "ready"
    if fire == "fire" and turn == "right":
        if bullet.xcor() >= 0:
            bullet.showturtle()
            x = bullet.xcor()
            x += BULLET_SPEED
            bullet.setx(x)
        else:
            x = bullet.xcor()
            x -= BULLET_SPEED
            bullet.setx(x)
    if bullet.xcor() > 350:
        bullet.hideturtle()
        fire = "ready"
