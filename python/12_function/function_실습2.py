#1
def print_coin():
    print('비트코인')
#2
print_coin()

# #3
# for i in range(100):
#     print_coin()
#
# #4
# def print_coin() :
#     for i in range(100):
#         print('비트코인')
#     print()
# print_coin()

#5 함수를 먼저 정의 해준후 hello()를 써야함
def hello():
    print('hi')
hello()

#6
def message():
    print('A')
    print('B')

message()
print('C')
message()

print('-----')
#7
print('A')

def message():
    print('B')
print('A')
print('C')
message()

print('---')
#8 오류 message1()이게없음
print('A')
def messages1():
    print('B')

print('C')
def messages2():
    print('D')

# message1()
print('E')
messages2()
print('----')

#9
def message1():
    print('A')

def message2():
    print('B')
    message1()
print('----')
message2()
print('----')

#10
def message1():
    print('A')

def message2():
    print('B')

def message3():
    for i in range(3):
        message2()
        print('C')
    message1()

print(message3())

11
def mul ():
  a=int(input('숫자1 : '))
  b=int(input('숫자2 : '))
  return a*b

print(mul())

12
def Upper():
    word=input('소문자 입력 : ')
    return word.upper()
print(Upper())

#13
def pickup_end(x):
    list=[]
    for i in x:
        if i % 2 == 0:
            list.append(i)
    return list
x=[1,2,3,4,5,6,1,5,6,20,100]
print(pickup_end(x))

def pickup_end(*args):
    list=[]
    for i in args:
        if i % 2 ==0:
            list.append(i)
    return list
print(pickup_end(1,2,3,4,5,9,6,7,10,20,100,1000))