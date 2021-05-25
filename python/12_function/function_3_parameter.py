# 함수의 매개변수(parameter)
# 함수에 전달(입력)되는 값 (함수 정의할때)

# 인수(argumnet) : 함수에 실제로 전달되는 값

# def showInfo(name,age):
#     print('이름은 {0}이고 나이는{1}이에요'.format(name,age))
# showInfo('홍길동',20)
#
# def getArea(width,height):
#     return width * height * 0.5
#
# w=int(input('밑변 : '))
# h=int(input('높이 : '))
# print(getArea(w,h))

#사칙연산을 수행하는 함수들을 정의하여 호출
#add(x,y), sub(x,y) mul(x,y), div(x,y)
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x, y):
    return x*y

def div(x, y):
    return x/y

x=int(input('숫자1 : '))
y=int(input('숫자2 : '))
print('{0} + {1} = {2}'.format(x,y,add(x,y)))
print('{0} - {1} = {2}'.format(x,y,sub(x,y)))
print('{0} * {1} = {2}'.format(x,y,mul(x,y)))
print('{0} / {1} = {2:.2f}'.format(x,y,div(x,y)))


