# score=[]
# sum=0
# ww=0
# std_count = int(input('학생 수 입력 : '))
# for i in range(1,std_count+1) :
#     scores= int(input('학생{0} 점수 입력 : '.format(i)))
#     score.append(scores)
#     sum += scores
#     if scores >=80:
#         ww+=1
# avg=sum/std_count
# score.sort(reverse=True)
# print('총점 : {0}'.format(sum))
# print('평균 : {0:.2f}'.format(avg))
# print('80점 이상 : {0}명'.format(ww))
# print('점수 내림차순 정렬 : ',*score)
import random
word=['개과천선','구사일생','군계일학','무용지물','동고동락','유비무환','입신양명','괄목상대','막역지우','고장난명']
sen=['잘못을 고치고 옳은 길에 들어섬','죽일 고비를 여러 번 겪으며 살아나다','평범한 사람 가운데 뛰어난 사람','아무짝에나 쓸모 없는 것','고통과 즐거움을 함께 한다'
       ,'미리 준비해두면 근심 걱정이 없다','사회적으로 인정받고 출세하여 이름을 세상에 드날림','다른 사람의 학식이나 업적이 크게 진보한 것을 말함',
       '생사를 같이 할 수 있는 친밀한 벗','상대 없이 혼자서는 어떤일을 이룰 수 없다']
print('사자성어 맞추기 게임을 시작합니다 \n----------------------------------')
que=random.randint(1,9)
while True :
    print("{0}".format(sen[que]))
    answer = input("이말의 사자성어는? : ")
    if(answer == word[]):
        print("\n맞습니다..게임을 종료합니다.")
        break
    else:
        print("\n틀렸습니다...다시 도전 !\n")