# 파일에 쓰기 : 파일을 쓰기 모드(w)로 열고 ,
# 파일객체의 write() 함수를 이용하여 파일에 출력

# data='hello'
# f = open('file2.txt','w') # 파일 객체f
# f.write(data)
# f.close()

data='안녕하세요'
f = open('file2.txt','w',encoding='utf-8') # 파일 객체f
f.write(data)
f.close()
# 한글이 깨져 보임

#utf-8 형식으로 저장 : 한글이 깨지지 않음