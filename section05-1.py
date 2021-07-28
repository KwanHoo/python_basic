# section 05-1 파이썬 제어, 조건문

print(type(True))
print(type(False))

#예1
if True:
    print("yes")

if False:
    print("no")
else:
    print("gosi!!")

# 참 : "내용", [내용], (내용), {내용}, 1
# 거짓 : "", [], (), {}, 0

# section-05-2
# 파이썬 흐름제어(반복문)

# 코딩의 핵심 -> 조건 해결 중요
# for , while

v1 = 1

while v1 <11 :
    print(v1)
    v1 += 1

for v2 in range(10):
    print("v2 is : ",v2)

# 1 ~ 100 합

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1
print('1부터 100까지 합 : ' ,sum1)
print('1부터 100까지 홀수합 : ' , sum(range(1,101 , 2)))


# 시퀀스( 순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수: range, reversed, enumerate, fileter, map, zip

names = ["kim", "park", "Lee", "choi"]

for name in names:
    print("How are you? ", name)

word = "dream perfect"

for a in word:
    print(a)

my_info ={
    "name" : "Ralo",
    "age" : "27",
    'City' :'Kimhe'
}
# 키
for key in my_info:
    print(key)
print("-------")
# 벨류
for a in my_info.values():
    print(a)
print("-------")
# 키
for key in my_info.keys():
    print(key)
print("-------")
# 키, 벨류
for k, v in my_info.items():
    print(k, v)

name = "KimCH"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())

# break : 빠져나오는거

numbers = [27, 1400, 2400, 3, 23, 34, 66, 72 ,888 , 36, 77, 93]

for a in numbers:
    if a == 2400:
        print("2400!! 2400!!")
        break
    else:
        print("1400!!")
else:  # 반복문이 정상적으로 수행된 경우(끝까지 간경우(2400 break 안하는경우)) ELSE 블럭 수행
    print('김찬호가 방송을 키지 않아!!')

# continue

li = ["1", 2 , 5, True, 4.3, complex(4)]

for v in li:
    if type(v) is float:
        print("불만읎제")
        continue
    print(v)
