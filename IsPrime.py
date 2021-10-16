#10/13/21 - KYGM
#Check if number is prime

import math
#from fractions import Fraction

cont = 1

while cont == 1:
    num = input("Enter number to see if its prime: ")
    
    num = int(num)
    if num > 1:
 
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
     
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
 
    else:
        print(num, "is not a prime number")
    
    
    cont = input("Another? 0 for no 1 for yes: ")
    cont = int(cont)