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


