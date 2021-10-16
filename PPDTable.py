#10-14-21 KYGM
#App that returns poisson probability distribution table
#complete

import math

cont = 1
 
# Returns factorial of n
def fact(n):
 
    res = 1
     
    for i in range(2, n+1):
        res = res * i
         
    return res

#Returns PPD
def ppd(lbd,t,x):
    ppd = (((lbd*t)**x)/(fact(x)))*math.exp((-lbd)*t)
    return ppd

#input constants
lbd = input("Enter Lambda: ")
t = input("Enter t: ")
li = input("Enter list size: ")

#casting
lbd = float(lbd)
t = int(t)
li = int(li)

while cont == 1:
    
    for i in range(li + 1):
        doge = ppd(lbd,t,i)
        print(i, ": ", doge)
        
    
    cont = input("Enter 1 for another or 0 to end: ")
    cont = int(cont)
    
    


