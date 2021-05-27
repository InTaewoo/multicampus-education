# read() : 파일전체를 읽어서 문자열로 반환

value=input('검색 값 입력 : ')
f = open('test2.txt','r',encoding='utf-8')
data = f.read()
if value in data:
    print('있다',value)
else :
    print('없다')

f.close()