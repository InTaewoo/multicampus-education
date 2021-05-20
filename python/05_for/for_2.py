'''for i in range(10):
    print(i,end=' ')
print('\n=================')
for i in range(1,10):
    print(i,end=' ')
print('\n=================')
for i in range(1,10,2):
    print(i,end=' ')
print('\n=================')
for i in range(12,1,-1):
    print(i,end=' ')
print('\n================='

#1~10사이의 수를 더하고 더한 결과 출력
total = 0
for n in range(1,11):
    total+=n
print('합은 {0}'.format(total))

total=0
for i in range(101):
    total+=i
print('1~100의 합은 :{0}'.format(total))

sum=0
for i in range(3,21,3):
    sum+=i
    print(i,end=' ')
print('3의 배수의 합은 : {0}'.format(sum))
'''
total=0
for i in range(1,21):
    if (i % 3 == 0) :
        total+=i
        print(i,end=' ')
print()
print('3의 배수의 합은 : {0}'.format(total))