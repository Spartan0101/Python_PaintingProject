import turtle as t
import random
from turtle import Turtle
from turtle import Screen

# Making a spirograph
tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)





# tib = t.Turtle()
# t.colormode(255)
# # Random colors and random directions
# # colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# # RBG color from Tuple
# # t.color(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
#
# directions = [0, 90, 180, 270]
# tib.pensize(15)
# tib.speed("fastest")
#
# for _ in range(200):
#     tib.color(random_color())
#     tib.forward(30)
#     tib.setheading(random.choice(directions))




# Draw a shapes
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tib.forward(100)
#         tib.right(angle)
#
# for shape_side_n in range(3, 11):
#     tib.color(random.choice(["red", "blue", "green", "yellow", "purple", "orange"]))
#     draw_shape(shape_side_n)



# tibi_the_turtle = Turtle()
# tibi_the_turtle.shape("turtle")
# tibi_the_turtle.color("green")



# for _ in range(10):
#     tibi_the_turtle.forward(10)
#     tibi_the_turtle.penup()
#     tibi_the_turtle.forward(10)
#     tibi_the_turtle.pendown()


# counter = 0
# while counter < 10:
#     tibi_the_turtle.forward(10)
#     tibi_the_turtle.penup()
#     tibi_the_turtle.forward(10)
#     tibi_the_turtle.pendown()
#     counter += 1


screen = t.Screen()
screen.exitonclick()