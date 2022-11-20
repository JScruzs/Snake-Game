# Se importa la libreria turtle y se importa la funcion random 
# la cual es para que un elemento sea al azar.

from turtle import Turtle
import random

# Se crea la clase Food la cual se define para que
# se cree los elementos de la comida definiendoles el color,
# la forma, la velocidad en la que tiene que aparecer y el tamaño
# para que aparesca de manera aleatoria se definen las variables
# random_x para los limites horizontales y random_y para los 
# limites verticales a las cuales se les pone un limite de
# posiciones de -280 pixeles y 280 pixeles a lo que se refiere
# es que los elementos no pueden aparecer en ningun lugar fuera
# de esos limites definidos

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("purple")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)