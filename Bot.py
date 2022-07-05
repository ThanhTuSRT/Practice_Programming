name=input("Họ và tên: ")
print()
print('Xin chào',name,'!')
print('Tôi có thể giúp gì cho bạn?')
print('1. Tính điểm')
print('2. Tính a và b')
print('3. Hình tam giác')
print('4. Kiểm tra số nguyên')
print('5. Kiểm tra tam giác')
print('6. Hình chữ nhật')
print('7. In bảng nhân')
print('8. Tính trung bình cộng')
print('9. Nghiệm PT ax+b=0')
print('10. Tìm ước của một số')
print('11. Hình tròn')
chon=int(input("Xin mời chọn: "))

while chon < 1 or chon > 11:
    print()
    print('Lỗi, vui lòng chọn lại!')
    chon=int(input("Xin mời chọn: "))
    print()
if chon == 1:
        print()
        print('TÍNH ĐIỂM TRUNG BÌNH')
        print()
        print('ĐIỂM HỌC KỲ I')
        Toán=float(input("Nhập điểm TB môn Toán: "))
        while Toán > 10 or Toán < 0:
            print('Vui lòng nhập lại điểm TB môn Toán')
            Toán=float(input("Điểm TB môn Toán:"))
            if Toán <= 10 and Toán >= 0:
                break
        Văn=float(input("Nhập điểm TB môn Ngữ Văn: "))
        while Văn > 10 or Văn < 0:
            print('Vui lòng nhập lại điểm TB môn Ngữ văn')
            Văn=float(input("Điểm TB môn Ngữ Văn:"))
            if Văn <= 10 and Văn >= 0:
                break
        TA=float(input("Nhập điểm TB môn Tiếng Anh: "))
        while TA > 10 or TA < 0:
            print('Vui lòng nhập lại điểm TB môn Tiếng Anh')
            TA=float(input("Điểm TB môn Tiếng Anh:"))
            if TA <= 10 and TA >= 0:
                break
        Sử=float(input("Nhập điểm TB môn Lịch sử: "))
        while Sử > 10 or Sử < 0:
            print('Vui lòng nhập lại điểm TB môn Ngữ văn')
            Sử=float(input("Điểm TB môn Lịch sử:"))
            if Sử <= 10 and Sử >= 0:
                break
        Địa=float(input("Nhập điểm TB môn Địa lý: "))
        while Địa > 10 or Địa < 0:
            print('Vui lòng nhập lại điểm TB môn Địa lý')
            Địa=float(input("Điểm TB môn Ngữ Văn:"))
            if Địa <= 10 and Địa >= 0:
                break
        Sinh=float(input("Nhập điểm TB môn Sinh học: "))
        while Sinh > 10 or Sinh < 0:
            print('Vui lòng nhập lại điểm TB môn Sinh học')
            Sinh=float(input("Điểm TB môn Sinh:"))
            if Sinh <= 10 and Sinh >= 0:
                break
        GDCD=float(input("Nhập điểm TB môn GDCD: "))
        while GDCD > 10 or GDCD < 0:
            print('Vui lòng nhập lại điểm TB môn GDCD')
            GDCD=float(input("Điểm TB môn GDCD:"))
            if GDCD <= 10 and GDCD >= 0:
                break
        Tin=float(input("Nhập điểm TB môn Tin học: "))
        while Tin > 10 or Tin < 0:
            print('Vui lòng nhập lại điểm TB môn Tin')
            Tin=float(input("Điểm TB môn Tin:"))
            if Tin <= 10 and Tin >= 0:
                break
        Lý=float(input("Nhập điểm TB môn Vật lý: "))
        while Lý > 10 or Lý < 0:
            print('Vui lòng nhập lại điểm TB môn Vặt lý')
            Lý=float(input("Điểm TB môn Vật lý:"))
            if Lý <= 10 and Lý >= 0:
               break
        CN=float(input("Nhập điểm TB môn Công nghệ: "))
        while CN > 10 or CN < 0:
            print('Vui lòng nhập lại điểm TB môn Công nghệ')
            CN=float(input("Điểm TB môn Công nghệ:"))
            if CN <= 10 and CN >= 0:
                break
        ĐTBHKI = round((Toán + Văn + TA + Sử + Địa + Sinh + GDCD + Tin + Lý + CN)/10,1)
        print()
        print('Điểm TB học kỳ I:',ĐTBHKI)
        if ĐTBHKI >= 8.0:
            print('Học lực HKI: Giỏi')
        if ĐTBHKI >= 6.5 and ĐTBHKI < 8.0:
            print('Học lực HKI: Khá')
        if ĐTBHKI >= 5.0 and ĐTBHKI < 6.5:
            print('Học lực HKI: Trung bình')
        if ĐTBHKI >= 3.5 and ĐTBHKI < 5.0:
            print('Học lực HKI: Yếu')
        if ĐTBHKI < 3.5:
            print('Học lực HKI: Kém')
        print()
        print()
        print('ĐIỂM HỌC KỲ II')
        Toán2=float(input("Nhập điểm TB môn Toán: "))
        while Toán2 > 10 or Toán2 < 0:
            print('Vui lòng nhập lại điểm TB môn Toán')
            Toán2=float(input("Điểm TB môn Toán:"))
            if Toán2 <= 10 and Toán2 >= 0:
                break
        Văn2=float(input("Nhập điểm TB môn Ngữ Văn: "))
        while Văn2 > 10 or Văn2 < 0:
            print('Vui lòng nhập lại điểm TB môn Ngữ văn')
            Văn2=float(input("Điểm TB môn Ngữ Văn:"))
            if Văn2 <= 10 and Văn2 >= 0:
                break
        TA2=float(input("Nhập điểm TB môn Tiếng Anh: "))
        while TA2 > 10 or TA2 < 0:
            print('Vui lòng nhập lại điểm TB môn Tiếng Anh')
            TA2=float(input("Điểm TB môn Tiếng Anh:"))
            if TA2 <= 10 and TA2 >= 0:
                break
        Sử2=float(input("Nhập điểm TB môn Lịch sử: "))
        while Sử2 > 10 or Sử2 < 0:
            print('Vui lòng nhập lại điểm TB môn Ngữ văn')
            Sử2=float(input("Điểm TB môn Lịch sử:"))
            if Sử2 <= 10 and Sử2 >= 0:
                break
        Địa2=float(input("Nhập điểm TB môn Địa lý: "))
        while Địa2 > 10 or Địa2 < 0:
            print('Vui lòng nhập lại điểm TB môn Địa lý')
            Địa2=float(input("Điểm TB môn Địa lý:"))
            if Địa2 <= 10 and Địa2 >= 0:
                break
        Sinh2=float(input("Nhập điểm TB môn Sinh học: "))
        while Sinh2 > 10 or Sinh2 < 0:
            print('Vui lòng nhập lại điểm TB môn Sinh học')
            Sinh2=float(input("Điểm TB môn Sinh:"))
            if Sinh2 <= 10 and Sinh2 >= 0:
                break
        GDCD2=float(input("Nhập điểm TB môn GDCD: "))
        while GDCD2 > 10 or GDCD2 < 0:
            print('Vui lòng nhập lại điểm TB môn GDCD')
            GDCD2=float(input("Điểm TB môn GDCD:"))
            if GDCD2 <= 10 and GDCD2 >= 0:
                break
        Tin2=float(input("Nhập điểm TB môn Tin học: "))
        while Tin2 > 10 or Tin2 < 0:
            print('Vui lòng nhập lại điểm TB môn Tin')
            Tin2=float(input("Điểm TB môn Tin:"))
            if Tin2 <= 10 and Tin2 >= 0:
                break
        Lý2=float(input("Nhập điểm TB môn Vật lý: "))
        while Lý2 > 10 or Lý2 < 0:
            print('Vui lòng nhập lại điểm TB môn Vặt lý')
            Lý2=float(input("Điểm TB môn Vật lý:"))
            if Lý2 <= 10 and Lý2 >= 0:
                break
        CN2=float(input("Nhập điểm TB môn Công nghệ: "))
        while CN2 > 10 or CN2 < 0:
            print('Vui lòng nhập lại điểm TB môn Công nghệ')
            CN2=float(input("Điểm TB môn Công nghệ:"))
            if CN2 <= 10 and CN2 >= 0:
                break
        
        ĐTBHKII = round((Toán2 + Văn2 + TA2 + Sử2 + Địa2 + Sinh2 + GDCD2 + Tin2 + Lý2 + CN2)/10,1)
        nam = round((ĐTBHKI+(ĐTBHKII*2))/3,1)
        print()
        print('Điểm TB học kỳ II:',ĐTBHKII)
        if ĐTBHKII >= 8.0:
            print('Học lực HKII: Giỏi')
        if ĐTBHKII >= 6.5 and ĐTBHKII < 8.0:
            print('Học lực HKII: Khá')
        if ĐTBHKII >= 5.0 and ĐTBHKII < 6.5:
            print('Học lực HKII: Trung bình')
        if ĐTBHKII >= 3.5 and ĐTBHKII < 5.0:
            print('Học lực HKII: Yếu')
        if ĐTBHKII <3.5:
            print('Học lực HKII: Kém')
        print()
        print()
        print('CẢ NĂM')
        print('Điểm TB cả năm học:',nam)
        if nam >= 8.0:
            print('Học lực cả năm: Giỏi')
        if nam >= 6.5 and nam < 8.0:
            print('Học lực cả năm: Khá')
        if nam >= 5.0 and nam < 6.5:
            print('Học lực cả năm: Trung bình')
        if nam >= 3.5 and nam < 5.0:
            print('Học lực cả năm: Yếu')
        if nam < 3.5:
            print('Học lực cả năm: Kém')
            
