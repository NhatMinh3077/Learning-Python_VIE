print('Căn lề giữa')
# Căn lề giữa
# Ở đây 50 là khoảng cách mà lệnh sẽ căn
# >>> '{:^10}'.format('Python')
a = '{:^50}'.format('Hello')
print(a)

print('Căn lề trái')
# Căn lề trái
# Ở đây 10 là khoảng cách mà lệnh sẽ căn
# >>> '{:<10}'.format('Python')
b = '{:<10}'.format('Hello')
print(b)

print('Căn lề phải')
# Ở đây 10 là khoảng cách mà lệnh sẽ căn
# >>> '{:>10}'.format('Python')
# Căn lề phải 
c = '{:>10}'.format('Hello')
print(c)

print('Căn lề trái, thay thế khoảng trắng bằng kí tự *')
# Căn lề trái, thay thế khoảng trắng bằng kí tự *
## >>> '{:*>10}'.format('Python')
d = '{:*>10}'.format('Hello')
print(d)

print('# Căn lề phải, thay thế khoảng trắng bằng kí tự *')
# Căn lề phải, thay thế khoảng trắng bằng kí tự *
# >>> '{:*<10}'.format('Python')
e = '{:*<50}'.format('Hello')
print(e)

# Có thể thay bất kì kí tự nào vào {:(a)<n}
f = '{:$^50}'.format('Dollar')
print(f)

# Ví dụ
print('Ví dụ')

row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('','','')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID','Ho va ten','Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123','ArchaicDaisy','U.S')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969','Courbet','France')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('','','')
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)