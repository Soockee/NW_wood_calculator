import turtle

#Screen
wn = turtle.Screen()
wn.title("New World Wood Calc")
wn.bgcolor("black")
wn.screensize(600, 300)
wn.tracer(0)

'''
t = "timber" # 4*gr
l = "Lumber" # 2*t (8*gr) and 4*ag
w = "wyrdwoodplanks" # 2*l<=>(16*gr, 8*ag) and 6*wy
i = "ironwoodplanks" # 2*w<=>(32*gr, 16*ag, 12*wy) and 8*ir
'''
#Var
t = int() # Anzahl Timber per User input
l = int() # Anzahl Lumber per User input
w = int() # Anzahl Wyrdwoodplanks per User input
i = int() # Anzahl Ironwoodplanks per User input

tl = int() # Anzahl t pro l
tlw = int() # Anzahl t pro w
tlwi = int() # Anzahl t pro i
lw = int() # Anzahl l pro w
lwi = int() # Anzahl l pro i
wi = int() # Anzahl w pro i

grt = int() # Anzahl green pro t

grl = int() # Anzahl green pro l
agl = int() # Anzahl aged pro l

grw = int() # Anzahl green pro w
agw = int() # Anzahl aged pro w
wyw = int() # Anzahl wyrd pro w

gri = int() # Anzahl green pro i
agi = int() # Anzahl aged pro i
wyi = int() # Anzahl wyrd pro i
iri = int() # Anzahl iron pro i

#Wahl var der Holzart
wahl = turtle.numinput(title="Wahl",prompt="Welches Holz soll berechnet werden?\n1: Timber, 2: Lumber, 3: Wyrd, 4: Iron !")

#User input
if wahl == 1:
    t = turtle.numinput(title="Timber",prompt="Wie viel Timber brauchst du ? ",minval=0,maxval=10000)
elif wahl == 2:
    l = turtle.numinput(title="Lumber",prompt="Wie viel Lumber brauchst du ? ",minval=0,maxval=10000)
elif wahl == 3:
    w = turtle.numinput(title="Wyrdwoodplanks",prompt="Wie viel Wyrdwoodplanks brauchst du ? ",minval=0,maxval=10000)
elif wahl == 4:
    i = turtle.numinput(title="Ironwoodplanks",prompt="Wie viel Ironwoodplanks brauchst du ? ",minval=0,maxval=10000)


#Rechenlogik
gri = 32*i 
agi = 16*i
wyi = 12*i
iri = 8*i
tlwi = 8*i
wi = 2*i
lwi = 4*i

grw = 16*w
agw = 8*w
wyw = 6*w
lw = 2*w
tlw = 4*w

grl = 8*l
agl = 4*l
tl = 2*l

grt = 4*t

#Anzeige
pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.hideturtle()


#main loop
while True:
    wn.update()
    pen.clear()
    if wahl == 1:
        pen.write("Du brauchst: {} Greenwood für: {} Timber!".format(grt, t), align="center", font=("Courier", 24, "normal"))
    
    elif wahl == 2:
        pen.write("Du brauchst:\n\n{} Timber({} Greenwood)\nund {} Agedwood \nfür: {} Lumber!".format(tl, grl, agl, l), align="center", font=("Courier", 24, "normal"))

    elif wahl == 3:
        pen.write("Du brauchst:\n\n{} Lumber\n({} Agedwood,\n{} Timber,\n{} Greenwood)\nund {} Wyrdwood\nfür {} Wyrdwoodplanks!".format(lw, agw, tlw, grw, wyw, w), align="center", font=("Courier", 24, "normal"))
    
    elif wahl == 4:
        pen.write("Du brauchst:\n\n{} Wyrdwoodplanks\n({} Lumber\n({} Agedwood,\n{} Timber,\n{} Greenwood\n,{} Wyrdwood)\nund {} Ironwood\n für {} Ironwoodplanks!".format(wi, lwi, agi, tlwi, gri, wyi, iri, i), align="center", font=("Courier", 24, "normal"))
