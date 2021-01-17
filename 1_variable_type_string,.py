# 변수 선언 방법1
a = 10
b = 1

# 2
a, b = 10, 15

# 3
origin = temp = 20

# 문자열 안에 작은 따옴표나 큰 따옴표 쓰는 경우
s1 = "she's gone"
s2 = 'she\'s gone'

# 따옴표 3개로 문자열 데이터 자유롭게 작성 가능
s = '''여러 줄로 구성된
문자열을 하나로 대입할 때'''

# 문자열 인덱싱
review = '이 영화는 너무 재미없다 노잼 비추!'
print("'"+review[-6]+review[-5]+"'") # '노잼'
print("'"+review[-3]+review[-2]+review[-1]+"'") #'비추'
print(review[-6:-4]) #노잼(뒤 숫자-1 까지 출력)
print(review[-3:-1]+review[-1]) # 비추!

msg = 'My name is MJ'
print(msg[0]) #M
print(msg[6]) #e
print(msg[-4]) #s
print(msg[3]+msg[4]+msg[5]+msg[6]) #name
print(msg[3:7]) #name
print(msg[:7]) # =print(msg[0:7])처음과 긑 부분은 굳이 숫자를 안써도 됨

# 문자열 포맷팅
date, month, day = 28, 12, '오늘'
s = '%s은(는) %d월 %d일 입니다.'%(day, month, date)
print(s)

d = '{}은(는) {}월 {}일 입니다.'.format(day, month, date)
print(d)

# find()함수 : 찾고자 하는 문자나 단어, 문장이 몇번째 인덱스에 있는지 알려줌
msg = 'Life is short. You need Python.'
print(msg.find('t'))
print(msg.find('You need Python'))

# strip()함수 : 양쪽 공백을 제거해주는 함수. 크롤링에서 주로 사용
msg = '       Life is short. You need Python.        '
print(msg)
print(msg.strip())

# replace(old data, new data)함수 : 기존의 데이터를 새로운 ㅔㄷ이터로 대체
msg = 'Life is short. You need Python'
print(msg.replace('short','long'))
print(msg) # 원본 데이터에는 영향 주지 않음. 영향 주려면 따로 변수 선언

# split()함수 : 특정 문자를 기준으로 문자열을 나누는 함수(리스트 타입 반환)
print(msg.split(' '))
print(msg.split('.'))

