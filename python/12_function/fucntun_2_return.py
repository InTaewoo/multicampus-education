# 함수의 반환값(return)

# def sum() :
#     a=int(input('숫자 1 :'))
#     b=int(input('숫자 2 :'))
#     #print(a+b)
#     return(a+b)
# #res = sum()
# # print('합은 {0}'.format(res))
# print('합은 {0}'.format(sum))

#삼각형의 넓이 계산 함수 get_triangle_area
#높이와 밑변을 입력
# def get_triangle_area() :
#     a=int(input('높이 : '))
#     b=int(input('밑변 : '))
#     return((a*b)/2)
# print('삼각형의 면적 : {0}'.format(get_triangle_area()))

# def get_triangle_area() :
#     a=int(input('높이 : '))
#     b=int(input('밑변 : '))
#     area=((a*b)/2)
#     return a,b,area
# area=get_triangle_area()
# print('높이 : {0}\n밑변 : {1}\n삼각형의 넓이 : {2}'.format(area[0],area[1],area[2]))

# def order() :
#     a=int(input('상품가격 입력 : '))
#     b=int(input('주문수량 입력 : '))
#     price=a*b
#     return a,b,price
# price=order()
# print('-'*30)
# print('상품가격 : {0}원\n주문수량 : {1}개\n주문액 : {2}원'.format(price[0],price[1],price[2]))

# 리스트 반환값

# def getName():
#     names=[]
#     for i in range(3):
#         name=input('이름 입력 : ')
#         names.append(name)
#     return(names)
# nameL = getName()
# print(type(nameL))
# print(nameL)

#이름과 나이를 받아서 딕셔너리 형태로 반환
# def dic ():
#     dict = {}
#     name=input('이름 : ')
#     age = int(input('나이 : '))
#     dict['이름']=name
#     dict['나이']=age
#     return dict
#
# dict=dic()
# print(dict)
# for key in dict.keys():
#     print(key,':',dict[key])

#반환값이 없는 경우 None 출력
def showHello():
    print('hello')