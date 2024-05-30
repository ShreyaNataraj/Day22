import colorgram
import turtle as turtle_module

import random
turtle_module.colormode(255)
tim = turtle_module
tim.speed("fastest")
tim.penup()
tim.hideturtle()
rgb_color =[(237, 234, 237), (233, 235, 233), (215, 166, 215), (230, 239, 230), (205, 153, 205), (225, 205, 225), (161, 55, 161), (113, 187, 113), (154, 31, 154), (8, 109, 8), (42, 13, 42), (160, 29, 160), (12, 23, 12), (34, 122, 34), (59, 23, 59), (9, 32, 9), (186, 156, 186), (63, 166, 63), (171, 57, 171), (156, 208, 156), (94, 183, 94), (205, 99, 205), (240, 200, 240), (213, 174, 213), (28, 37, 28), (187, 99, 187), (163, 209, 163), (220, 177, 220), (14, 105, 14)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
no_of_dots = 100
for dot in range(1,no_of_dots+1):
  tim.dot(20,random.choice(rgb_color))
  tim.forward(50)
  if dot%10==0:
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
  