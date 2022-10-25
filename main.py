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
    print(c)