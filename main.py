import turtle as t
import time
from snake import Snake
from apple import Apple
from scoreboard import Scoreboard
from border import Border

screen_size = 600

screen = t.Screen()
screen.tracer(0)
screen.setup(screen_size, screen_size)
screen.bgcolor('black')
border = Border(screen_size)

apple = Apple()
snake = Snake()
scoreboard = Scoreboard()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while True:
    screen.update()
    screen.listen()
    game_on = True
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(apple) < 20:
        apple.random_location()
        snake.add_segment()
        scoreboard.update()

    if abs(snake.head.xcor()) >= 295 or abs(snake.head.ycor()) >= 295:
        game_on = False
    for i in snake.segments[1:]:
        if snake.head.distance(i) < 10:
            game_on = False

    if game_on == False:
        scoreboard.game_over()
        snake.reset()
        scoreboard.replay(screen)
