from turtle import Turtle
import random


class Food(Turtle):  # crear clase Food, la herencia es entre parentesis, en este caso desde Turtle (padre)

    def __init__(self):  # definir constructor
        super().__init__()  # herede todo de Turtle (shape, penup, shapesize)
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("red")
        self.refresh()  # para que la comida aparezca en lugar diferente cada vez q se abre la pantalla

    def refresh(self):  # metodo para refrescar y generar nuevo lugar de la comida
        # no debe pasar de 300 ó se sale de la pantalla
        random_x = random.randint(-200, 200)
        # no debe pasar de 300 ó se sale de la pantalla
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)
