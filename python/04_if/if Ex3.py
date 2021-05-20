#컴퓨터와 게임하는 경우
from random import randint
computer= randint(1,100) #1에서 100까지중 난수1개 생성
mynum= randint(1,100)
print('com : {0} vs my : {1}'.format(computer,mynum))
if(mynum>computer) :
    print('성공')
else :
    print('실패')