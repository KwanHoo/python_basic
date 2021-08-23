# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스(객체), 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언
# class 클래스명:
    #속성, 메소드(움직임이 있는것)
#     함수
#     함수
#     함수


# 예제1

class UserInfo:  # 클래스명 첫글자는 대문자
    def __init__(self, name): #__init__매직매소드 # 클래스 최초 초기화 하는 함수
        self.name = name

    def print_info(self):
        print("Name: " + self.name)

    def __del__(self):
        print("Instance removed!")

user1 = UserInfo("Kim") #인스턴스 생성
user2 = UserInfo("Park")
 
 # 인스턴스는 서로 독립적인 네임스페이스
print(id(user1)) #id : 메모리의 주소값 찍어줌
print(id(user2))

user1.print_info()
user2.print_info()

print('user1 : ', user1.__dict__)  # 클래스 네임스페이스 확인
print('user2 : ', user2.__dict__)

print(user1.name)

# 예제2
# self의 이해

class SelfTest:
    def function1():
        print("function1 called!")

    def function2(self):
        print(id(self))
        print("function2 called!")


f = SelfTest()
# print(dir(f))
print(id(f))
# f.function1() #예외 발생 : 클래스 에서 직접 호출
f.function2() 
print(SelfTest.function1())


# print(SelfTest.function2()) #예외 발생


# 예제3
# 클래스 변수(self 없음, 공통으로 공유함) , 인스턴스 변수 (self 가 들어가야함)

class Warehouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1 # 클래스 변수는 직접 접근

    def __del__(self):  # __del__ : 인스턴스가 종료될때 호출되는 함수
        Warehouse.stock_num -= 1


user1 = Warehouse('Kim')
user2 = Warehouse('Park')

print(user1.name)
print(user2.name)
print(user1.__dict__) # 인스턴스 변수는 각각 가지고
print(user2.__dict__)
print(Warehouse.__dict__)  # 클래스 네임스페이스 , 클래스 변수 (공유)

# Warehouse.stock_num = 50 # 직접 접근 가능

print(user1.stock_num)
print(user2.stock_num)
