print("give me a sequence of DNA:")
se = input()
dictionary={}
a = 0
c = 0
g = 0
t = 0
for symbol in se:
    if symbol == 'A':
        a=a+1
    if symbol == 'C':
        c=c+1
    if symbol == 'G':
        g=g+1
    if symbol == 'T':
        t=t+1

dictionary['A'] = str(a)
dictionary['C'] = str(c)
dictionary['G'] = str(g)
dictionary['T'] = str(t)    
print(dictionary)

import matplotlib.pyplot as plt

labels = 'A','C','G','T'
sizes = dictionary.values()
explode = (0,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',
        shadow=False,startangle=99)
plt.axis('equal')
plt.show()