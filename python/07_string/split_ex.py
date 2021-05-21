# #생일 입력하세요(연/월/일) : 1998/9/20
# birth=input('생일을 입력하세요 : ')
# a=birth.split('/')
# print('당신은'+ a[0]+'년에 태어나셨군요' '\n생일은 '+a[1]+'월 '+ a[2]+'일 이네요'),

#주어진 데이터에서 점수만 추출하여 숫자화하고 총점과 평균을 구하시오.
data='{a1:30},{a2:50},{a3:20},{a4:70},{a5:40}'
sum=0
num=data.split(',')
for i in range(len(num)):
    #print(num[i][4:6])
    sum=sum+int((num[i][4:6]))
print('총점은 {0}이고, 평균은 {1}이다.'.format(sum,sum/len(num)))