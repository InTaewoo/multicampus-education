# 함수의 매개변수 형식
# 매개변수에 기본값 지정 : default parameter

# def showMessage(message='hi!'):
#     print(message)
#
# def showMessage2(name,message='Hello!'):
#     print(name,message)
#
# #default argumet는 맨 뒤에!
# #def showMessage2(message='Hello!',name):
#     #print(name,message)
#
# def showInfo(name='aniny',age=10,sex='F'):
#     print(name,age,sex)
#
#
# # showMessage('Hello')
# # showMessage('Hi')
# # showMessage('We are happy!')
# # showMessage('We are happy!')
# # showMessage2('Kim')
# # showMessage()
# showInfo('홍길동')
# showInfo('강감찬',40)
# showInfo('변학도',40,'M')
# showInfo()
#
# #함수의 실인수로 리스트로 전달
# def showName(names):
#     for name in names:
#         print(name,end=' ')
# names=['HONG','PARK','CHOI','LEE']
# showName(names)
#
# # 함수의 실인수로 딕셔너리가 전달
# def showInfostd(student):
#     print(student)
#     print('이름 : ', student['name'])
#     print('나이 : ', student['age'])
#     print('연락처 : ', student['phone'])
# info_std={'name':'kim','age':19,'phone':'010-0202-0330'}
# showInfostd(info_std)

# 가변길이 매개변수
# *args : arguments 1개 이상 지정
# *kwargs : keyword arguments key=value
#
# def mysum(*args):
#     total=0
#     for x in args:
#         total+=x
#     return total
#
# def myShowInfo(**kwargs):
#     for key in kwargs.keys():
#         print(key,end=' ')
#     print()
#     for value in kwargs.values():
#         print(value,end=' ')
#     print()
#     for item in kwargs.items():
#         print(item,end=' ')
#
# # print(mysum(1,3,5))
# # print(mysum(1,3,5,4,4,4,))
# # print(mysum(1,3,5,10))
# myShowInfo(id=123, name='kim',add='seoul')
# myShowInfo(id=333, name='lee',add='seoul',phone='111')
#
# def calculator(operator, *args):
#     pass

def studentInfo(name,age,sex):
    student={'name':name,
             'age':age,
             'sex':sex
             }
    return student
studentInfo('lee',30,'f')  #위치 인수
print(studentInfo(name='kim',age=30,sex='f')) #키워드 기반의 인수
print(studentInfo(name='kim',sex='f',age=15))
print(studentInfo(name='kim',sex='f',age=15))

# 위치인수와 키워드인수를 혼용할때는 키워드 인수는 위치인수 뒤쪽으로