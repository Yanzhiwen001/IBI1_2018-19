print('give me a string of words:')
nonsense = 'tree flower butter milk virus'
print(nonsense)
a = nonsense[-1:-len(nonsense)-1:-1]
print(a)
n1 = a.split()
print(n1)
n1.reverse()
print(n1)