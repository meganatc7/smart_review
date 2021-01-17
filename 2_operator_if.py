# 연산자
num1, num2 = 10, 7
print(num1/num2) #나누기
print(num1%num2) #나머지
print(num1//num2) #몫

str1 = '안녕'
str2 = '하세요'
print(str1 + str2)

num1 = 10
str1 = '7'
print(num1+int(str1))

# 키보드로 값 입력받기
num = input('정수를 입력해주세요>>') #타입은 str

num1 = int(input('정수를 입력하세요 >>'))
num2 = int(input('정수를 입력하세요 >>'))
print('더하기 결과 : {}'.format(num1+num2))
print('빼기 결과 : {}'.format(num1-num2))
print('곱하기 결과 : {}'.format(num1*num2))
print('나누기 결과 : {}'.format(num1/num2))

num1 = int(input('python 점수 입력 >>'))
num2 = int(input('머신러닝 점수 입력 >>'))
num3 = int(input('딥러닝 점수 입력 >>'))
#변수를 항상 활용할 것!
total = num1 + num2 + num3
avg = total/3
print('합계 : {}'.format(total))
print('평균 : {}'.format(avg))

# 문자열 곱하기
s = 'python'
print(s*5) #pythonpythonpythonpythonpython

# 지수 연산
result = 2**3
print(result) #2의 3승

#num1과 num2의 값을 치환하기
num1 = 10
num2 = 5
print(num1)
print(num2)

num1, num2 = num2, num1
print(num1)
print(num2)

# 삼항연산자
score = 80
print('합격' if score>=80 else '불합격')
score = 50
result = '합격' if score>=80 else '불합격' #변수 활용
print(result)

# 조건문 (if, if~else, if~elif~else)
num = int(input('정수 입력 >> '))
if num%3 ==0 and num%5 == 0:
    print('3과 5의 배수입니다.')
else:
    print('3과 5의 배수가 아닙니다.')

score = int(input('점수 입력 >> '))
result = ''

if 90 <= score <= 100:
    result = 'A'
elif 80 <= score <90:
    result = 'B'
elif 70 <= score < 80:
    result = 'C'
elif 60 <= score < 70:
    result = 'D'
else:
    result = 'F'
print('{}점은 {}학점 입니다.'.format(score, result))