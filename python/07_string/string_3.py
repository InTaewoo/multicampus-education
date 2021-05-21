crwaling='Data crawling is fun'
# print(crwaling.find('i'))
# print(crwaling.rfind('i'))
# print(crwaling.find('i',1,9))
# print('-'*12)
# print(crwaling.index('i'))
# print(crwaling.rindex('i'))
# print(crwaling.rindex('i',1,9))#오류

#split : 지정된 문자로 문자열을 분할함, 리스트 형식으로 분할
token = crwaling.split()
print(token)

names='lee,kim,choi,kang'
nameL=(names.split(','))
for n in nameL :
    print(n,end=' ')

for i in range(len(nameL)):
    print(nameL[i])

#문자열 요소 하나씩 출력
for c in crwaling:
    print(c)
