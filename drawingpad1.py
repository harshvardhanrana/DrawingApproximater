from turtle import *
from turtle import Turtle, Screen

def drag(i, j):
    tur.ondrag(None)
    tur.setheading(tur.towards(i, j))
    tur.goto(i, j)
    tur.ondrag(drag)
    print(i ,j)
    file.write('{}+{}j\n'.format(i,j))
    file.flush()

def turtmove(x, y):
    ws.onscreenclick(None)
    tur.penup()
    tur.goto(x, y)
    tur.down()


ws = Screen()
#ws.setup(width=600,height=600)
#ws.bgpic('C://Users//harsh//Documents//python files//random stuff//Fourier//images//bird1.gif')

tur = Turtle('turtle')
tur.speed('fastest')
tur.shapesize(0.1,0.1,0.1)

ws.onscreenclick(turtmove)

file = open('imagefourier.txt','w')

tur.ondrag(drag)

ws.mainloop()

print("DONE!")