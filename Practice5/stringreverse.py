print('give me a string of words:')
nonsense = input()
a = nonsense[-1:-len(nonsense)-1:-1]

n1 = a.split()

n1.reverse()
print(n1)