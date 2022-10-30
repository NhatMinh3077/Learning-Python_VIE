a = 'Hello'
b = 'World'

print("Lấy kí tự đầu tiên của chữ Hello tại a")
# Lấy kí tự đầu tiên ở "Hello" tại a
c = a[0]
print(c)

print("Lấy ngược lại kí tự Hello ở a xuất phát từ H")
# Lấy ngược lại kí tự Hello  ở python 1 xuất phát từ H
d = a[-1]
print(d)

print("Lấy bớt kí tự từ chữ Hello")
e = a[1:None]
print(e)

print("Lấy bớt kí tự từ chữ Hello")
f = a[None:5]
print(f)

print("In ra giá trị của a")
g = a[:] 
print(g)

print("Lấy bớt kí tự của Hello")
h= a[None:None:2]
print(h)

# Cách thay số 0 cho chữ o ở World
l = b[None:1] + "0" + b[2:None]
print(l)