import turtle
import paddle
import paddle_bot
import time
import ball
import frame

screen = turtle.Screen()
screen.setup(800, 600)
screen.title('PONG')
screen.bgcolor('black')
screen.tracer(0)

ball = ball.Ball((0, 0))
scoreboard = frame.Scoreboard()

paddle_A = paddle.Paddle((-350, 0), ball)
paddle_B = paddle_bot.PaddleBot((350, 0), ball)

upper_frame = frame.Frame((0, 315), ball)
lower_frame = frame.Frame((0, -315), ball)

middle_screen_stripe = turtle.Turtle()
middle_screen_stripe.shapesize(500, 0.1)
middle_screen_stripe.shape('square')
middle_screen_stripe.color('white')
middle_screen_stripe.setposition(0, 0)

screen.listen()
screen.onkeypress(paddle_A.go_up, 'Up')
screen.onkeypress(paddle_A.go_down, 'Down')

game_on = True
while game_on:
    if ball.xcor() == paddle_A.xcor() - 60:
        scoreboard.pc_score_refresh()
        ball.setposition(0, 0)
        ball.ball_current_movement = ball.ball_movement_north_east
        time.sleep(1)
    if ball.xcor() > paddle_B.xcor():
        scoreboard.my_score_refresh()
    ball.ball_current_movement()
    paddle_B.bot_movement()
    paddle_A.paddle_collision()
    paddle_B.paddle_bot_collision()
    upper_frame.check_collision()
    lower_frame.check_collision()
    screen.update()
    time.sleep(0.000001)

screen.exitonclick()

