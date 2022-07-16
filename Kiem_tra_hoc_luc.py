nam=float(input("Nhập điểm TB các môn HKI hoặc HKII hoặc cả năm: "))
if nam >= 8.0 and nam <= 10:
        print('Học lực: Giỏi')
elif nam >= 6.5 and nam < 8.0:
        print('Học lực: Khá')
elif nam >= 5.0 and nam < 6.5:
        print('Học lực: Trung bình')
elif nam >= 3.5 and nam < 5.0:
        print('Học lực: Yếu')
elif nam < 3.5 and nam >= 0:
        print('Học lực: Kém')
else:
        print('Định dạng đầu vào không hợp lệ, tôi chưa thấy ai có điểm như vậy cả:)')
        print('Vui lòng nhập lại!')
        print()
        nam=float(input("Nhập điểm TB các môn HKI hoặc HKII hoặc cả năm: "))
        while nam < 0 or nam > 10:
            print()
            print('Vui lòng nhập lại!')
            nam=float(input("Nhập điểm TB các môn HKI hoặc HKII hoặc cả năm: "))
            if nam >= 8.0 and nam <= 10:
                 print('Học lực: Giỏi')
            elif nam >= 6.5 and nam < 8.0:
                 print('Học lực: Khá')
            elif nam >= 5.0 and nam < 6.5:
                 print('Học lực: Trung bình')
            elif nam >= 3.5 and nam < 5.0:
                 print('Học lực: Yếu')
            elif nam < 3.5 and nam >= 0:
                 print('Học lực: Kém')