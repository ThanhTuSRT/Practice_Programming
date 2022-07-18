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
print('Nếu bạn trúng, bạn sẽ được {:,} VND.Nếu thua bạn sẽ bị mất số tiền đã đặt cược.'.format(cuoc*80))

quay=int(input("Nhập số 0 để bắt đầu quay: "))
while quay != 0:
    quay=int(input('Vui lòng nhập số 0 để bắt đầu quay: '))
if quay == 0:
    xoso = random.randint(0,99)
    print()
    print('Số may mắn là: ',xoso)
    
    if so == xoso:
        von1=von+cuoc*80
        print('Xin chúc mừng, bạn đã được cộng {:,} VND vào vốn'.format(cuoc*80))
        print('Số tiền hiện tại của bạn là {:,} VND'.format(von1))
    else:
        von1=von-cuoc
        print('Rất tiếc, bạn đã bị trừ {:,} VND'.format(cuoc))
        print('Số tiền hiện tại của bạn là {:,} VND'.format(von1))

print()        
print('Bạn có muốn tiếp tục không?')
print('1.Có')
print('2.Không')
choose=int(input("Chọn: "))
while choose != 1 and choose != 2:
    choose = int(input("Lỗi, vui lòng nhập lại: "))
if choose == 1 and von1 == 0:
    print()
    print('Bạn không đủ tiền')
if choose == 2:
    print()
    print('Cảm ơn bạn đã tham gia')
    print('Tổng số tiền của bạn là {:,} VND'.format(von1))
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
        print('Nếu bạn trúng, bạn sẽ được {:,} VND.Nếu thua bạn sẽ bị mất số tiền đã đặt cược.'.format(cuoc*80))
        
        quay=int(input("Nhập số 0 để bắt đầu quay: "))
        while quay != 0:
            quay=int(input('Vui lòng nhập số 0 để bắt đầu quay: '))
        if quay == 0:
            xoso = random.randint(0,99)
            print()
            print('Số may mắn là: ',xoso)
                        
            if so == xoso:
                von1=von1+cuoc*80
                print('Xin chúc mừng, bạn đã được cộng {:,} VND vào vốn'.format(cuoc*80))
                print('Số tiền hiện tại của bạn là {:,} VND'.format(von1))
            else:
                von1=von1-cuoc
                print('Rất tiếc, bạn đã bị trừ {:,} VND'.format(cuoc))
                print('Số tiền hiện tại của bạn là {:,} VND'.format(von1))
                     
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
                  print('Tổng số tiền của bạn là {:,} VND'.format(von1))
                  break          