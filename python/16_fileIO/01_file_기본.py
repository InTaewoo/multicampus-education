#생성된 file.txt파일은 빈 파일
# f=open('file1.txt','w')
# f.close()

# 경로 수정 : 디렉토리가 존재하지 않은 경로
# f=open('c:/python/file1.txt','w')
# f.close()
#f=open('file1.txt','w')
#FileNotFoundError: [Errno 2] No such file or directory: 'c:/python/file1.txt'

#상대경로 표현
f=open('../file.txt','w')
f.close()
#/python study/pythonstudy/16_fileI0/01_file_기본.py" 상위폴더에 저장
