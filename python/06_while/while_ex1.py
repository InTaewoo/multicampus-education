#1~100까지의 정수중 3의배수
'''
n=1
sum=0
while n <= 100:
    if n%3 == 0:
        sum+=n
    n+=1
print('1부터 100까지의 합은 {0}'.format(sum))
'''
n=0
sum=0
while n <= 100:
    sum += n
    n+=3
print('1부터 100까지의 합은 {0}'.format(sum))