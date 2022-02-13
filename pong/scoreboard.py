#############################################################
#Date: 10.02.22                                             #
#Programmed by: Luka Henig (luka.henig@gmail.com)           #
#Curse: 100 Days of Code(udemy)                             #
#Description: Litle pong game to learn and understand       #
#python and the Turtle Library                              #
#############################################################

#imports
from turtle import Turtle

#scoardboard class
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    #show score on Screen
    def update_scoreboard(self):
        """Updates the score on screen, no parameters"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))

    #increment score
    def l_point(self):
        """increments score for left player by one, no parameters"""
        self.l_score += 1
        self.update_scoreboard()

    #increment score
    def r_point(self):
        """increments score for right player by one, no parameters"""
        self.r_score += 1
        self.update_scoreboard()