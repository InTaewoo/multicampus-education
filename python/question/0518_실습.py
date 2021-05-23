money=int(input('교환할 돈은 얼마?'))
b=money//50000
c=(money//50000)%10000
d=(money//10000)%5000
e=(money//5000)%1000
f=(money//1000)%500
g=(money//500)%100
h=(money//100)%50
i=(money//50)%10
j=(money//10)
print('50000원 {0}장, 10000원 {1}장, 5000원 {2}장, 1000원{3}장 \n500원{4}개,100원{5}개,'
      '50원{6}개, 10원{7}개, 바꾸지못한 돈은 : {8}'.format(b,c,d,e,f,g,h,i,j))

import random
a=random.randint(1,6)
b=random.randint(1,6)
print('A의 주사위는 {0} 입니다.'.format(a))
print('A의 주사위는 {0} 입니다.'.format(b))
if a > b :
      print('B가 졌다')
elif a==b :
      print('비겼다')
else :
      print('B가 이겼다'

