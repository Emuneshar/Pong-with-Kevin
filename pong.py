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
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("blue")
leftPaddle.shapesize(stretch_len=5, stretch_wid=-1)


while True:
    window.update()