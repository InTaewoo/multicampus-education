# 파일 읽어오기
# readline() : 1개의 행씩 읽어오기, 행 끝에 '\n' 포함
# readlines() : 모든 행을 전부 읽어 라인 단위별로 잘라서 리스트를 생성
# ['...\n','....\n','...]
#read() : 내용 전체를 한 문자열로 반환 ''

# print('-----첫번째 행 읽어오기-------')
# f = open('test.txt','r')
# line = f.readline()
# print(line)
# f.close()

print('-------여러 줄 읽기--------')
f = open('test.txt','r')
line = f.readline()
print(line,end='')
line = f.readline()
print(line)
f.close()
# 출력 : 안녕하세요. 홍길동입니다.

#       지금 파이썬을 공부하는 중이에요

print('-------파일 전체 읽기--------')

f = open('test.txt','r',encoding='utf-8')
while True :
    line=f.readline()
    if line =='':
        break
    print(line,end='')
f.close()
