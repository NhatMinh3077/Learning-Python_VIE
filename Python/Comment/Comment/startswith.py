print('starstwith')
a = 'Hello World'  
b = a.startswith('Hello')
print(a)
print(b)

b = a.startswith('Hello', 4)
print(a)
print(b)

b = a.startswith('Hello',0, 1)
print(a)
print(b)

b = a.startswith('l')
print(a)
print(b)