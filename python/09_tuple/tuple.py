#집합적 자료형 : tuple
# 삭제, 변경, 추가 작업불가

#리스트 생성 : list() or []
#tuple생성 : tuple() or ()
# t1=tuple()
# t2=()
#
# t1=(1,2,3)
# print(t1)
# print(type(t1))
# t2=1,3,4
# print(t2)
# t3=t1,(5,6,7)
# print(t3)
# t4=[1,4],[5,6]
# print(t4)
# t5=tuple([1,4]) #list->tuple
# print(t5)
#
# #튜플의 요소 다루기
# #요소 변경 불가
# # print(t1[2])
# # t1[2]=10
#
# #요소 추가 및 삭제 불가
# # t1.append(-9)
# # print(t1)
# # del(t1[2])
# # list1=[1,2,3]
# # del(list[1])
# # print(list1)
#
# # tuple.index(), .count()
# tt = 'a','b','c','d','a','e'
# print(tt.index('e'))
# c=tt.count('b')
# print(c)
# #slicing
# t=(tt[:])
# print(t)
# t=tt[1:5]
# print(t)
#
# # +, * 연산
# print(t1 + t2)
# print(tt*2)

# 2차원 tuple 연습문제
tt = ((1,2,3),(4,5,6),(7,8,9))
print(tt[1][2])

for i in tt :
    for j in i :
        print(j,end=' ')
    print()

# tuple
myTuple = (10,20,30)
myTuple = (10,20,30,40)
l1=[]
print(dir(l1))
#list 객채의 메소드
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__',
 '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
 '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
 '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy',
 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

