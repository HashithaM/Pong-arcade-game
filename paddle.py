from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_up(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto(x_cor, y_cor + 40)

    def move_down(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto(x_cor, y_cor - 40)

