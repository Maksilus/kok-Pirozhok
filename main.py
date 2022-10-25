#Вариант 4
import math
orda=open("orda.txt",'r')
c=0
try:
    while True is True:
        x=int((orda.readline()))
        y=math.sqrt(x)
        z=y%2
        if y==round(y) :
            if  z==1:
                c+=1
        if x=="":
            break
except(ValueError):
    print("Количество квадратов нечётных чисел: ",c)
orda.close()
orda=open("orda.txt",'r')
cCH=0
cN=0
cO=0
try:
    while True is True:
        a=int((orda.readline()))
        b=a%2
        if a==0:
            cO+=1
        elif b==1 and a!=0:
            cN+=1
        else:
            cCH+=1
        if x=="":
            break
except(ValueError):
    print("Количество нечётных чисел: ", cN)
    print("Количество чётных чисел: ",cCH)
    print("Количество нулей: ", cO)