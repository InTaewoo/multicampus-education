yang=0
um=0
young=0
for i in range(1,11):
    num=int(input('숫자 {0}입력 : '.format(i)))
    if num > 0 :
        yang+=1
    elif num < 0 :
        um+=1
    else :
        young+=1
print('-----------')
print('양의 개수 : {0}'.format(yang))
print('음의 개수 : {0}'.format(um))
print('0의 개수 : {0}'.format(young))