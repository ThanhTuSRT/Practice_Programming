a=int(input("Nhập cạnh a: "))
b=int(input("Nhập cạnh b: "))
c=int(input("Nhập cạnh c: "))
print()
print('Chu vi hình tam giác là: ', a+b+c)
print('Nửa chu vi hình tam giác là: ', (a+b+c)/2)
import math
p = (a+b+c)/2
number = math.sqrt(p*(p-a)*(p-b)*(p-c))
print('Diện tích hình tam giác là: ', round(number,1))