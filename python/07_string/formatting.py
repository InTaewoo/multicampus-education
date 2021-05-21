#formatting : %d %f %s
#%3d : 3자리 정수 %5.2f 전체5자리수중 소수점 두자리까지
# alphas=20;digit=30
# height=179.33
# string='python'
# print('문자 : %d개' % alphas)
# print('문자 :',format(alphas,'d'),'개')
# print('문자 : {0}개, 숫자 : {1}개'.format(alphas,digit))
# print('문자 : {alp}개, 숫자 : {dig}개'.format(alp=alphas,dig=digit))
# print('키는 {0:5.1f}'.format(height))
# print('{0:<10}'.format(string)) #왼쪽 정렬
# print('{0:>10}'.format(string))#오른쪽 정렬
# print('{0:-^10}'.format(string))#가운대 정렬
# print(string.ljust(10))
# print(string.rjust(10))
# print(string.center(10))

#날짜, 시간 출력 포맷
from datetime import date,datetime,timedelta
today=date.today()
print(today.year)
print(today.month)
print(today.day)
#t시간
cur_time = datetime.now()
print(cur_time)
print(cur_time.hour)
print(cur_time.minute)
print(cur_time.second)
print(cur_time.microsecond)

print(today + timedelta(days=-1)) #어제날짜
print(today + timedelta(days=7)) #1주일 뒤
print(cur_time +timedelta(days=-1,hours=2))

print(today.strftime('%Y-%m-%d %H:%M:%S'))