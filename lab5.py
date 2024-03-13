import numpy as np
from math import sqrt as sq
import string
import random

#zad1
a=np.arange(3,46,3)

#zad2
b=np.arange(10,dtype="float")
c=a.astype("int64")

#zad3
def intmat(n):
    return np.arange(1,n**2+1).reshape((n,n))

#zad4
def powarray(n,m):
    return np.logspace(1,m,m,base=n,dtype=int)

#zad5
def diag(n):
    return np.diag(np.arange(n,0,-1))
  
#zad6
d=np.array(random.choices(string.ascii_lowercase,k=100),dtype=str).reshape(10,10)
d[0,5:]=list("cello")
d[4:,1]=list("violin")
d[np.arange(2,7),np.arange(2,7)]=list("piano")

#zad7
def twodiag(n):
    a=np.diag(n*[2])
    for i in range(n-1,0,-1):
        a[np.arange(i,n),np.arange(n-i)]=(n-i)*[2**(i+1)]
    for i in range(1,n):
        a[np.arange(n-i),np.arange(i,n)]=(n-i)*[2**(i+1)]
    return a

#zad8
def matsplit(array,dir):
    sh=array.shape
    if dir=="ver" and sh[1]%2==0:
        return np.array((array[:,0:sh[1]//2],array[:,sh[1]//2:]))
    if dir=="hor" and sh[0]%2==0:
        return np.array((array[:,0:sh[0]//2],array[:,sh[0]//2:]))
    raise ValueError("wrong dimensions")
        
#zad9
fib = lambda n: n if n <= 1 else fib(n - 1) + fib(n - 2)
fib_sequence = [fib(i) for i in range(25)]
F=np.array(fib_sequence).reshape((5,5))
print(F)