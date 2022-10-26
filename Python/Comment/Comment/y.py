
print('Capitalize')
# capitalize() giúp in hoa kí tự đầu tiên của giá trị  
a = 'hello'
b = a.capitalize()
print(b)

print('Upper')
# upper() giúp tất cả các chữ trong giá trị viết hoa
c = 'hello world'
d = c.upper()
print(d)

print('Lower')
# lower() giúp tất cả các chữ trong giá trị viết thường
e = 'HELLO WORLD'
f = c.lower()
print(f)

print('swapcase')
# swapcase() giúp tất cả các chữ trong giá trị viết thường -> viết hoa, viết hoa -> viết thường
e = 'HeLlO wOrLd'
f = e.swapcase()
print(f)

print('title')
# title() giúp các từ viết hoa chữ cái đầu tiên còn lại viết thường
g = 'HeLlO wOrLd'
h = e.title()
print(h)

print('center')
# center() trả về một chuỗi được căn giữa với chiều rộng width
A = 'Hello World'
B = A.center(30)
print(B)