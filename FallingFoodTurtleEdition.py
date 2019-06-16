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

PANCAKE_X_LENGTH = 110  # after considering the shrink
CHEF_PIC_X_LENGTH = 140

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

food_speed = 5
food_on_plate = False
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

number_of_pancakes = 10
PANCAKES = []


class Pancake:

    def __init__(self, turtle, time_delay):
        self.turtle = turtle
        self.time_delay_counter = time_delay
        self.on_plate = False

    def get_time_delay_counter(self):
        return self.time_delay_counter

    def get_turtle(self):
        return turtle

    def set_time_delay_counter(self, new_int_value):
        self.time_delay_counter = new_int_value
        return self

    def print_guy_is_handsome(self):
        print("guy is handsome")


def enlarge(img_path, x, y):
    return change_size(True, img_path, x, y)


def shrink(img_path, x, y):
    return change_size(False, img_path, x, y)


def change_size(enlarge_picture, img_path, x, y):
    if enlarge_picture:
        larger = PhotoImage(file=img_path).subsample(x, y)
    else:
        larger = PhotoImage(file=img_path).subsample(x, y)
    wn.register_shape("larger", turtle.Shape("image", larger))
    food_name = turtle.Turtle("larger")
    food_name.stamp()
    return food_name


def move_right():
    x = chef.xcor()
    x += chef_speed
    for pancake in PANCAKES:
        turtle = pancake.turtle
        turtle.penup()
        pancake_x = turtle.xcor()
        # turtle.hideturtle()
        if x < 290 and not pancake.on_plate:
            chef.setx(x)
        if x < 290 and pancake.on_plate:
            chef.setx(x)
            pancake_x += chef_speed
            turtle.setx(pancake_x)

def move_left():
    x = chef.xcor()
    x -= chef_speed
    for pancake in PANCAKES:
        turtle = pancake.turtle
        # turtle.hideturtle()
        turtle.penup()
        pancake_x = turtle.xcor()
        if x > -100 and not pancake.on_plate:
            chef.setx(x)
        if x > -100 and pancake.on_plate:
            chef.setx(x)
            pancake_x -= chef_speed
            turtle.setx(pancake_x)


def place_cloche_lid():
    pass


def is_collision(turtle, turtle_chef):
    turtle_left_edge = turtle.xcor() - int(PANCAKE_X_LENGTH / 2)
    turtle_right_edge = turtle.xcor() + int(PANCAKE_X_LENGTH / 2)
    turtle_chef_right_edge = turtle_chef.xcor() + int(CHEF_PIC_X_LENGTH / 2)
    turtle_chef_left_edge = turtle_chef.xcor() - int(CHEF_PIC_X_LENGTH / 2)
    # print(turtle_left_edge, turtle_right_edge,  turtle_chef_left_edge, turtle_chef_right_edge)

    if turtle_left_edge < turtle_chef_right_edge:  # Pancake in the right
        if turtle_left_edge > turtle_chef_left_edge:  # make sure not extreme left
            if turtle.xcor() < turtle_chef_right_edge:  # make sure that most of the pancake goes into the chef
                return True

    if turtle_right_edge > turtle_chef_left_edge:
        if turtle_right_edge < turtle_chef_right_edge:
            if turtle.xcor() > turtle_chef_left_edge:
                return True

    # elif #pancake in the left

    # if int(turtle_left_edge/2) <= turtle_chef_right_edge and int(turtle_right_edge/2) >= turtle_chef_left_edge:
    #     return True
    return False

    # distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    # if distance < 50:
    #     return True
    # else:
    #     return False


wn.onkey(move_right, "Right")
wn.onkey(move_left, "Left")
wn.listen()


# random_y_position = random.choice(random.randint(400,600))
# if random_y_position == range

def generate_pancakes(pancakes_number):
    for i in range(pancakes_number):
        pancake_turtle = shrink(pancakes_img, 2, 2)
        wn.register_shape(pancakes_img)
        pancake_turtle.penup()
        pancake_turtle.speed(0)
        pancake_turtle.sety(random.randint(400, 600))
        pancake_turtle.setx(random.randint(-120, 320))
        pancake_turtle.clearstamps()
        pancake_turtle.stamp()

        pancake_guy = Pancake(pancake_turtle, random.randint(0, 1000))
        PANCAKES.append(pancake_guy)


# 1. Deep approach: understand excatly how to delete turtles
# 2. workaround: startwith <100 turtles and then if they  go  to the buttom, reset their coornidates.


generate_pancakes(number_of_pancakes)
# for pancakes in PANCAKES:
#     pancakes.penup()
#     pancakes.speed(0)
#     #  Pancakes.Stamp == stamps an image on to the screen on the poinvaders.pop(invaders.index(invader))int given
#     pancakes.setposition(80, 400)
#     pancakes.clearstamps()  # Deletes previous position of image / stamp
#     pancakes.stamp()

# pancakes = shrink(pancakes_img, 2, 2)
#
# wn.register_shape(pancakes_img)
#
# # pancakes = turtle.Turtle(shape=pancakes_img)
#
# pancakes.penup()
# pancakes.speed(0)
# #  Pancakes.Stamp == stamps an image on to the screen on the point given
# pancakes.setposition(80, 400)
# pancakes.clearstamps()  #  Deletes previous position of image / stamp
# pancakes.stamp()


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

pancake_index = len(PANCAKES)


def drop_pancake_down(turtle_pancake):
    y = turtle_pancake.ycor()
    if y > bottom_of_screen_coordinate:

        y -= food_speed
        turtle_pancake.clearstamps()
        turtle_pancake.sety(y)

    else:
        PANCAKES.pop(PANCAKES.index(pancake))
while True:
    wn.update()
    above_chef_coordinate = -300
    bottom_of_screen_coordinate = -375

    for pancake in PANCAKES:
        turtle_pancake = pancake.turtle

        if pancake.get_time_delay_counter() == 0:
            if turtle_pancake.ycor() > above_chef_coordinate:
                drop_pancake_down(turtle_pancake)

            if turtle_pancake.ycor() in range(above_chef_coordinate, 5 + above_chef_coordinate):
                if is_collision(turtle_pancake, chef):
                    # print("collision!!!!!!")

                    #  Create a delay until panckages go down #
                    # 1. find the current index of this pancake the list - i

                    # go with for loop on all the  elements in the list with  index greater  than i

                    pancake.on_plate = True
                    # food_on_plate = True
                if not pancake.on_plate:
                    drop_pancake_down(turtle_pancake)

            if turtle_pancake.ycor() < above_chef_coordinate:
                if not pancake.on_plate:
                    drop_pancake_down(turtle_pancake)

            if turtle_pancake.ycor() < bottom_of_screen_coordinate:
                y = turtle_pancake.ycor()
                # turtle_pancake.clearstamps()
                PANCAKES.remove(pancake)
                turtle_pancake.clear()
                del pancake.turtle
                del pancake

        else:
            pancake.set_time_delay_counter((pancake.get_time_delay_counter() - 1))

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
