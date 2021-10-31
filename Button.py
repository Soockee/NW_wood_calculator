from turtle import Turtle

class Button(Turtle):
    FONT_NAME, FONT_SIZE, FONT_TYPE = 'Arial', 18, 'normal'

    HORIZONTAL_PAD, VERTICAL_PAD = 1.05, 1.15

    def __init__(self, text, position, command=None):
        super().__init__(visible=False)
        self.speed('fastest')
        self.penup()

        self.text = text
        self.position = position
        self.command = command

        self.width, self.height = self.drawButton()

    def drawButton(self):
        x, y = self.position
        self.setposition(x, y - self.FONT_SIZE/2)
        button_font = (self.FONT_NAME, self.FONT_SIZE, self.FONT_TYPE)
        self.write(self.text, align='center', move=True, font=button_font)

        width = 2 * (self.xcor() - x) * self.HORIZONTAL_PAD
        height = self.FONT_SIZE * self.VERTICAL_PAD

        self.setposition(x - width/2, y - height/2)
        self.pendown()

        for _ in range(2):
            self.forward(width)
            self.left(90)
            self.forward(height)
            self.left(90)

        self.penup()

        return width, height

    def deleteButton(self):
        self.clear()
	
    def clickButton(self, x, y):
        c_x, c_y = self.position
        half_w, half_h = self.width/2, self.height/2

        if c_x - half_w < x < c_x + half_w and c_y - half_h < y < c_y + half_h:
            (self.command)(x, y)
