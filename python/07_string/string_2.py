#string 관련 함수들

#len():문자열의 length
string='Python Programming'
n=len(string)
print(n)

#count() : 문자열에서 찾고자하는 문자(열)의 개수
print(string.count('p'))

#find() : 특정문자열이 존재여부에 따라 위치
print(string.find('ing'))
print(string.find('ong')) #-1은 없다

#index() : find랑 같지만 없으면 오류
print(string.index('ing'))
print(string.index('ong'))


