import turtle as t

class Border(t.Turtle):
    def __init__(self, size):
        super().__init__()
        cor = (size/2) - 10
        self = t.Turtle('arrow')
        self.speed('fastest')
        self.color('white')
        self.penup()
        self.goto(-cor, -cor)
        self.pendown()
        self.goto(-cor,cor)
        self.goto(cor,cor)
        self.goto(cor,-cor)
        self.goto(-cor,-cor)