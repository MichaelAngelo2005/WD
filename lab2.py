import sys

def zad1():
    return len(input("input a sentence\n").split())

def zad2():
    a,b,c=int(sys.stdin.readline()),int(sys.stdin.readline()),int(sys.stdin.readline())
    sys.stdout.write(str(a**b+c))

def zad3():
    str=input("input a word\n").lower()
    return str==str[::-1]

def zad3b():
    str=list(input("input a word\n").lower())
    str2=str
    str2.reverse()
    return str==str2
    
def zad4():
    n=int(input("input a number"))
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

def zad5():
    perfect=[]
    for n in range(1001):
        divs=[]
        for i in range(1,n//+1):
            if n%i==0:
                divs.append(i)
        if sum(divs)==n:
            perfect.append(n)
    return perfect

def zad6():
    list=[1,2.0,3,4.0,5,6.0,7,8.0]
    for i in range(len(list)):
        list[i]=list[i]**2
    return list

def zad7():
    y=0
    list=[]
    while y<10:
        x=int(input())
        if x%2==0:
            list.append(x)
        y+=1
    return list
        
def zad8():
    list=[1,2,3,4,"a","b","c","d",(1,2),(3,4),1,1]
    dict={item:list.count(item) for item in list}
    return dict











