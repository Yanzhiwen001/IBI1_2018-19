#input DNA
print("give me a sequence of DNA:")
se = input()
dictionary={}
#no need of se =se.split('')
#count words
for word in se:
       if word in dictionary:
           dictionary[word] += 1
       else:
           dictionary[word] = 1
print(dictionary)

# make plot
import matplotlib.pyplot as plt

labels =dictionary.keys()
sizes = dictionary.values()
explode = (0,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',
        shadow=False,startangle=99)
plt.axis('equal')
plt.show()
