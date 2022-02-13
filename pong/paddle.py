#############################################################
#Date: 10.02.22                                             #
#Programmed by: Luka Henig (luka.henig@gmail.com)           #
#Curse: 100 Days of Code(udemy)                             #
#Description: Litle pong game to learn and understand       #
#python and the Turtle Library                              #
#############################################################

#imports
from turtle import Turtle

#player class
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """To move the player 20 pixels up, no parameters"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """To move the player 20 pixels down, no parameters"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)