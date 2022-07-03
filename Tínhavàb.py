n=int(input('Nhập a: '))
m=int(input('Nhập b: '))
def USCLN_2(n, m):
    r = n % m
    while r != 0:
        n = m
        m = r
        r = n % m
    return m

a = int(abs(n+m))
sum = 0
for i in range(1, a+1):
    if (a % i == 0):
       sum += i


print('Tổng hai số là: ', n + m)
print('Hiệu hai số là: ', n - m)
print('Tích hai số là: ', n * m)
print('Thương hai số là: ', n // m)
print('Ước chung lớn nhất của a và b là: ', USCLN_2(n, m))
print('Tổng các ước của ',n + m,' là ', sum)