#evaL() : 입력된 문자열에 해당하는 숫자형식으로 변환

num1=eval(input('number1 : '))
num2=eval(input('number2 : '))
print(type(num1))
print(type(num2))
total = num1 + num2
print('합은 {0}'.format(total))

print(eval(input()))
# = : assign
#print(), format(), input(), type(), id()
#escape \n \t \\ \'
#import
#주석문, 문자열
#bin, oct(), int(), str(), float(), eval()



#산술 연산자 : +, =, *, /, //, %, **
#문제 10000초는 몇시간 몇분 몇초인가?
s=10000
m=s//60
M=s//60%60
r=s%60
h=m//60
print('{0}시간 {1}분 {2}초,'.format(h,M,r))
#산술연산자 우선순위 : ()
# 지수**
# 곱셈, 나눗셈, 나머지, 몫
# 덧셈, 뺄셈
#할당 연산자 : =
#대입 연산자 : +=, -=, *=, /=, //=, %=, **=
a=100
a = a + 10 # a += 10
a = a + 10
a = a + 10

sum = 1
sum = sum + 2 # 1+2
sum = sum + 3 # 1+2+3
sum = sum + 4 # 1+2+3+4
sum = sum + 5 # 1+2+3+4+5

b -= 10 #b=b-10
c *= 10 #c=c*10
d /= 10 #d=d/10
e **= 3 #e=e**3
#관계 연산자 : > , < , >=, <=, ==, != : 결과값이 참(True), 거짓(False)

100 > 3 # True
a= 100
b= 1001
a > b
print(a>b)
print(a!=b)
#논리 연산자 : and, or, not
print('#논리연산자')
print(a>b and b==1001) #False
print(a>b or b==1001) #True
print(not(a>b))
#비트 연산자 : 정수를 2진수로 변환한 수 각각의 비트별로 연산
# & (논리곱), | (논리합), ^(xor) ~(부정not), <<(왼쪽시프트) , >>(오른쪽시프트)

print(10 & 3) #1010 & 0011 (2진수곱) -> 0010
print(10 | 3) #1010 | 0011 (2진수합) -> 1011
print(10 ^ 3) #1010 ^ 0011  -> 1001
print(~3) # ~0011 -> 1100 (12)
print(10<<1)
print(10<<2)
print(10<<3)

print(10>>1)
print(10>>2)
print(10>>3)

candy= 5000//120
cash=5000%120
print('사탕의 개수는 : {0} 나머지돈은 : {1}원'.format(candy,cash))
print('잔액 : ', format(1235000, ',.0f')) # , 는 자릿수


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



# 타입변환
#str()함수 : 숫자를 문자열로 변환
#print('나는 현재 나이가'+str(23)+'살입니다.')
#int():정수형식의 문자열을 정수로 변환
'''num=input('숫자를 입력하세요 : ') #키보드로 입력받은 자료를 num변수에 할당
print(type(num))
print(int(num)+100)
print(int('123',8)) #8진수 0o123 2진수 : 001001
print(int('123',16)) #16진수

print(float(num)+100) #문자열을 실수로

#키보드로부터 2개의 숫자를 입력을 받아요, 두수의 합과 평균을 구하시오
a=int(input('숫자를 입력하시오 : '))
b=int(input('숫자를 입력하시오 : '))
sum=a+b
average=sum/2

print('합 : %d , 평균 : %.2f'%(sum,average))
print('두 수의 합은 {0}, 평균은 {1}'.format(sum,average))
'''


score=55
if score >= 60 :
    print("합격이다.")
elif score >= 40 :
    print("불합격 이지만 과락은 아닙니다.")
else :
    print("불합격 이면서 과락입니다.")
