#Cái này code cho vui thôi không có cờ bạc gì đâu nhé =))
import random
print('CHƯƠNG TRÌNH QUAY XỔ SỐ')
ten=input("Họ và tên: ")
print('Xin chào',ten,'!')
print('Chào mừng đến chương trình quay sổ xố')

von=int(input("Nhập số vốn của bạn (VND): "))

so = int(input("Vui lòng nhập số bạn chọn: "))
while so < 0 or so > 99:
    so = int(input("Lỗi, vui lòng nhập số từ 00 đến 99: "))
cuoc = int(input("Vui lòng nhập số tiền cược (VND): "))
while cuoc > von:
    cuoc = int(input("Bạn không đủ tiền cược, vui lòng nhập lại (VND): "))
print()
print('Nếu bạn trúng, bạn sẽ được',cuoc*80,'VND.Nếu thua bạn sẽ bị mất số tiền đã đặt cược.')

quay=int(input("Nhập số 0 để bắt đầu quay: "))
while quay != 0:
    quay=int(input('Vui lòng nhập số 0 để bắt đầu quay: '))
if quay == 0:
    xoso = random.randint(0,99)
    print()
    print('Số may mắn là: ',xoso)
    
    if so == xoso:
        von1=von+cuoc*2
        print('Xin chúc mừng, bạn đã được cộng',cuoc*2,'VND vào vốn')
        print('Số tiền hiện tại của bạn là', von1,'VND')
    else:
        von1=von-cuoc
        print('Rất tiếc, bạn đã bị trừ',cuoc,'VND')
        print('Số tiền hiện tại của bạn là', von1,'VND')

print()        
print('Bạn có muốn tiếp tục không?')
print('1.Có')
print('2.Không')
choose=int(input())
while choose != 1 and choose != 2:
    choose = int(input("Lỗi, vui lòng nhập lại: "))
if choose == 1 and von1 == 0:
    print()
    print('Bạn không đủ tiền')
if choose == 2:
    print()
    print('Cảm ơn bạn đã tham gia')
    print('Tổng số tiền của bạn là',von1,'VND')
if choose == 1 and von1 != 0:
    while True:
        print()
        so = int(input("Vui lòng nhập số bạn chọn: "))
        while so < 0 or so > 99:
            so = int(input("Lỗi, vui lòng nhập số từ 00 đến 99: "))
        cuoc = int(input("Vui lòng nhập số tiền cược (VND): "))
        while cuoc > von1:
            cuoc = int(input("Bạn không đủ tiền cược, vui lòng nhập lại (VND): "))
        print()
        print('Nếu bạn trúng, bạn sẽ được',cuoc*80,'VND.Nếu thua bạn sẽ bị mất số tiền đã đặt cược.')
        
        quay=int(input("Nhập số 0 để bắt đầu quay: "))
        while quay != 0:
            quay=int(input('Vui lòng nhập số 0 để bắt đầu quay: '))
        if quay == 0:
            xoso = random.randint(0,99)
            print()
            print('Số may mắn là: ',xoso)
                        
            if so == xoso:
                von1=von1+cuoc*2
                print('Xin chúc mừng, bạn đã được cộng',cuoc*2,'VND vào vốn')
                print('Số tiền hiện tại của bạn là', von1,'VND')
            else:
                von1=von1-cuoc
                print('Rất tiếc, bạn đã bị trừ',cuoc,'VND')
                print('Số tiền hiện tại của bạn là', von1,'VND')
                     
            print()
            print('Bạn có muốn tiếp tục không?')
            print('1.Có')
            print('2.Không')
            choose=int(input("Chọn: "))
            while choose != 1 and choose !=2:
                choose=int(input("Lỗi, vui lòng nhập lại: "))
            if choose == 1 and von1 == 0:
                  print()
                  print('Bạn không đủ tiền')
                  break	      
            if choose == 2:
                  print()
                  print('Cảm ơn bạn đã tham gia')
                  print('Tổng số tiền của bạn là',von1,'VND')
                  break          