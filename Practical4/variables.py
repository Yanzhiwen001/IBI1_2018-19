#input
a=223
b=223223
#judge if b could be divided by 7
if b%7 == 0:
    print(b)
c=b/7
d=c/11
e=d/13
#compare a e
if a>e:
    print(a)
else:
    print(e)
    
X=1>0
Y=1<0
Z=(X and not Y)or(Y and not X)
W= X!=Y
print(X,Y,Z,W)
