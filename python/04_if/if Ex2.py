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