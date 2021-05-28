# 예외 발생 상황

# ZeroDivisionError: division by zero
# print(10/0)

#print('age=' + 23)

#NameError: name 'x' is not defined
#print(x)

#ValueError: incomplete format
# a=100
# print('%d%'%a)

#SyntaxError: invalid syntax
# if x > 10
#     print('kim')

#IndexError: list index out of range
# a=[1,2,3]
# print(a[3])

#unboundLocalError
# def add():
#     a += 1
# ModuleNotFoundError: No module named 'modd'
#import modd

#FileNotFoundError: [Errno 2] No such file or directory: 'readfile.txt'
# f = open('readfile.txt','r')
# data=f.read()

#
# try :
#     print(10/0)
# except :
#     print('오류가 발생')
# finally :
#     print('나누기')
#
# 여러 개의 예외처리 : 함께 처리 가능
# try:
#     print('age='+23)
#     print(10/0)
# except (ZeroDivisionError,TypeError)as e:
#     print(e)
#

# try :
#     num = int(input('input number : '))
# except ValueError :
#     print('정수가 아닙니다')
# else :
#     print(num) #TRUE면 출력
# finally:
#     print('정수만 입력하세요')

try :
    f = open('testex.txt','r')
except FileNotFoundError:
    pass
else :
    data = f.read()
    print(data)
    f.close()
finally:
    print('종료')