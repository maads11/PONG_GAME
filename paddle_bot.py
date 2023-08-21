import turtle
import time


class PaddleBot(turtle.Turtle):
    def __init__(self, position, ball):
        super().__init__()
        self.penup()
        self.shapesize(5, 1)
        self.shape('square')
        self.color('white')
        self.setposition(position)
        self.ball_position = ball

    def bot_movement(self):
        if self.ball_position.ycor() <= 250 or self.ball_position.ycor() >= - 300:
            new_y = self.ball_position.ycor()
            self.goto(self.xcor(), new_y)
        else:
            self.goto(self.xcor(), self.ycor())

    def paddle_bot_collision(self):
        if self.xcor() - 20 == self.ball_position.xcor() and self.ball_position.ball_current_movement == self.ball_position.ball_movement_south_east:
            self.ball_position.ball_current_movement = self.ball_position.ball_movement_south_west
            self.ball_position.ball_speed +=0.1

        elif self.xcor() - 20 == self.ball_position.xcor() and self.ball_position.ball_current_movement == self.ball_position.ball_movement_north_east:
            self.ball_position.ball_current_movement = self.ball_position.ball_movement_north_west
            self.ball_position.ball_speed +=0.1



# kljsndfjklsndjfklsdnjkf