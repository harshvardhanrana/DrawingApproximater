from distutils.log import error
import math

file2 = open('C://Users//harsh//Documents//python files//random stuff//Fourier//imagefourier.txt','r')
List2 = (file2.read()).split('\n')[:-1]
file2.close()
dx = 0.001

iter = int(input("Enter how much precision you want [recommended: 5-50]: "))

z1 = int((2 * math.pi / dx) // len(List2))
z2 = math.floor((2 * math.pi / dx) % len(List2))

List3 = []
counter = 0

if 2*math.pi/dx >= len(List2):
    for i1 in List2:
        if counter <= z2:
            List3.extend([eval(i1)] * (z1+1))
        else:
            List3.extend([eval(i1)] * z1)
        counter += 1

else:
    pass

print(len(List3))




def f(x):
    y = math.floor((math.pi + x)/dx)
    return List3[y]

x = - math.pi


integralA = 0
integralB = 0

A=[]
B=[]
print('initiated')
for i in range(iter):
    while x < math.pi:
        integralA += math.sin(i*x) * f(x) * dx
        integralB += math.cos(i*x) * f(x) * dx
        x+=dx
    A += [integralA  / math.pi]
    B += [integralB  / math.pi]
    integralA = 0
    integralB = 0
    x= - math.pi

B[0]/=2

file = open('C://Users//harsh//Documents//python files//random stuff//Fourier//fourierimageseries.txt', 'w')
for j in range(len(A)):
    file.write('A{}'.format(A[j]))
file.write('\n')
for k in range(len(B)):
    file.write('B{}'.format(B[k]))

file.close()
print('done')