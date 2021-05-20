#키보드로 입력받은 정수가 짝수인지 홀수인지?
'''
num=int(input('정수는 : '))
if num % 2 ==0 :
    print('짝수')
else :
    print('홀수')
if num % 2 ==0 :
    print('짝수')
else :
    pass #아무것도 수행하지 않을때

id = input('아이디 입력 : ')
password = int(input('비밀번호 입력 : '))
if (id == 'flower' and password == 1234):
    print('로그인 성공!')
else :
    print('로그인 실패!')
'''

number = int(input('정수입력 : '))
if(number>0):
    print('양수')
else :
    if(number<0):
        print('음수')
    else:
        print('0')

if(number>0):
    print('양수')
elif(number<0):
    print('음수')
else :
    print('0')

#1~10까지의 정수 합계 계산
a=1
a+=1