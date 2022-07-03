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




