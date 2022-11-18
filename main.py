# Se importan las clases correspondientes
# necesarias las cuales se crean con anterioridad
# en otros archivos en la misma carpeta.

from turtle import Screen, Turtle
from snake import Snake
from food import Food 
from scoreboard import Scoreboard
import time

# Se crea la ventana con sus correspondientes dimensiones
# color, titulo.

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Se definen ciertas variables a las cuales
# se les asigna el valor de una clase a cada
# para manejar los parametros de las clases 
# de manera mas sencilla

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Se enlistan los movimientos en los cuales se podra
# mover la serpiente estos se definieron con anterioridad 
# en el archivo snake.py al cual importamos desde un
# inicio.

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Se define la variable game_is_on
# la cual esta junto a un ciclo while 
# el cual nos define que la pagina se 
# va a actualizar en un tiempo de 0.1 sg
# lo que es nos deja una velocidad mayor 
# a la normal que es de 1 sg

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# Se definen ciertas condiciones if, la primera
# nos define que si la cabeza de la serpiente es
# menor que 15 pixeles nos refrescara la comida
# la cual nos aparecera en otro logar al azar 
# ademas de eso se define que en el momento de
# cumplir esa funcion se extenderia el cuerpo de
# la serpiente lo cual se define en snake.extend
# y por ultimo se define que al pasar esto el puntaje
# se va incrementando.

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

# Esta condicion lo que define en que este en una 
# posicion mayor a 280 pixeles en direccion positiva
# o menor que -280 pixeles en direccion negativa o mayor 
# que 280 pixeles en direccion positiva vertical o menor 
# que -280 pixeles en direccion negativa vertical entonces
# se acabara el juego mostrando un mensaje de Game Over.

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.Game_Over()

# Esta condicion es para el caso tal que se llege a tener
# una longitud muy larga en la serpiente la cual define
# que si la cabeza esta a menos de 10 pixeles de la cabeza
# se mostrara la funcion Game Over que señala el fin del juego
# y en caso de que todo este en normalidad el juago continuara.

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.Game_Over()

# Este metodo funciona para marcar la salida de la
# ventana la cual se hara a partir de un click en 
# la equis de la barra superior.
            
screen.exitonclick()