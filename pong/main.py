#############################################################
#Date: 10.02.22                                             #
#Programmed by: Luka Henig (luka.henig@gmail.com)           #
#Curse: 100 Days of Code(udemy)                             #
#Description: Litle pong game to learn and understand       #
#python and the Turtle Library                              #
#############################################################

#imports
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#constants
WIDTH = 800
HEIGHT = 600
PADDLE_POSITION = 350
WALL_T_B = 280
WALL_L_R = 380
PADDLE_DISTANCE = 50
PADDLE_L_R = 320
BALL_DELAY = 0.075

#screen handling
screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Pong")
screen.tracer(0)    #to avoid moving animation

#create player
r_paddle = Paddle((PADDLE_POSITION, 0))
l_paddle = Paddle((-PADDLE_POSITION, 0))

#create ball
ball = Ball()

#create scoreboard
scoreboard = Scoreboard()

#player control
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

#Game loop
game_is_on = True
while game_is_on:
    time.sleep(BALL_DELAY)
    screen.update()
    ball.move()

    #detect collision with wall
    if (ball.ycor() > WALL_T_B or ball.ycor() < -WALL_T_B):
        ball.bounce_y()

    #detect collision with paddle
    if (ball.distance(r_paddle) < PADDLE_DISTANCE and ball.xcor() > PADDLE_L_R or ball.distance(l_paddle) < PADDLE_DISTANCE and ball.xcor() < -PADDLE_L_R):
        ball.bounce_x()

    #detect ball miss r_paddle
    if (ball.xcor() > WALL_L_R):
        ball.restart()
        scoreboard.l_point()

    #detect ball miss l_paddle
    if (ball.xcor() < -WALL_L_R):
        ball.restart()
        scoreboard.r_point()

#keep screen alive
screen.exitonclick()