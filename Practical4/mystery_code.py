# What does this piece of code do?
# Answer: it finds out a prime number in the range of (1,100) randomly

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
while p==False:
    p=True
#choose a random number
    n = randint(1,100)
#find the biggest possible divisor of x
    u = ceil(n**(0.5))
#find out whether there exist some divisors of x
    for i in range(2,u+1):
        if n%i == 0:
#if not p=ture and break the loop
            p=False


     
print(n)
            