# name=[]
# for i in range(3) :
#     a=input('회원 입력 : ')
#     name.append(a)
# print('회원 명단 : {0}'.format(name))
#
score=[]
sum=0
ww=0
std_count = int(input('학생 수 입력 : '))
for i in range(1,std_count+1) :
    scores= int(input('학생{0} 점수 입력 : '.format(i)))
    score.append(scores)
    sum += scores
    if scores >=80:
        ww+=1
avg=sum/std_count
score.sort(reverse=True)
print('총점 : {0}'.format(sum))
print('평균 : {0:.2f}'.format(avg))
print('80점 이상 : {0}명'.format(ww))
print('점수 내림차순 정렬 : ',*score)

# list=[]
# while True :
#     item=input('상품 등록 (엔터키 누르면 종료 ) : ')
#     if item == '' :
#         break
#     list.append(item)
# print('등록된 상품 : {0}'.format(list))

#5

