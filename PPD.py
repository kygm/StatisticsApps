#10-14-21 KYGM
#App that returns poisson probability distribution

import math

cont = 1
 
# Returns factorial of n
def fact(n):
 
    res = 1
     
    for i in range(2, n+1):
        res = res * i
         
    return res


while cont == 1:
    
    lbd = input("Enter Lambda: ")
    x = input("Enter X: ")
    t = input("Enter t: ")
    
    lbd = float(lbd)
    x = int(x)
    t = int(t)
    
    ppd = (((lbd*t)**x)/(fact(x)))*math.exp((-lbd)*t)
    print(ppd)
    
    cont = input("Enter 1 for another or 0 to end: ")
    cont = int(cont)
    
    

