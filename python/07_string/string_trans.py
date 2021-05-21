# #replace()
# text='Java Programming'
# text2=text.replace('Java','Python')
# print(text2)
#
# #대문자/소문자
# #upper()대문자 lower()소문자 caplitalize()전체중 맨앞만 대문자 title()매 문장 앞글자 대문자, swapcase() 대->소 소->대
# text='Java Programming is Fun'
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())
# print(text.swapcase())

#공백문자 제거 strip()-전체 공백제거,lstrip()-왼쪽 공백제거, rstrip()-오른쪽 공백제거
text='     Java Programming is Fun   '
print(text.strip())
print(text.lstrip())
print(text.rstrip())
