'''
#1-1 for i in range(5,0,-1):
    print('☆'*i)

for i in range(1,10):
    if i % 2 == 1 :
        print('☆'* i)
#1-2 while True:
    num=int(input('숫자 입력 : '))
    if num == 7 :
        break
    else :
        int(input('다시 입력 :'))
print('{0}입력! 종료'.format(num))

#3
money=10000
charge=2000
song=0
while True:
    if money < 2000:
        break
    song += 1
    money=money-charge
    print('노래 {0}곡 불렀습니다.'.format(song))
    print('현재 {0}원 남았습니다.'.format(money))
print('잔액이 없습니다. 종료합니다.')
'''

