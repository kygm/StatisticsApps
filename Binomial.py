#10-13-21 KYGM
#App that returns binomial probability distribution

import math

cont = 1

def nCr(n, r):
 
    return (fact(n) / (fact(r)
                * fact(n - r)))
 
# Returns factorial of n
def fact(n):
 
    res = 1
     
    for i in range(2, n+1):
        res = res * i
         
    return res


while cont == 1:
    
    n = input("Enter N: ")
    p = input("Enter probability: ")
    x = input("Enter X: ")
    
    x = int(x)
    p = float(p)
    n = int(n)
    #((N nCr X)*((P)^X)*((1-P)^(N-X))
    #current issue: find compatible combinations lib
    probability = ((nCr(n,x))*((p)**x)*((1-p)**(n-x)))
    print(probability)
    
    cont = input("Enter 1 for another or 0 to end: ")
    cont = int(cont)
    
    
