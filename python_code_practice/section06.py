# *args, **kwargs   /*가 하나면 튜플 **면 딕셔너리로 

# 튜플로 넘어옴  /매개변수가 가변
def args_func(*args):
    # print(args)
    for i,v in enumerate(args): #이너뮬레이트
        print(i,v)

args_func('Kim')
args_func('Kim', 'Park')
args_func('Kim', 'Park', 'Lee')

# kwargs (kw:키워드)
# 딕셔너리 형태로 넘길수 있음
def kwargs_func(**kwargs):
    print(kwargs)


kwargs_func(name1='Kim')
kwargs_func(name1='Kim', name2='Park')
kwargs_func(name1='Kim', name2='Park', name3='Lee')


# 전체 혼합  (필수 인자 2개, 가변인자 2개)
def example(arg_1, arg_2, *args, **kwargs):
    print(arg_1, arg_2, args, kwargs)


example(10, 20, 'park', 'kim', 'lee', age1=33, age2=34, age3=44)


# 중첩함수(클로저)
# +)추가 고급스킬 : 데코레이터 클로저
def nested_func(num):
    def func_in_func(num):
        print(num)

    print("In func")
    func_in_func(num + 100)


nested_func(1)


# 예제6
# Hint : 함수를 명시적으로 알려줄 수 있음
def tot_length1(word: str, num: int) -> int: # word는 str형을 입력받고 출력은 int형을 출력해준다
    return len(word) * num


print('hint exam1 : ', tot_length1("i love you", 10))


def tot_length2(word: str, num: int) -> None:
    print('hint exam2 : ', len(word) * num)


tot_length2("niceman", 10)

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화

# 예제7
# def mul_10(num):
#     return num * 10

# def mul_10_one(num): return num * 10
#
# lambda x: x * 10


# 일반적 함수 -> 변수 할당
def mul_10(num):
    return num * 10


mul_func = mul_10

print(mul_func)
print(mul_func(6))


# 람다 함수 -> 할당
lambda_mul_func = lambda x: x * 10  # lambda num: num * 10


def func_final(x, y, func):
    print(x * y * func(10))


func_final(10, 10, lambda_mul_func)