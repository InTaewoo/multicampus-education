#continue 문
'''x=0
while x < 10:
    x+=1
    if x % 2 != 0 :
        continue
    print(x)
'''
while True:
    print('반복시작')
    answer=input('종료하려면 x입력 :')
    if answer == 'x':
        break
print('반복 종료')