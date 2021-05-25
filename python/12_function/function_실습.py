def order(price,qty):
    amount=price*qty
    total=0
    if amount >= 100000:
        discount=amount*0.1
    elif amount < 50000:
        discount=0
    else :
        discount=amount*0.05
    total=amount-discount
    return amount,discount,total

price=int(input('상품 가격 입력 : '))
qty=int(input('주문 수량 입력 : '))
order=order(price,qty)
print('-'*30)
print('주문액 : {0}'.format(order[0]))
print('할인액 : {0}'.format(order[1]))
print('지불액 : {0}'.format(order[2]))


