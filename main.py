import turtle
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
#colors = ["green", "black", "cyan", "magenta", "orange", "pink", "brown", "dark blue", "blue"]


# for i in range(36):
#     tim.speed(99)
#     tim.circle(90)
#     tim.left(10)
#     tim.color(random.choice(colors))
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

tim.pensize(2)
tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
draw_spirograph(5)
turtle.exitonclick()

