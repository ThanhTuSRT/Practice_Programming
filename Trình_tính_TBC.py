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