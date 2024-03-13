import math
import random


def zad1():
    results=[]
    for x in range(25,41):
        results.append(round((math.sin(x)+math.log(36,4))**(1/3),2))
    print(results)


def zad2(min=0,max=0,ile=0,n=0):
    ls=[random.randint(min,max) for i in range(ile)]
    if len(ls)%n!=0:
        print("wrong dimensions")
        return
    indexes=list(range(0,len(ls)+1,n))
    return [ls[i:j] for i,j in zip(indexes[0:-1],indexes[1:])]
    

def zad3(nazwa_pliku):
    with open(nazwa_pliku) as file:
        rows=[[int(i) for i in row.split(" ")] for row in file.read().split("\n")]
    columns=[[rows[j][i] for j in range(len(rows))] for i in range(len(rows[0]))]
    return [min(col) for col in columns]

     
def zad4():
    try:
        a=int(input())
        h=int(input())
    except:
        print("no letters please")
        return
    if a<0 or h<0:
        print("negative length")
        return
    V=(a**2)*h
    return V
