# 딕셔너리의 key값은 유일해야 함
dic_test = {
    '이름': 'young',
    '나이': 27,
    '전화번호': '010-9552-1234',
}
print(dic_test)
print(dic_test['이름'])     #없는 키 값 입력시 에러가 남
print(dic_test.get('나이')) #없는 키 값 입력시 에러가 안남
print(dic_test.get('키'))   #None으로 나옴

# 존재하는 dictionary에 값 추가
dic_test['생일'] = '4월 10일'
print(dic_test)

# 값 삭제
del dic_test['나이']
print(dic_test)

# 딕셔너리의 키 값만 가져오기
print(dic_test.keys())
print(list(dic_test.keys())) # list타입으로

# 딕셔너리의 value값만 가져오기
print(dic_test.values())
print(list(dic_test.values()))

# 반복문으로 key값 뽑기
for key in dic_test.keys():
    print(key)
print(type(key))

# 반복문으로 value값 뽑기
for value in dic_test.values():
    print(value)

# 반복문으로 key, value 동시에 가져오기
for k, v in dic_test.items():
    print(k, v)

# in 키워드 : key in 딕셔너리명 --> 결과값은 True of False (key만 가능)
print('생일' in dic_test)
print('키' in dic_test)

# 딕셔너리에 있는 모든 값 지우기
dic_test.clear()
print(dic_test)