from turtle import Screen, Turtle
from snake import Snake
from food import Food 
from scoreboard import Scoreboard
import time


# se crean las dimenciones de la ventana.
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")



snake = Snake()
food = Food()
scoreboard = Scoreboard()





screen.listen()
screen.onkey(snake.up, "up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.left, "Left")

# se crea el cuerpo inicial de la serpiente 
# con sus rerspectivas posiciones iniciales

starting_position=[(0,0),(-20,0),(-40,0)]
segments = []


for position in starting_position:
    new_segment = Turtle("turtle")
    new_segment.color("orange")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)


# Se crea en exit on click para que no se cierre
# la ventana al instante de abrirla.
screen.exitonclick()