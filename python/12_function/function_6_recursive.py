# 팩토리얼 계산 factorial()
# n! = n*(n-1)*(n-2)...

def factorial(n):
    a=n
    for i in range(a-1,0,-1):
        a*=i
    return a
print(factorial(7)

#재귀함수
def factorial(n):
    if n == 1:
        return 1
    return n* factorial(n-1)

