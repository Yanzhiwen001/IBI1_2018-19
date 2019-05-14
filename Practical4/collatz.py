#displays the Collatz sequence for any number
#input the number
m=input('write a positive integer:')
print(int(m))
n=int(m)
# dividing by 2 (if n is even) or multiplying by 3 and adding 1 
while n>1:
    if n%2 ==0:
        n=n/2
    else:
        n=n*3+1
    print(n)
