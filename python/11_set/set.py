# # set
#
# s1 = set()
# print(type(s1))
# s1={3,5,7,1,3,4}
# print(s1)
#
# #s2={[10,20,40]} # 리스트는 불가
# s2={(10,20,40)} #튜플은 가능
# print(s2)
# # 인덱스 사용 불가
# # s1[0]
#
# #데이터추가 .add
# s2.add(90)
# print(s2)
#
# s1.add(-9)
# print(s1)
#
# #데이터 삭제.remove
# s1.remove(-9)
# print(s1)
# #s1.remove(8) # 값이 에러발생
# print(s1)
# s1.discard(7)
# print(s1)
# s1.discard(4)
# print(s1)
#
# s1.clear()
# print(s1)

#집합 연산 : union, intersection, difference
s1 = {3,4,1,6}
s2 = {2,4,5,8,3}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))
print('-'*20)
print(s1 | s2)
print(s1 & s2)
print(s1-s2)

a={x for x in 'abracadabra' if x not in 'abc'}
print(a)

