import time
import random
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Score


r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
screen=Screen()
ball=Ball()
score=Score()

screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
game_on=True


screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")






while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 40 or ball.distance(l_paddle) < 40:
        ball.bounce_x()
    if ball.xcor() > 400:
        ball.restart()
        score.l_point()
    if ball.xcor() < -400:
        ball.restart()
        score.r_point()



screen.exitonclick()