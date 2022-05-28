import turtle as t

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(-100, 270)
        self.hideturtle()
        self.write(f'score: {self.score}', align='center', move=True, font=('arial', 15, 'normal'))

    def update(self):
        self.score += 1
        self.clear()
        self.goto(-100, 270)
        self.showturtle()
        self.write(f'score: {self.score}', align='center', move=True, font=('arial', 15, 'normal'))
        self.hideturtle()
        
    def game_over(self):
        self.goto(0,0)
        self.showturtle()
        self.write('game over', align='center', move=True, font=('arial', 30, 'normal'))
        self.hideturtle()

    def replay(self, screen):
        replay = screen.textinput('replay', 'start again (y/n):  ')
        if replay == 'y':
            self.score = -1
            self.clear()
            self.update()
        else:
            screen.bye()