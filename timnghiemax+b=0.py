print()
print('CHƯƠNG TRÌNH GIẢI PT ax+b=0')
print()
a=int(input("Nhập hệ số a: "))
b=int(input("Nhập hệ số b: "))

if a != 0:
    print('Phương trình',a,'x +',b,'= 0','có nghiệm x =',round(-b/a,1))
if a == 0 and b == 0:
    print('Phương trình có vô số nghiệm')    
if a == 0 and b != 0:
    print('Phương trình có vô số nghiệm')