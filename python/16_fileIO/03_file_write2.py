# 파일에 쓰기

# 여러 줄의 데이터를 쓰기
# f = open('file3.txt','w',encoding='utf-8')
#
# for i in range(1,11):
#     data='%d행' % i
#     f.write(data)
# f.close()

# 한줄 단위로 출력
# f = open('file4.txt','w',encoding='utf-8')
#
# for i in range(1,11):
#     data='%d행\n' % i
#     f.write(data)
# f.close()

# , 넣어서 csv파일 형식으로 출력
# f = open('file4.txt','w',encoding='utf-8')
#
# for i in range(1,11):
#     data='%d행,' % i
#     f.write(data)
# f.close()

f = open('file4.txt','w',encoding='utf-8')

for i in range(1,11):
    if i == 10 :
        data='%d행,' % i
    else :
        data='%d행,'% i
    f.write(data)
f.close()