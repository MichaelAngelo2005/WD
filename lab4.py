from math import e,log,sin,cos,pi
import random

def zad1():
    s1=(e**4-log(34,2))**(1/3)
    s2=(log(20)+cos(45)+e)**(1/3)
    s3=(log(20,3)+sin(45)*5/8)**(1/4)
    s4=log(23,3)+(sin(34)+5)**(1/3)
    s5=(log(32,2)+pi+sin(56))**(1/4)
    ss=[s1,s2,s3,s4,s5]
    for s in ss:
        print(f"{s:.2f}",end=" ")
    
def zad2(x):
    if x<=10:
        for i in range(1,x+1):
            print(i*"A")

def zad3(x):
    if x<=10:
        for i in range(1,x+1):
            print((x-i)*" "+(2*i-1)*"A")

def zad5(n):
    M=[random.choices(range(-100,100),k=n) for i in range(n)]
    return [sum(row) for row in M]