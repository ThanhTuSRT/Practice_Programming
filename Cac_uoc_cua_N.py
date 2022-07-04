n=int(input("Nhập số N: "))
print()
print('Các ước của N là',end='  ')
for i in range(1,n+1):
    if n % i == 0:
        print(i,end='  ')