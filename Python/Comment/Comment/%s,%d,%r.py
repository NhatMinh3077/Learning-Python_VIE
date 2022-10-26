print("Công dụng của %s")
# %s là giá trị của phương thức __str__ của đối tượng đó
# Dùng %s, %d, v.v và gán giá trị cho % đó để thay vào giá trị kia 
#Cách 1
a = 'Hello %s' %('World')
print(a)

#Cách 2
b = 'Hello %s and %s' %('World','Python')
print(b)

#Cách 3
python19 = 'Hello %s and %s'
print(python19 %('World','Python'))

#Cách 4
c = 'Hello %s and %s' 
result = c %('World','Python')
print(result)

# %s là giá trị của phương thức __str__ của đối tượng đó
# %r Giá trị của phương thức __repr__ của đối tượng đó
# %d là giá trị của một số - Nếu là số sẽ được chuyển sang số thực 