n=int(input("Nhập vào số N lớn hơn 1: "))
while n <= 1:
    print('Lỗi, vui lòng nhập lại số N lớn hơn 1')
    print()
    n=int(input("Nhập vào số N lớn hơn 1: "))

flag = True

if n < 2:
    flag = False
elif n == 2:
    flag = True
elif n % 2 == 0:
    flag = False
else:
    for i in range(3, n, 2):
        if n % i == 0:
            flag = False
 

if flag == True:
    print()
    print(n, "là số nguyên tố (không phải là hợp số).")
else:
    print()
    print(n, "là hợp số (không phải là số nguyên tố).")