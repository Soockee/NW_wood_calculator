from entities import Item

from turtle import Screen, Turtle
from Button import Button
from ButtonHandler import handle

def main():
	#Screen
	screen = Screen()
	screen.title("New World Wood Calc")
	screen.screensize(600, 300)
	screen.tracer(0)

	#Anzeige
	pen = Turtle()
	pen.color("black")
	pen.speed(0)
	pen.penup()
	pen.hideturtle()


	# Buttons with callback function
	buttons = []
	buttons.append( Button("Timber", (-500, -100), lambda x, y: handle(screen, pen, "timber")))
	buttons.append( Button("Lumber", (-500, -200), lambda x, y: handle(screen, pen, "timber")))
	buttons.append( Button("wyrdwoodplanks", (-500, -300), lambda x, y: handle(screen, pen, "wyrdwoodplanks")))
	buttons.append( Button("ironwoodplanks", (-500, -400), lambda x, y: handle(screen, pen, "ironwoodplanks")))

	#onClick Event on each button
	for button in buttons:
		screen.onclick(button.clickButton, add=True)

	# main loop
	while True:
	 	screen.update()


if __name__ == "__main__":

    main()