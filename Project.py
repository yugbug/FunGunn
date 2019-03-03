import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(800, 600)
wn.title("Number Here")
wn.tracer(0)

number_of_victims = 178600
vc = []
victims = "JEW"
pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.setposition(-393, 300)
pen.speed(0)
pen_string = "%s" % victims
# pen.write(pen_string, False, align="left", font=("Courier", 10, "none"))
pen.hideturtle()
victims_count = 0
way = "right"
x_c = -393
y_c = 300
# pen = turtle.Turtle()
# pen.color("white")
# pen.penup()
# pen.setposition(-370, 280)
# pen.speed(0)
# pen_string = "%s" % victims
# pen.write(pen_string, False, align="left", font=("Courier", 10, "none"))
# pen.hideturtle()
# Main loop
while True:
    wn.update()
    for i in range(number_of_victims):
        vc.append(pen)
        if way == "right":
            if y_c <= -300:
                pen.clear()
                x_c = -393
                y_c = 300
                pen.setposition(x_c, y_c)
            if y_c > -300:
                y_c -= 10
                pen.sety(y_c)
                pen.setx(x_c)
                print(victims_count)
                pen.write(pen_string, False, align="left", font=("Courier", 10))

                for pen in vc:
                    # if y_c <= -300:
                    #     pen.clear()
                    #     x_c = -393
                    #     y_c = 300
                    #     pen.setposition(x_c, y_c)
                    for z in range(0, 335):
                        if x_c < 350:
                            x_c += 27
                            pen.sety(y_c)
                            pen.setx(x_c)
                            print(victims_count)
                            pen.write(pen_string, False, align="left", font=("Courier", 10))
                            way = "left"
                            victims_count += 1
                            wn.title("Jews Remembered So Far: " + str(victims_count))
        if way == "left":
            if y_c <= -300:
                pen.clear()
                x_c = -393
                y_c = 300
                pen.setposition(x_c, y_c)
            if y_c > -300:
                y_c -= 10
                pen.sety(y_c)
                pen.setx(x_c)
                print(victims_count)
                pen.write(pen_string, False, align="left", font=("Courier", 10))
                for pen in vc:
                    # if y_c <= -300:
                    #     pen.clear()
                    #     x_c = -393
                    #     y_c = 300
                    #     pen.setposition(x_c, y_c)
                    for z in range(0, 30):
                        if x_c > -380:
                            x_c -= 27
                            pen.sety(y_c)
                            pen.setx(x_c)
                            print(victims_count)
                            pen.write(pen_string, False, align="left", font=("Courier", 10))
                            way = "right"
                            victims_count += 1
                            wn.title("Jews Remembered So Far: " + str(victims_count))


# 1680 Jews per page are remembered
# 3572 pages are required in order to remember all the Jews which died in the Holocaust
# Each page takes 28.56 seconds to fill 1680 Jews in.
# You would have to wait 28 hours and 20 minutes to complete the 3572 pages
