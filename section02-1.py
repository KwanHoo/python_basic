# Section 02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본출력
print("hello?")
print()

# Separator 옵션 사용

print('T', 'E', 'S', sep='')
print( '0329', '1123', sep='-')
print('Ralo', '129' , sep='@')

# end 옵션 사용

print('Welccome to', end=' ')
print('the black parade', end=' ')
print('piano notes')

# format 사용
print('{} and {}'.format('apple', 'banana'))
print("{0} and {1} and {0}".format('you', 'me'))

# %s : 문자 / %d : 정수 / %f : 실수
print("%s's favorite number is %d" %('ho', 7))

print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("test1 : {0: 5d}, Price : {1: 4.2f}".format(776, 6534.123))
print("test1 : {a: 5d}, Price : {b: 4.2f}".format(a = 776, b = 6534.123))

# Escape 코드  \n , \t \\ \' \" 등


# tasks  빠른 런  =>> 단축키 : ctrl + shift + b