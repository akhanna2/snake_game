import turtle as t

STARTING_POSITION = [(0,0), (0,-20), (0,-40)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITION:
            new_segment = t.Turtle('square')
            new_segment.color('green')
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            newx = self.segments[i - 1].xcor()
            newy = self.segments[i - 1].ycor()
            self.segments[i].goto(newx, newy)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def add_segment(self):
        self.add_new_segment = t.Turtle('square')
        self.add_new_segment.color('green')
        self.add_new_segment.penup()
        self.add_new_segment.goto(self.segments[-1].position())
        self.segments.append(self.add_new_segment)       

    def reset(self):
        for i in self.segments:
            i.hideturtle()
        self.__init__()