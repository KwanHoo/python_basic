# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집한 자료형

# 딕셔너리(Dictionary) : 순서 x, 키는 중복x, 수정o, 삭제o

# Key, Value (Json)-> MongoDB
# 선언
a = {'name' : 'KIM', 'Phone' : '010-1234-1234', 'birth' : 991122}
b = {0 : 'Hello Python', 1 : 'Hello Ralo'}
c = {'arr' : [1, 2, 3, 4, 5]} #딕셔너리 안에는 모든 값들(자료형들)이 들어 올 수 있다
print(type(a))

# 출력
print(a['name'])
print(a.get('name'))
print(a.get('address')) # get함수로 키를 찾았을때 없으면 None 값을 반환해줌 # 찾을때 get함수 사용하는거 추천
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)

# keys, values, items(키와 벨류 한쌍을 뜻함)
print(a.keys())
print(list(a.values()))
ex1 = (list(a.items()))

for i in ex1:
    print(i)

# 집합(set) 순서 없고, 중복 없음
print()
print()
print()
a = set()
b = set([1, 2, 3,4, 56])
c = set([3, 4 , 56, 7,4])
print(type(a))
print(c)

s1 = set([1,2,3,4,5,6,7])
s2 = set([4,5,6,7,87,8])
print(s1.intersection(s2)) #교집합
print(s1 & s2) # 교집합

print(s1 | s2) #합
print(s1.union(s2)) #합집합
print(s1 - s2) #차
print(s1.difference((s2))) #차집합

