# Se hace la debida importacion de la libreria Turtle.

from turtle import Turtle

# se definen las posiciones iniciales en las que
# aparecen los segmentos los cuales conforman
# el cuerpo de la serpiente y las variables las 
# cuales se definen de acuerdo a los grados en 
# los que se desea que se mueva la serpiente

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Se crea la clase Snake con las propiedades del cuerpo de la serpiente 
# se le añade la variable STARTING_POSITIONS a la cual se le definieron 
# las posiciones iniciales para los segmentos que conforman el cuerpo de 
# la serpiente

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

# Se le asigna a el cuerpo de la serpiente las respectivas 
# posiciones iniciales.

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

# Se crea la funcion add_segment la cual nos define las propiedades 
# del segmento al momento de añadirlo al cuerpo de la serpiente

    def add_segment(self, position):
        new_segment = Turtle("turtle")
        new_segment.color("orange")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

# Se define la funcion extend la cual nos define las posiciones 
# iniciales del segmento al momento de añadirlo

    def extend(self):
        self.add_segment(self.segments[-1].position())

# Se define la funcion move la cual nos define que al momento 
# de añadir un segmento al cuerpo de la serpiente el cuerpo de la 
# serpiente se debe extender y se define la posicion en la cual
# quedara el nuevo segmento

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

# Se define la funcion up la cual nos define el movimiento
# de la serpiente hacia arriba en un angulo de 90 grados.

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading (UP)

# Se define la funcion down la cual nos define el movimiento
# de la serpiente hacia abajo en un angulo de 270 grados.

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

# Se define la funcion left la cual nos define el movimiento
# de la serpiente hacia la izquierda en un angulo de 180 grados.

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

# Se define la funcion rigth la cual nos define el movimiento
# de la serpiente hacia la derecha en un angulo de 0 grados.

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

