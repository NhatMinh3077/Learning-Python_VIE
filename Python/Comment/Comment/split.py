print('split')
# Trả về một list
a = 'Hello World'  
b = a.split()
print(a)
print(b)

b = a.split('e')
print(a)
print(b)

b = a.split('l', 1)
print(a)
print(b)

b = a.split(' ', 3)
print(a)
print(b)

# Cắt từ phía bên phải
b = a.rsplit('l', 1)
print(a)
print(b)
