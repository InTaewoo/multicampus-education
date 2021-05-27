# read() : 파일전체를 읽어서 문자열로 반환

f = open('test2.txt','r',encoding='utf-8')
data = f.read()
print(data)
print(len(data))

for i in data:
    print(i)