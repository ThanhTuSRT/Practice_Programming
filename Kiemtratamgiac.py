a=float(input("Nhập độ dài cạnh a: "))
b=float(input("Nhập độ dài cạnh b: "))
c=float(input("Nhập độ dài cạnh c: "))
print()
import math
cv=a+b+c
p=(a+b+c)/2
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print('Chu vi tam giác: ',cv)
print('Diện tích tam giác: ',S)
print()
print('Đường cao cạnh thứ nhất là:',S*2/a)
print('Đường cao cạnh thứ hai là:',S*2/b)
print('Đường cao cạnh thứ ba là:',S*2/c)

if a==b==c:
  print('Tam giác đều')
elif a==b or a==c or b==c:
  print('Tam giác cân')
if a**2==b**2+c**3 or b**2==a**2+c**2 or c**2==a**2+b**2:
  print('Tam giác vuông')
if a**2==b**2+c**3 and b==c or b**2==a**2+c**2 and a==c or c**2==a**2+b**2 and a==b:
  print('Tam giác vuông cân')
