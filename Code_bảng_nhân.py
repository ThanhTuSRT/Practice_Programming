n=int(input("Nhập số N: "))
print()
if n > 1 and n < 10:
   print('Bảng nhân', n)
   print()
if n > 1 and n < 10:
   for i in range(1,10):
     print(n,' × ', i,' = ', n*i)

if n <= 1 or n >= 10:
    print('Vui lòng nhập số N từ 2 đến 9!')
    print()
    n=int(input("Nhập số lại số N: "))
    print()
while n <= 1 or n >= 10:
    print('Vui lòng nhập số N từ 2 đến 9!')
    print()
    n=int(input("Nhập số lại số N: "))
    print()
    if n > 1 and n < 10:
       print('Bảng nhân', n)
       print()
    if n > 1 and n < 10:
        for i in range(1,10):
            print(n,' × ', i,' = ', n*i)
