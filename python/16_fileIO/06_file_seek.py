# 파일 내에서 검색
# seek(offset,whence) 함수

print('------파일 내에서 검색 seek()-------')
f = open('test2.txt','r',encoding='utf-8')
# f.seek(0,0) # 시작위치 0행, 0열
# f.seek(1,0) # 시작위치 0행, 0열
f.seek(16,0) # 시작위치 1행, 0열

#한글 utf-8 3바이트씩, utf-16:2바이트씩
lines=f.readlines()
print(lines)
f.close()

