import random
import math

def zad1():
    A={1-x for x in range(1,11)}
    B={4**i for i in range(0,8,1)}
    C={x for x in B if x%2==0}
    print(A)
    print(B)
    print(C)

def zad2():
    ls1=list(random.choices(range(-100,100,1),k=10))
    ls2=[x for x in ls1 if x%2==0]
    print(ls1)
    print(ls2)

def zad3():
    dict={"ground beef":"kg", "ground bizon":"kg", "figs":"piece", "manuka honey":"l", "raw milk":"l"}
    ls=[item for item in dict if dict[item]=="piece"]
    print(dict)
    print(ls)

def is_right(a,b,c):
    return a**2+b**2+c**2-2*max(a,b,c)**2==0

def area_of_trapezoid(a=0,b=0,h=0):
    return ((a+b)*h)/2

def series_product(a1=1,b=4,length=10):
    return a1*b**length
    
def zad7():
    x=int(input("type in a number: "))
    try:
        print(math.sqrt(x))
    except ValueError:
        print("x was negative")

if __name__=="main":
    zad1()
    zad2()
    zad3()
    print(is_right(3,4,5))
    print(area_of_trapezoid(2,4,10))
    print(series_product(5,2,4))
    zad7()
    