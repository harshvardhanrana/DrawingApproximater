import math
import turtle

file = open('C://Users//harsh//Documents//python files//random stuff//Fourier//fourierimageseries.txt','r')
str = file.read()

file.close()

list = str.split('\n')
listA = list[0].split('A')[1::]
listB = list[1].split('B')[1::]

coeffA = []
coeffB = []

for i in range(len(listA)):
    coeffA.append(eval(listA[i]))
    coeffB.append(eval(listB[i]))

def coordi(x):
    f = 0
    for i in range(len(coeffA)):
        f += coeffA[i] * math.sin(i * x) + coeffB[i] * math.cos(i * x)
    return f.real, f.imag

"""def coordi(x,tur):
    f = 0
    for i in range(len(coeffA)):
        f += coeffA[i] * math.sin(i * x) + coeffB[i] * math.cos(i * x)
        tur.setheading(tur.towards(f.real,f.imag))
        tur.goto(f.real,f.imag)"""

ws = turtle.Screen()
ws.bgcolor('black')
tur = turtle.Turtle()
tur.color('white')
tur.speed('fastest')
tur.width(3)

t=-math.pi
tur.penup()


while True:
    L = coordi(t)
    tur.setheading(tur.towards(L))
    tur.goto(L)
    #coordi(t,tur)
    t+=0.01
    tur.down()