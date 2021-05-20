#문자열의 기본 형식과 이해
crawling='Data crawling is fun.'
parsing = 'Data parsing is also fun'

print(type(crawling))
print(type(parsing))
'''
PI = 3.1414
r=10
result = ('반지름 ' + str(PI) +  '인 원의 넓이는'+str(PI*r*r))
print(result)
print('hello ' * 3)
'''
#slicing : 문자의 일부분을 추출
print(crawling[0])
print(crawling[-1])
print(crawling[1:5])
print(crawling[:-1])
print(crawling[-1:])
print(crawling[:])
print(crawling[0:10])
