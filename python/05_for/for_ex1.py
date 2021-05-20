
num1=int(input('숫자1을 입력하시오 : '))
num2=int(input('숫자2을 입력하시오 : '))
sum=0
for i in range(num1,num2+1):
    sum+=i
print('{0}과 {1}사이의 합은 : {2}'.format(num1,num2,sum))

dan=int(input('단 수 입력 :'))
for i in range(1,10):
    print('{0} * {1} = {2}'.format(dan,i,dan*i) )

num=int(input('시작 숫자를 입력하시오 : '))
for i in range(num,0,-1):
    print(i,end=' ')
print('발사')

