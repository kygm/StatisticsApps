#10-14-21 KYGM
#App that returns poisson probability with no t
#complete

import math

cont = 1
 
# Returns factorial of n
def fact(n):
 
    res = 1
     
    for i in range(2, n+1):
        res = res * i
         
    return res


while cont == 1:
    
    u = input("Enter mean: ")
    x = input("Enter X: ")
    
    u = float(u)
    x = int(x)
    
    ppd = (((u**x))/(fact(x)))*math.exp((-u))
    print(ppd)
    
    cont = input("Enter 1 for another or 0 to end: ")
    cont = int(cont)
    
    



