a=int(input("Nhập a: "))
b=int(input("Nhập b: "))
c=int(input("Nhập c: "))
d=int(input("Nhập d: "))

if a >= b and a >= c and a >= d:
    print()
    print('Số lớn nhất là',a)
if b >= a and b >= c and b >= d:
    print()
    print('Số lớn nhất là',b)
if c >= a and c >= b and c >= d:
    print()
    print('Số lớn nhất là',c)
if d >= a and d >= b and d >= c:
    print()
    print('Số lớn nhất là',d)