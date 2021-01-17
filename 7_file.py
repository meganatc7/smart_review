# # 파일 입력 방법('w' write의 약자)
f1 = open("연습.txt","w")
f1.write("hello world")
f1.close()

# 반복문 사용해서 입력
f2 = open("연습2.txt","w")
for i in range(1,6):
    f2.write('{}번째 줄입니다.\n'.format(i))
f2.close()

# 파일 읽기 -- 1. readline()
# 연속 사용 시 다음 줄 출력
f3 = open("연습2.txt","r")
line = f3.readline()
print(line)
line = f3.readline()
print(line)
line = f3.readline()
print(line)
line = f3.readline()
print(line)
line = f3.readline()
print(line)

# 다음 값이 없을 때 readline()사용 시 None값 리턴
line = f3.readline()
print(line)
line = f3.readline()
print(line)
f3.close()

# 반복문 사용해서 읽기
f4 = open("연습2.txt","r")
while True:
    line = f4.readline()
    if not line:
        break
    print(line)
f4.close()

# readlines()함수 사용, 리스트 타입으로 저장됨
f5 = open("연습2.txt","r")
lines = f5.readlines()
print(lines)
f5.close()

# 반복문으로 한줄 씩 읽어오기
f6 = open("연습2.txt","r")
lines = f6.readlines()
for i in lines:
    print(i)
f6.close()

# read()함수 사용
f7 = open("연습2.txt","r")
data = f7.read()
print(data)
f7.close()

# 파일 추가하기 (w는 추가 작성이 아닌 덮어쓰기, 'a' append의 약자)
f8 = open("연습2.txt","a")
f8.write('6번째 줄입니다.\n')
f8.close()

# 다시 읽어오기
f9 = open("연습2.txt","r")
data = f9.read()
print(data)
f9.close()

# with문 : 파일 사용이 끝나면 자동으로 닫아주는 기능을 갖고 있는 문장
# open() 사용 시 항상 close()로 닫아줘야함.
with open("연습2.txt","a") as f:
    f.write("7번째 줄입니다.")

with open("연습2.txt","r") as f:
    data = f.read()
    print(data)