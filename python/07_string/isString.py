# 문자열의 구성요소 판단
# isalpha() : 문자 여부 (True,False)

text='1234567'
print(text.isdigit())
print(text.isalpha())
print('    '.isspace())

# isdigit() 숫자인지
# issplace() 공백인지
# isalnum()
# islower()
# isupper()

#연습문제. 문장을 입력하여 알파벳,숫자,스페이스, 그외 문자의개수를 출력
alpha=digit=space=etc=0
sentence=input('문장을 입력하시오 : ')
for i in sentence:
    if (i.isalpha()):
        alpha+=1
    elif (i.isdigit()):
        digit+=1
    elif (i.isspace()):
        space+=1
    else :
        etc+=1
print('알파벳은 : {0},숫자는 : {1}, 스페이스는 : {2}, 그외문자는 : {3}'.format(alpha,digit,space,etc))
