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