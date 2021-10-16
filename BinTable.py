#10-14-21 KYGM
#App that returns binomial probability distribution table

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

def binomial(p,n,x):
    #((N nCr X)*((P)^X)*((1-P)^(N-X))
    probability = ((nCr(n,x))*((p)**x)*((1-p)**(n-x)))
    return probability

n = input("Enter N: ")
p = input("Enter probability: ")
li = input("Enter size of list: ")

p = float(p)
n = int(n)
li = int(li)

while cont == 1:
    
    for i in range(li + 1):
        doge = binomial(p,n,i)
        print(i, ": ", doge)
        
        
    
    cont = input("Enter 1 for another or 0 to end: ")
    cont = int(cont)
    
    

