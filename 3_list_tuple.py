# 리스트 선언
list1 = [1,2,3,4,5]
list2 = ['사과', '딸기', '멜론', '바나나']
list3 = ['가나',23,'체코',33]
list4 = [[1,2,3],[4,5,6],[7,8,9]]

print(list1[2])
print(list2[3])
print(list1[1:4])

# 리스트에 데이터 추가
song_list = []
song_list.append('Gone')
song_list.append('사랑은')
song_list.append('소소한 해피엔딩')
song_list.append('Credit')
song_list.append('Freak')
song_list.append('VVS')
print(song_list)

# 데이터 삭제
del song_list[0] # 인덱싱이나 슬라이싱으로 삭제
song_list.remove('사랑은') # 요소명으로 삭제
print(song_list)

# 데이터 추가2 // inser(인덱스, 요소)
song_list.insert(0,'Gone')
song_list.insert(1,'사랑은')
print(song_list)

# index()함수 : 요소의 인덱스값
print(song_list.index('Freak'))

# len() : 리스트 내 요소들의 갯수 확인
print(len(song_list))

# 튜플 선언
tuple1 = (1,2,3,4,5)

# 인덱싱
print(tuple1[0])
print(tuple1[0:3])