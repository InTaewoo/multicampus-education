#정수 3개를 입력받아서 제일 큰 수를 출력
a=int(input('정수1 입력 : '))
b=int(input('정수2 입력 : '))
c=int(input('정수3 입력 : '))
if (a > b and a > c):
    max = a
elif(b > a and b > c):
    max = b
else :
    max= c
print('제일 큰 수 : {0}'.format(max))


#컴퓨터와 게임하는 경우
from random import randint
computer= randint(1,100) #1에서 100까지중 난수1개 생성
mynum= randint(1,100)
print('com : {0} vs my : {1}'.format(computer,mynum))
if(mynum>computer) :
    print('성공')
else :
    print('실패')
    
#도형을 선택해서 면적 구하기
#도형 입력 1: 사각형 2:삼각형 3:원
shape= input('도형을 입력하시오(1 : 사각형, 2 : 삼각형, 3 : 원) : ')
if shape == '1' :
    a=int(input('가로입력 :'))
    b=int(input('세로입력 :'))
    c = a*b
    print('사각형의 면적 : {0}'.format(c))
elif shape=='2' :
    a=int(input('밑변입력 :'))
    b=int(input('높이입력 :'))
    c=(a*b)/2
    print('삼각형의 면적 : {0}'.format(c))
else :
    a = int(input('반지름 입력 :'))
    b = 3.14 * a * a
    print('원의 면적 : {0}'.format(b))

