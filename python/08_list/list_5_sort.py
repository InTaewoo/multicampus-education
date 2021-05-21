# #리스트의 요소를 정렬 : sort(), reverse() / sorted()
# a=[3,6,0,-4,1]
# b=[40,30,20,50]
# print(a)
# #a.sort(reverse=True) #내림차순
# a.reverse()
# print(a)
#
# #reverse() 메소드를 사용하지않고 리스트를 역순으로 생성하여 출력하기
# b=[]
# for i in range(len(a)) :
#     b.append(a.pop())
# print(b)
#
# #sorted() 함수
# a=[3,6,0,-4,1]
# c = sorted(a)
# print(a)
# print(c)

string =['GRAPE','Apple','aPPle','banana','melon','apple']
string.sort(key=str.lower) #대,소문자별로 정렬
string.sort()
print(string)

#max(),min()
a=[3,6,0,-4,1]
print(max(a))
print(min(a))
print(max(string))
print(min(string))