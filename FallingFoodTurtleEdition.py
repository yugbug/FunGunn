import random
import turtle
from tkinter import PhotoImage

# Setting the background
WIDTH = 700
HEIGHT = 1000
wn = turtle.Screen()
wn.setup(WIDTH, HEIGHT)
wn.bgcolor("sky blue")
wn.title("Food Fall")
wn.tracer(0)

top_left = (int(- (WIDTH // 2)), int((HEIGHT // 2)))

# Describing the orders
order_sent = False  # If computer makes the order
order_num = 1  # Number of orders completed
order_complete = False  # Todo: Every time one order is complete, order_num += 1
title = "FOOD FALL"
writing_pen = turtle.Turtle()
writing_pen.speed(0)
writing_pen.color("white")
writing_pen.hideturtle()
writing_pen.penup()
writing_pen.setposition(-340, 350)
write_string_one = "%s" % title
writing_pen.write(write_string_one, False, align="left", font=("Courier", 26, "italic"))

by = "BY GUY NIR"
writing_pen.setposition(-340, 320)
write_string_two = "%s" % by
writing_pen.write(write_string_two, False, align="left", font=("Courier", 26, "italic"))

order = "Order #" + str(order_num) + ":"
writing_pen.setposition(-330, 250)
order_string = "%s" % order
writing_pen.write(order_string, False, align="left", font=("Courier", 26, "underline"))

chef_img = r"/Users/gnir/PycharmProjects/games/Images/chef.gif"
pancakes_img = r"/Users/gnir/PycharmProjects/games/Images/pancakes.gif"
# larger = PhotoImage(file=pancakes_img).subsample(2, 2)

# Creating the chef
wn.addshape(chef_img)
chef = turtle.Turtle()
chef.shape(chef_img)
chef.resizemode("auto")
chef.penup()
chef.setposition(100, -325)
chef_speed = 20


def enlarge(img_path, x, y):
    change_size(True, img_path, x, y)


def shrink(img_path, x, y):
    change_size(False, img_path, x, y)


def change_size(enlarge_picture, img_path, x, y):
    if enlarge_picture:
        larger = PhotoImage(file=img_path).subsample(x, y)
    else:
        larger = PhotoImage(file=img_path).subsample(x, y)
    wn.addshape("larger", turtle.Shape("image", larger))
    food_name = turtle.Turtle("larger")
    food_name.stamp()


def move_right():
    x = chef.xcor()
    x += chef_speed
    if x < 290:
        chef.setx(x)


def move_left():
    x = chef.xcor()
    x -= chef_speed
    if x > -100:
        chef.setx(x)


wn.onkey(move_right, "Right")
wn.onkey(move_left, "Left")
wn.listen()
shrink(pancakes_img, 2, 2)

# Draw the blue line
separation_pen = turtle.Turtle()
separation_pen.speed(0)
separation_pen.color("blue")
separation_pen.penup()
separation_pen.hideturtle()
separation_pen.pensize(5)
separation_pen.setposition(-150, -390)

separation_pen.pendown()
separation_pen.lt(90)
separation_pen.fd(HEIGHT)

while True:
    wn.update()
    if not order_sent:
        food_list = ["bacon", "eggs", "toast", "pancakes", "waffles", "coffee", "muffin", "doughnut", "croissant",
                     "sandwich"]
        times_list = ["1", "2", "3"]

        random_choice1 = random.choice(food_list)
        random_choice2 = random_choice1
        while random_choice1 == random_choice2:
            random_choice2 = random.choice(food_list)

        random_food = "X" + str(random.choice(times_list)) + " " + str(random_choice1)
        random_food_2 = "X" + str(random.choice(times_list)) + " " + str(random_choice2)
        order_pen2 = turtle.Turtle()
        order_pen2.speed(0)
        order_pen2.color("white")
        order_pen2.penup()
        order_pen2.setposition(-345, 220)
        food_string = "%s" % random_food
        order_pen2.write(food_string, False, align="left", font=("Courier", 26))
        order_pen2.hideturtle()
        food_string_2 = "%s" % random_food_2
        writing_pen.speed(0)
        writing_pen.setposition(-345, 200)
        writing_pen.write(food_string_2, False, align="left", font=("Courier", 26))
        order_sent = True
