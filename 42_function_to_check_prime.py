import math

def isPrime(num):
    
    prime = True

    if num == 1:
        prime = False
    
    for i in range(2, math.ceil(num / 2) + 1):
        if num % i == 0:
            prime = False
    
    if prime:
        print("Prime")
    else:
        print("Not Prime")


num = int(input("Enter a numbe to check whether it is prime or not : "))
isPrime(num)