#############################################################
#Date: 10.02.22                                             #
#Programmed by: Luka Henig (luka.henig@gmail.com)           #
#Curse: 100 Days of Code(udemy)                             #
#Description: Litle pong game to learn and understand       #
#python and the Turtle Library                              #
#############################################################

#imports
from turtle import Turtle

#ball class
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """to move the ball, no parameters"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        """to invert the y-koordinate, no parameters"""
        self.y_move *= -1
        self.move_speed *= 0.2

    def bounce_x(self):
        """to inverst the x-koordinate, no parameters"""
        self.x_move *= -1
        self.move_speed *= 0.2

    def restart(self):
        """resets the ball into the middle, no parameters"""
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1


