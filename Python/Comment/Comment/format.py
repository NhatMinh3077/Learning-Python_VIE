# Định dạng bằng phương thức format
# Cho phép python định dạng chuỗi

# Ví dụ 1
print('Dùng format')
a = 'a:{}\nb:{}\nc:{}'.format(1,2,3)
print(a) 

print('Dùng %d')
# Tương tự như dùng phương thức format trên
b = 'a:%d\nb:%d\nc:%d' %(1,2,3)
print(b)


# Ví dụ 2
# Ở đây 'one' được hiểu là {0}
# 'two' được hiểu là {1}
# 'three' được hiểu là {2}
print('Dùng format')
c = 'a:{1}\nb:{2}\nc:{0}'.format('one','two','three')
print(c)
# Có thể lặp lại {0}