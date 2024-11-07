from turtle import Turtle, Screen

from Scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

# TODO 1 - build the screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

# TODO 2 - Build the paddle and make it move

screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
pong_ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "z")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(pong_ball.move_speed)
    screen.update()
    pong_ball.move()

    # detect collision with wall
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_y()

    # detect collision with a paddle
    if pong_ball.xcor() > 320 and pong_ball.distance(r_paddle) < 40 or pong_ball.xcor() < -320 and pong_ball.distance(
            l_paddle) < 40:
        pong_ball.bounce_x()

    #detect R paddle misses
    if pong_ball.xcor() > 380:
        pong_ball.reset()
        scoreboard.l_point()

    # detect L paddle misses
    if pong_ball.xcor() < -400 :
        pong_ball.reset()
        scoreboard.r_point()

screen.exitonclick()

# TODO 7 - detect when paddle misses

# TODO 8 - keep score
