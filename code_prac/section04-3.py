# section04-3
# 파이썬 데이터 타입(자료형)
# 리스트 튜플

# 리스트( 순서O, 중복o, 수정o, 삭제o)
# 선언 [] , list()

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, [1334,1415], 'oewa', '2400!!']

# 인덱싱 , 슬라이싱

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 1000]
print(c)
del c[1]
print(c)

# 리스트 함수

y =[5,2,3,1,32]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2, 7) # 지정 인덱스값을 바꿈
print(y)
y.remove(2) # 입력한 데이터 값을 지움
print(y)
y.pop() # 스택 
print(y)
ex = [88, 77]
y.extend(ex)
print(y)


# 삭제 : del, remove , pop

# 튜플 (순서O, 중복 o, 수정 x, 삭제 x)
# 변경안되는 키, 계좌와 같은 중요한 값들에 사용됨

a = ()
b = (1,)
print(b)
c = (10, 100, ('a', 'b', 'c'),132)
print(c[2])
print(c[3])
print(c[2][1])
print(c[:-1])
print(c[2:3])

# 튜플 함수
print()
print()
z = (5, 2, 1, 3, 4)
print(z)
print(3 in z)
print(z.index(3)) # 지정한 값에 인덱스 번호 나옴
print(z.count(1)) # 지정한 값의 갯수를 반환해줌

