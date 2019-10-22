import random
import time
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

game_over = False
freeze = False
pancake_counter = 0

space_was_clicked_time = 0
space_was_clicked = False


PANCAKE_X_LENGTH = 110  # after considering the shrink
CHEF_PIC_X_LENGTH = 140

top_left = (int(- (WIDTH // 2)), int((HEIGHT // 2)))

# Describing the orders
order_num = 1  # Number of orders completed
order_complete = False  # Todo: Every time one order is complete, order_num += 1


def writing_turtle(color, x, y, title, font_size, style):
    writing_pen = turtle.Turtle()
    writing_pen.speed(0)
    writing_pen.color(color)
    writing_pen.hideturtle()
    writing_pen.penup()
    writing_pen.setposition(x, y)
    write_string_one = "%s" % title
    writing_pen.write(write_string_one, False, align="left", font=("Courier", font_size, style))
    return writing_pen


writing_pen = writing_turtle("white", -340, 350, "FOOD FALL", 26, "italic")

by_string = "BY GUY NIR"
by = writing_turtle("white", -340, 320, by_string, 26, "italic")

food_speed = 5
food_on_plate = False

chef_img = r"/Users/gnir/PycharmProjects/games/Images/chef.gif"
pancakes_img = r"/Users/gnir/PycharmProjects/games/Images/pancakes.gif"

# Creating the chef
wn.addshape(chef_img)
chef = turtle.Turtle()
chef.shape(chef_img)
chef.resizemode("auto")
chef.penup()
chef.setposition(100, -325)
chef_speed = 20

number_of_pancakes = 10


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


class Order:
    def __init__(self, amount_of_pancakes, order_number):
        self.amount_of_pancakes = amount_of_pancakes
        self.order_number = order_number
        self.creation_time = time.time()
        self.constant_y_change = 100  # how much the orders are spaced out by
        self.order_complete = True
        self.turtle = None
        self.customer_rating = 5  # rating out of 5, 2 main factors: amount of time, amount of pancakes,
        # add later: different feelings for each customer

        wn.ontimer(self.decrease_rating, 5000)

    def decrease_rating(self):
        self.customer_rating -= 1


class Game:
    def __init__(self):
        self.freeze = False
        self.game_over = False
        self.pancake_list = []
        self.standard_rating = 1  # this means the standard rating that the player needs to get to. 1-5
        self.chef_destination = 100
        #  Todo: orders,

    def unfreeze(self):
        game.freeze = False
        diff = (self.chef_destination) - chef.xcor()
        for pancake in game.pancake_list:
            turtle = pancake.turtle
            if pancake.on_plate:
                turtle.setx(turtle.xcor() + diff)
        chef.setx(self.chef_destination)

    def freeze_game(self):
        game.freeze = True
        wn.ontimer(self.unfreeze, 4000)

    # def freeze(self):
    #     game.pancake_list


orders = []
num_of_orders = len(orders)  # 5

orderA = Order(amount_of_pancakes=2, order_number=1)
game = Game()


def print_orders(some_order, order_num):
    y_cor = 220 - (order_num * some_order.constant_y_change)
    order = "Order #" + str(some_order.order_number) + ":"
    writing_pen.setposition(-330, y_cor + 30)  # 250 + var*6
    order_string = "%s" % order
    writing_pen.write(order_string, False, align="left", font=("Courier", 26, "underline"))
    random_food = "X" + str(some_order.amount_of_pancakes) + " pancakes"
    some_order.turtle = turtle.Turtle()
    some_order.turtle.speed(0)
    some_order.turtle.color("white")
    some_order.turtle.penup()

    some_order.turtle.setposition(-345, y_cor)
    food_string = "%s" % random_food
    some_order.turtle.write(food_string, False, align="left", font=("Courier", 26))
    # some_order.turtle.hideturtle()
    # if oder complete then remove order


for i in range(3):
    order = Order(random.randint(1, 7), i + 1)
    orders.append(order)
    print_orders(order, i)


# Remove
#
# for i in range(3):
#     some_order = orders[i]
#     some_order.turtle.hideturtle()

# time delay



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
    for pancake in game.pancake_list:
        turtle = pancake.turtle
        turtle.penup()
        pancake_x = turtle.xcor()
        # turtle.hideturtle()
        if x < 290 and not pancake.on_plate and not game.freeze:
            chef.setx(x)
        if x < 290 and pancake.on_plate and not game.freeze:
            chef.setx(x)
            pancake_x += chef_speed
            turtle.setx(pancake_x)

def move_left():
    x = chef.xcor()
    x -= chef_speed
    for pancake in game.pancake_list:
        turtle = pancake.turtle
        # turtle.hideturtle()
        turtle.penup()
        pancake_x = turtle.xcor()
        if x > -100 and not pancake.on_plate and not game.freeze:
            chef.setx(x)
        if x > -100 and pancake.on_plate and not game.freeze:
            chef.setx(x)
            pancake_x -= chef_speed
            turtle.setx(pancake_x)


def distribute_pancakes():
    print("Distributing pancakes")
    print(pancake_counter)
    if pancake_counter == 0:
        space_was_clicked = True
        empty_warning = "Error: CANNOT DISTRIBUTE 0 PANCAKES"
        t = writing_turtle("red", -100, 350, empty_warning, 20, "bold")
        space_was_clicked_time = time.time()
        wn.ontimer(t.clear, 2000)
    else:
        # game.freeze = True
        game.freeze_game()
        chef_destination = -255
        diff = chef.xcor() - (chef_destination)
        for pancake in game.pancake_list:
            turtle = pancake.turtle
            if pancake.on_plate:
                turtle.setx(turtle.xcor() - diff)
        chef.setx(chef_destination)
        # wn.ontimer(unfreeze, 4000)


def escape():
    game.game_over = True
    wn.bye()


def is_collision(turtle, turtle_chef):
    turtle_left_edge = turtle.xcor() - int(PANCAKE_X_LENGTH / 2)
    turtle_right_edge = turtle.xcor() + int(PANCAKE_X_LENGTH / 2)
    turtle_chef_right_edge = turtle_chef.xcor() + int(CHEF_PIC_X_LENGTH / 2)
    turtle_chef_left_edge = turtle_chef.xcor() - int(CHEF_PIC_X_LENGTH / 2)

    if turtle_left_edge < turtle_chef_right_edge:  # Pancake in the right
        if turtle_left_edge > turtle_chef_left_edge:  # make sure not extreme left
            if turtle.xcor() < turtle_chef_right_edge:  # make sure that most of the pancake goes into the chef
                return True

    if turtle_right_edge > turtle_chef_left_edge:
        if turtle_right_edge < turtle_chef_right_edge:
            if turtle.xcor() > turtle_chef_left_edge:
                return True


    return False


wn.onkey(escape, "Escape")
wn.onkey(move_right, "Right")
wn.onkey(move_left, "Left")
wn.onkey(distribute_pancakes, "1")
wn.onkey(distribute_pancakes, "2")
wn.onkey(distribute_pancakes, "3")

wn.listen()



def generate_pancakes(pancakes_number):
    for i in range(pancakes_number):
        # Creating one pancake
        pancake_turtle = shrink(pancakes_img, 2, 2)
        wn.register_shape(pancakes_img)
        pancake_turtle.penup()
        reset_initial_pancake_position(pancake_turtle)
        pancake_turtle.clearstamps()
        pancake_turtle.stamp()

        pancake_guy = Pancake(pancake_turtle, random.randint(0, 1000))
        game.pancake_list.append(pancake_guy)


def reset_initial_pancake_position(pancake_turtle):
    pancake_turtle.speed(0)
    pancake_turtle.sety(random.randint(420, 600))
    pancake_turtle.setx(random.randint(-120, 320))



generate_pancakes(number_of_pancakes)


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

pancake_index = len(game.pancake_list)


def drop_pancake_down(turtle_pancake):
    y = turtle_pancake.ycor()

    y -= food_speed
    turtle_pancake.clearstamps()
    turtle_pancake.sety(y)


above_chef_coordinate = -300  # Todo: capitalize both and refactor
bottom_of_screen_coordinate = -420

while not game_over:
    wn.update()

    for pancake in game.pancake_list:
        turtle_pancake = pancake.turtle
        if not game.freeze:
            if pancake.get_time_delay_counter() == 0:
                if turtle_pancake.ycor() > above_chef_coordinate:
                    drop_pancake_down(turtle_pancake)

                if turtle_pancake.ycor() in range(above_chef_coordinate, 5 + above_chef_coordinate):
                    if is_collision(turtle_pancake, chef):

                        if not pancake.on_plate:
                            pancake_counter += 1

                            pancake.on_plate = True

                    if not pancake.on_plate:
                        drop_pancake_down(turtle_pancake)

                if turtle_pancake.ycor() < above_chef_coordinate:
                    if not pancake.on_plate:
                        drop_pancake_down(turtle_pancake)

                if turtle_pancake.ycor() < bottom_of_screen_coordinate:
                    reset_initial_pancake_position(turtle_pancake)


            else:
                pancake.set_time_delay_counter((pancake.get_time_delay_counter() - 1))
    for order in orders:
        print("hello from order#" + str(order.order_number) + ": " + str(order.customer_rating))
