# Lấy toàn bộ nội dung của thư viện decimal
from decimal import*

# Lấy tối đa 30 chữ số phần nguyên và phần thập phân decimal
getcontext().prec = 30

f = 10/3
print(f)
print(type(f))

d = Decimal(10)/Decimal(3)
print(d)
print(type(d))

print(10/3)
print(Decimal(10)/Decimal(3))