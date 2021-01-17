# 반복문
# - 특정 조건에 따라 실행문장 반복해서 실행
# - while, for-each, range()함수를 활용한 for문

# for-each 구조 for 변수명 in 리스트: 실행문장
for i in range(100,301):
    if int((i/100)%2) == 0 and int((i/10)%2) == 0 and int(i%2) == 0:
        print(i)

food_list = ['햄버거', '치킨', '피자']
for food in food_list:
   print(food)

score_list = [90, 45, 70, 60, 55]
num = 1
for result in score_list:
    if result >= 60:
        print('{}번 학생은 합격입니다.'.format(num))
    else:
        print('{}번 학생은 불합격입니다.'.format(num))
    num = num + 1

for i in range(1, 11, 1):
    print(i)

for j in range(10):
    print(j+1, end = ' ') #print()함수의 end속성 기본값 \n(줄바꿈), 새로운 값 지정하면 줄바꿈 사라짐

for k in range(97,76,-1):
    print(k,end = ' ')

# list 안에 list 요소 뽑기
list1 = [[1,2],[3,4],[5,6]]
for i in list1:
    print(i)
for i,j in list1:
    print(i,j)
for i in list1:
    for j in i:
        print(j)

#두 개의 정수를 입력받아 첫 번째 정수 부터 두 번째 정수까지 출력되는 코드
start = int(input('첫 번째 정수 입력 >> '))
end = int(input('두 번째 정수 입력 >> '))

for i in range(start, end+1):
    print(i, end=' ')

# 구구단 2단
num = 2
for i in range(1,10):
    print("{} x {} = {}".format(num, i, num*i))

# 약수 구하기
num = int(input('정수 입력 >> '))
print('{}의 약수 : '.format(num), end=' ')
for i in range(1,num+1):
    if num%i == 0:
        print(i,end=' ')    

# while문
num = 0
while num<10:
    print('hi')
    num += 1

# break
num = 0
while True:
    num += 1
    print(num)
    if num >= 10:
        break

while True:
    num1 = int(input('첫 번째 정수 입력 >> '))
    num2 = int(input('두 번째 정수 입력 >> '))
    print('두 정수의 합 : {}'.format(num1+num2))
    if num1+num2==0:
        print('프로그램이 종료되었습니다.')
        break
    
# 랜덤 수 뽑기
import random as r

num = r.randint(1,50)
num1 = 0
while num != num1:
    num1 = int(input('숫자를 입력하세요>>'))
    if num1 > num:
        print('{}보다 작은 수입니다.'.format(num1))
    else:
        print('{}보다 큰 수입니다.'.format(num1))
print('정답입니다!')
    