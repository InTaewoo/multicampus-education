#1
# list=[]
# for i in range(3):
#     name = input('회원 입력 : ')
#     list.append(name)
# print('회원 명단 : {0}'.format(list))

#2
# list=[]
# total=0
# eight=0
# std_count=int(input('학생 수 입력 : '))
# for i in range(1,std_count+1):
#     scores=int(input('학생'+str(i)+'점수 입력 : '))
#     total+=scores
#     list.append(scores)
#     if scores >= 80:
#         eight+=1
#     else :
#         pass
# print('총점 : {0}'.format(total))
# print('평균 : {0:.2f}'.format(total/std_count))
# print('80점 이상 학생 : {0}명'.format(eight))
#3
# list=[]
# while True :
#     items=input('상품 등록 (엔터키 누르면 종료) : ')
#     if items=='':
#         break
#     list.append(items)
# print('등록된 상품 : {0}'.format(list))

4
list=[]
total=0
eight=0
std_count=int(input('학생 수 입력 : '))
for i in range(1,std_count+1):
    scores=int(input('학생 '+str(i)+'점수 입력 : '))
    total+=scores
    list.append(scores)
    if scores >= 80:
        eight+=1
    else :
        pass
list.sort(reverse=True)
print('총점 : {0}'.format(total))
print('평균 : {0:.2f}'.format(total/std_count))
print('80점 이상 학생 : {0}명'.format(eight))
# print('점수 내림차순 정렬 : {0}'.format(list))

#5
word=['개과천선','구사일생','군계일학','무용지물','동고동락','유비무환','입신양명','괄목상대','막역지우','고장난명']
sen=['잘못을 고치고 옳은 길에 들어섬','죽일 고비를 여러 번 겪으며 살아나다','평범한 사람 가운데 뛰어난 사람','아무짝에나 쓸모 없는 것','고통과 즐거움을 함께 한다'
       ,'미리 준비해두면 근심 걱정이 없다','사회적으로 인정받고 출세하여 이름을 세상에 드날림','다른 사람의 학식이나 업적이 크게 진보한 것을 말함',
       '생사를 같이 할 수 있는 친밀한 벗','상대 없이 혼자서는 어떤일을 이룰 수 없다']
print('사자성어 맞추기 게임을 시작합니다\n--------------------------')
import random
ques=random.randint(1,10)
while True :
    print('{0}'.format(sen[ques]))
    ans=input('이말의 사자성어는? : ')
    if (ans == word[ques]):
        print('맞습니다..게임을 종료합니다.')
        break
    else :
        print('틀렸습니다...다시 도전 !')
