import turtle as t
import random

class Apple (t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.speed('fastest')
        self.random_location()

    def random_location(self):
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.goto(x, y)

