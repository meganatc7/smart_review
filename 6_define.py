# 덧셈
def sum_number(num1,num2):
    result = num1 + num2
    return result

print(sum_number(10,12))

# 뺄셈
def minus_number(num3,num4):
    return num3 - num4

print(minus_number(10,9))

# 연산
def cal(n1,n2,o):
    """덧셈 뺄셈 입력 받아 계산하는 함수"""
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2

num1 = int(input('첫 번째 정수 입력 >> '))
num2 = int(input('두 번째 정수 입력 >> '))
op = input("연산자 입력(+,-) >> ")
result = cal(num1, num2, op)
print('결과 : {}'.format(result))

# 약수
def divisor(num):
    for i in range(1, num+1):
        if num % i == 0:
            print(i, end=' ')

divisor(32)

def getDivisors(n1,n2):
    for i in range(n1,n2+1):
        print(f'{i}의 약수 : ', end=' ')
        for j in range(1,i+1):
            if i%j == 0:
                print(j, end=' ')
        print()
num1 = int(input('\nstartValue = '))
num2 = int(input('endValue = '))
getDivisors(num1, num2)

# 재귀함수 : 함수 안에 함수가 무한반복으로
def getDivisors1(n1,n2):
    for i in range(n1,n2+1):
        divisor(i)
        print()

getDivisors1(10,12)

# 가변 매개변수를 가진 함수
def sum_all(*args): #arguments
    sum = 0
    for i in args:
        sum += i
    return sum

a = sum_all(1,2,3,4,5)
print(a)