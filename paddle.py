import turtle
import time


class Paddle(turtle.Turtle):
    def __init__(self, position, ball):
        super().__init__()
        self.penup()
        self.shapesize(5, 1)
        self.shape('square')
        self.color('white')
        self.goto(position)
        self.vector = None
        self.ball_position = ball

    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)
        self.vector = 'Up'
        print(self.distance(self.ball_position.position()))

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
        self.vector = 'Down'
        print(self.distance(self.ball_position.position()))

    def paddle_collision(self):
        if self.xcor() + 20 == self.ball_position.xcor() and self.distance(self.ball_position.position()) < 100 and self.ball_position.ball_current_movement == self.ball_position.ball_movement_north_west:
            self.ball_position.ball_current_movement = self.ball_position.ball_movement_north_east
        if self.xcor() + 20 == self.ball_position.xcor() and self.distance(self.ball_position.position()) < 100 and self.ball_position.ball_current_movement == self.ball_position.ball_movement_south_west:
            self.ball_position.ball_current_movement = self.ball_position.ball_movement_south_east

