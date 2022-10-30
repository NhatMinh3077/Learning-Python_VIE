print('center')
# center() trả về một chuỗi được căn giữa với chiều rộng width
# center(width,[fillchar])
A = 'Hello World'
B = A.center(30)
print(B)
C = 'Hello World'  
D = C.center(30, '-')
print(D)

print('Căn trái')
# Căn trái
M = 'Hello World'  
N = M.ljust(30, '-')
print(M)

print('Căn phải')
# Căn phải
m = 'Hello World' 
n = m.rjust(30, '-')
print(n)