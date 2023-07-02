from turtle import Screen
from snake import Snake
from Food import Food
from score import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food=Food()
score=ScoreBoard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# detect eating food

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.Increase()

# detect collision with wall

    if any([snake.head.xcor() >290,snake.head.xcor() <-290 ,snake.head.ycor() >290,snake.head.ycor() <-290]):
        game_on=False
        score.game_over()

# detect collision with tail

    for square in snake.squares[1:]:
        if snake.head.distance(square)<10:
            game_on=False
            score.game_over()

screen.exitonclick()