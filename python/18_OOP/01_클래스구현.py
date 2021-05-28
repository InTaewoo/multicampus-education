# 클래스 선언
# class 클래스이름 [(슈퍼클래스명)]:

# # 빈 클래스 정의
# class Car:
#     pass
#
# car1 = Car()
# print(car1)


# class Car:
#     #메소드 정의
#     def show(self):
#         print('시험중입니다')
#
#
# car1 = Car()
# car2 = Car()
# car3 = Car()
#
# print('------')
# car1.show() # 메소드 호출
# car2.show()
# car3.show()
#
# # 특정 클래스의 인스턴스인지 확인 : isinstance(인스턴스명, 클래스명)
#
# print(isinstance(car1, Car))
# print(isinstance(car1, int))
#
# x = 3
# print(isinstance(x,int))
#
# y=list([1,2,3,4])
# print(isinstance(y,list))
#
# z= 'Hi, 반가워여'
# print(type(z))
#
# a=True
# print(type(a))
#
# #파이썬에서 기본 제공하고 있는 int, float, bool, str, list, dict, set, tuple --> class
#
# print(isinstance(a,int))
#
# b = (1,2,3)
# print(type(b))
# print(isinstance(b,list))

# instance & object
# 같은 것을 가리키고 있음
# instance : 클래스와 연관지어 말할때
# 예, car1은 Car 클래스의 인스턴이다
# object : 단독으로 부를 때

###
#필드 추가 : 메소드 내에서 사용
# class Car:
#     def show(self):
#         print('시험중입니다')
#
#     # def drive(self):
#     #     self.speed  #speed 필드
#     #     print('{0}로 주행중입니다.'.format(self.speed))
#
#     def drive(self,speed):
#         self.speed = speed #speed 필드
#         print('{0}로 주행중입니다.'.format(self.speed))
#
#
# #메인 : 인스턴스를 생성하고 이용
# car1 = Car()
# car1.drive(70)
# print(car1.speed)
# car1.speed = 100
# car1.drive(50)
#
# #인스턴스.필드
# car1.color='red'
# print(car1.color)

class Car:
    speed = 0
    color = ''


    def show(self):
        print('시험중입니다')

    def drive(self):
        print('{0}으로 주행중입니다'.format(self.speed))

# mycar = Car()
# print(mycar.speed)
# mycar.drive()
# mycar.speed=60
# mycar.drive()

# 생성자(consrutor) : 인스턴스를 생성해주는 함수

# 기본 생성자
# class Car:
#     def__init__(self):
#     self.color = 'white'
#     self.speed = 0
#
# mycar = Car()
# print(mycar.color)

class Car:
    def__init__(self,speed=0, color='white'):
        se