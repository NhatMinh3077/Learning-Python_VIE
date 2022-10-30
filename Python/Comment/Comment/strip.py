print('strip')
# Trả về một chuỗi với phần đầu và phần đuôi của chuỗi được bỏ đi, v.v
a = 'có gì hót'  
b = a.strip('t')
print(b)

a = '   có gì hót   '  
b = a.strip()
print(b)

a = 'có gì hót'  
b = a.strip('c')
print(b)

a = 'cbcbcbcbcó gì hót'  
b = a.strip('cb')
print(b)

print('Cắt phía bên phải')
# Cắt phía bên phải
a = 'cbcó gì hótcb'  
b = a.rstrip('cb')
print(b)

print('Cắt phía bên trái')
# Cắt phía bên trái 
a = 'cbcó gì hótcb'  
b = a.lstrip('cb')
print(b)