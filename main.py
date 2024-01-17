from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Score
from divider import Divider
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("The Pong") 
screen.tracer(0)

ball=Ball()
score=Score()
for i in range(0,16):
    divide=Divider((0,i*20))

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if(ball.ycor()>280 or  ball.ycor()<-280):
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    if ball.xcor()>380 :
        ball.point()
        score.l_point()
    if ball.xcor()<-380 :
        ball.point()
        score.r_point()
screen.exitonclick()