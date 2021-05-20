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



