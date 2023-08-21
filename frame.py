import turtle
import time


class Frame(turtle.Turtle):
    def __init__(self, position, ball):
        super().__init__()
        self.penup()
        self.shapesize(1, 500)
        self.shape('square')
        self.color('white')
        self.goto(position)
        self.ball = ball

    def check_collision(self):
        if self.ball.ball_current_movement == self.ball.ball_movement_north_east and self.ball.ycor() >= 290:
            self.ball.ball_current_movement = self.ball.ball_movement_south_east
        if self.ball.ball_current_movement == self.ball.ball_movement_north_west and self.ball.ycor() >= 290:
            self.ball.ball_current_movement = self.ball.ball_movement_south_west
        if self.ball.ball_current_movement == self.ball.ball_movement_south_east and self.ball.ycor() <= -290:
            self.ball.ball_current_movement = self.ball.ball_movement_north_east
        if self.ball.ball_current_movement == self.ball.ball_movement_south_west and self.ball.ycor() <= -290:
            self.ball.ball_current_movement = self.ball.ball_movement_north_west


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.my_score = 0
        self.pc_score = 0
        self.hideturtle()
        self.goto(0, 260)
        self.color('white')
        self.write(f'ME :  {self.my_score}         PC :  {self.pc_score}', move=False, align='center', font=('Arial', 20, 'normal'))

    def my_score_refresh(self):
        self.clear()
        self.my_score += 1
        self.hideturtle()
        self.goto(0, 260)
        self.color('white')
        self.write(f'ME :  {self.my_score}         PC :  {self.pc_score}', move=False, align='center', font=('Arial', 20, 'normal'))

    def pc_score_refresh(self):
        self.clear()
        self.pc_score += 1
        self.hideturtle()
        self.goto(0, 260)
        self.color('white')
        self.write(f'ME :  {self.my_score}         PC :  {self.pc_score}', move=False, align='center', font=('Arial', 20, 'normal'))