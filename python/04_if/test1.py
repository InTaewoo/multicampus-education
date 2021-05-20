
word = input('16진수 한 글자 입력 : ')
if word == 'A' :
    print('10진수 :',int(word,16))
elif word == 'B' :
    print('10진수 :',int(word,16))
elif word == 'C' :
    print('10진수 :',int(word,16))
elif word == 'D' :
    print('10진수 :',int(word,16))
elif word == 'E':
    print('10진수 :', int(word,16))
elif word == 'F' :
    print('10진수 :',int(word,16))
else :
    print('16진수가 아닙니다')

money = int(input('교환할 돈은 얼마? : '))
a= money//50000
b=(money%50000)//10000
c=(money%10000)//5000
d=(money%5000)//1000
e=(money%1000)//500
f=(money%500)//100
g=(money%100)//50
h=(money%50)//10
i=(money%10)
print('50000원:{0}장, 10000원:{1}장 5000원{2}장,1000원:{3}장,\n 500원:{4}개, 100원:{5}개,50원:{6}개,10원:{7}개,바꾸지못한돈:{8}'
      .format(a,b,c,d,e,f,g,h,i))

from random import randint
a=randint(1,6)
b=randint(1,6)
if b > a :
    print('b가 이겼다')
elif b==a :
    print('비긴다')
else :
    print('b가 진다')
