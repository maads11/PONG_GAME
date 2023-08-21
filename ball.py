import turtle


class Ball(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shapesize(1, 1)
        self.shape('circle')
        self.color('white')
        self.goto(position)
        self.vector = None
        self.ball_current_movement = self.ball_movement_north_east
        self.ball_speed = 5

    def ball_movement_north_east(self):
        self.vector = 'Up'
        new_x = self.xcor() + self.ball_speed
        new_y = self.ycor() + self.ball_speed
        self.goto(new_x, new_y)

    def ball_movement_north_west(self):

        self.vector = 'Up'
        new_x = self.xcor() - self.ball_speed
        new_y = self.ycor() + self.ball_speed
        self.goto(new_x, new_y)

    def ball_movement_south_east(self):

        self.vector = 'Down'
        new_x = self.xcor() + self.ball_speed
        new_y = self.ycor() - self.ball_speed
        self.goto(new_x, new_y)

    def ball_movement_south_west(self):

        self.vector = 'Down'
        new_x = self.xcor() - self.ball_speed
        new_y = self.ycor() - self.ball_speed
        self.goto(new_x, new_y)


