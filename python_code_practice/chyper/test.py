# 10진수를 2진수로 된 문자열로 변환할 때는 bin을 사용합니다. 반대로 2진수에서 10진수로는 입력 즉시 변환됩니다.
a= bin(4)
print(a)
print(0b1101)
b = bin(3)
h = bin(0b1111 ^ 0b10101)
print(h)

a = 0b10000000
b = 0b01110011
print('a ^ b = ',  a ^ b, ":", bin(a ^ b))

print(type(a)) # int type
c = type(bin(128)) #str type
# 문자 입력 되는 부분
d = ord('h')
e= ord('g')
print(c)
print(d)
print(type(d)) # int type

print(bin(d ^ e)) # xor
bin_int =bin(d ^ e) # xor
print(bin_int)
conv = int(bin_int, 2) # 2진수 10진수 변환
print(conv)