if chon == 2:
        print()
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
        
if chon == 3:
        print()
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

if chon == 4:
    print()
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

if chon == 5:
    print()
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
    
    if a==b or a==c or b==c:
      print('Tam giác cân')
    if a==b==c:
      print('Tam giác đều')
    if a**a==b**2+c**3 or b**2==a**2+c**2 or c**2==a**2+b**2:
      print('Tam giác vuông')

if chon == 6:
     print()
     n=int(input("Chiều dài hình chữ nhật: "))
     m=int(input("Chiều rộng hình chữ nhật: "))

     print('Chu vi: ', (m+n)*2)
     print('Diện tích: ', n*m)
     
if chon == 7:
    print()
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
        
if chon == 8:
    print()
    print('Bạn cần tính trung bình cộng của mấy số?')
    n=int(input())
    
    while n < 2 or n > 5:
        print('Trình chỉ tính được trong phạm vi từ 2 đến 5')
        print('Vui lòng chọn lại')
        n=int(input())
    if n == 2:
        a=float(input("Nhập số thứ nhất: "))
        b=float(input("Nhập số thứ hai: "))
        ave = (a+b)/2
        print('Trung bình cộng của hai số đó là',ave)
    if n == 3:
        a=float(input("Nhập số thứ nhất: "))
        b=float(input("Nhập số thứ hai: "))
        c=float(input("Nhập số thứ ba: "))
        ave = (a+b+c)/3
        print('Trung bình cộng của ba số đó là',ave)
    if n == 4:
        a=float(input("Nhập số thứ nhất: "))
        b=float(input("Nhập số thứ hai: "))
        c=float(input("Nhập số thứ ba: "))
        d=float(input("Nhập số thứ tư: "))
        ave = (a+b+c+d)/4
        print('Trung bình cộng của bốn số đó là',ave)
    if n == 5:
        a=float(input("Nhập số thứ nhất: "))
        b=float(input("Nhập số thứ hai: "))
        c=float(input("Nhập số thứ ba: "))
        d=float(input("Nhập số thứ tư: "))
        e=float(input("Nhập số thứ năm: ")) 
        ave = (a+b+c+d+e)/5
        print('Trung bình cộng của năm số đó là',ave)
        
if chon == 9:   
    print()
    print('NGHIỆM PT ax+b=0')
    print()
    a=int(input("Nhập hệ số a: "))
    b=int(input("Nhập hệ số b: "))
    
    if a != 0:
        print('Phương trình',a,'x +',b,'= 0','có nghiệm x =',round(-b/a,1))
    if a == 0 and b == 0:
        print('Phương trình có vô số nghiệm')    
    if a == 0 and b != 0:
        print('Phương trình có vô số nghiệm')
        
if chon == 10:
    print()
    n=int(input("Nhập số N: "))
    print()
    print('Các ước của N là',end='  ')
    for i in range(1,n+1):
        if n % i == 0:
            print(i,end='  ')  

if chon == 11: 
    print()   
    n=int(input("Nhập bán kính (cm): "))
    print('Chu vi hình tròn là: ', 2*3.14*n,'cm')
    print('Diện tích hình tròn là: ', 3.14*n*n,'cm²')                