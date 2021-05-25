# 함수내에 사용되는 변수 : local variable(지역변수)

# def show():
#     a = 'Hello' #지역변수
#     print(a)
#
# def show1(a):
#     a = a + 'hello'
#     print(a)
#
# def show2(a):
#     a = a+'H'
#     print(a)
#
# #전역변수를 함수 내부에서 수정(변경)
# def show3(): #전역변수 a를 변경하고싶다
#     global a
#     a= a+'H'
#     print(a)
# a='Hi' #전역변수
#
# # show()
# # print(a)
# # show1(a)
# # show2(a)
# show3()

#실습문제
def sub(x,y):
    global a
    a = 7  #지역변수
    x, y=y, x #swap
    b = 3
    print(a,b,x,y)
    print(id(a))
    print(id(x))

a,b,x,y=1,2,3,4 #전역변수
print('전역변수')
print(id(a))
print(id(x))
sub(x,y)
print(a,b,x,y)

def showlist(mylist):
    mylist[0]=100
    print(mylist)
    print('in function ID :',id(mylist))

mylist=[1,2,3,4]
showlist(mylist)
print(mylist)

# 딕셔너리 list를 dictionary로 변환
def getProduct(prdList):
    name = prdList['name']
    price = prdList['price']
    return {'name' : name, 'price' : price}

productL=[{'name':'notebook','price':'12000000','Maker':'삼성'},
          {'name':'smartphone','price':'12000000','Maker':'삼성'},
          {'name':'냉장고','price':'12000000','Maker':'Lg'},
          {'name':'에어콘','price':'12000000','Maker':'삼성'},
        ]
for product in productL:
    prdInfo=getProduct(product)
    print(prdInfo)