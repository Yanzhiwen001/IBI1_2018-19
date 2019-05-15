#input
x=2019
n=-1
#save the initial value of x
final=str(x)+" is"
list=[]
#divide x by 2 , count the order and save the result
while 0<x<8192:
#it is special when x= 1 or 2
    if x ==2:
        n=n+2
        message = " 2**"+str(n)
        list.append(message)
        break
    if x==1:
        n=n+1
        message = " 2**"+str(n)
        list.append(message)
        break
    if x%2 != 0:
        n=n+1
        x=(x-1)/2
        message=" 2**"+str(n)+" +"
        list.append(message)
    else:
        x=x/2
        n=n+1
#print all the elements in the list
for messages in list:
    final=final+messages
print(final)
