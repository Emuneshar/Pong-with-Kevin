import turtle
import os 

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height = 600)
window.tracer(0)

leftScore = 0
rightScore = 0

leftPaddle = turtle.Turtle()


while True:
    window.update()