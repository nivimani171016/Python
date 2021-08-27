#Write code to draw a regular pentagon (a five-sided figure with all sides the same length).
import turtle
wn = turtle.Screen()
wn.bgcolor("red")
pento = turtle.Turtle()
pento.color("Green")
pento.forward(100)
for x in range(4):
    pento.left(73)
    pento.forward(100)
wn.exitonclick()
