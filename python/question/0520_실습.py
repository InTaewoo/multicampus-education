for i in range(5,0,-1):
    print('*'*i)

#2
while True:
    num=int(input('숫자 입력 : '))
    if num == 7 :
        print('{0} 입력 ! 종료'.format(num))
        break
    else :
        num=int(input('숫자 입력 : '))
