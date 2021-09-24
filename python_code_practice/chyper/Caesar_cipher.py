# chr() 함수는 숫자를 인자로 주면 아스키 코드에 해당하는 문자를 반환하며 (아스키 코드 -> 문자)
# ord() 함수는 문자의 아스키 코드를 반환한다. (문자 -> 아스키 코드)


def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return "".join(s)

def xor_c(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            # s[i] = chr(int(bin(((ord(s[i]) - ord('A') + n) % 26 + ord('A')) ^ n), 2)) # xor->2진수 10진수변환
            s[i] = chr(int(bin(ord(s[i]) ^ n), 2))
        elif s[i].islower():
            # s[i] = chr(int(bin(((ord(s[i]) - ord('a') + n) % 26 + ord('a')) ^ n), 2))
            s[i] = chr(int(bin(ord(s[i]) ^ n), 2))

    return "".join(s)



if __name__ == "__main__":
    cstring1, cstring2, cstring3, xstring1, xstring2, xstring3, num1 = input("입력하세요 :").split() # split사용하여 여러가 인풋받기
    num1 = int(num1)
    print(caesar(cstring1, num1))
    print(caesar(cstring2, num1))
    print(caesar(cstring3, num1))
    print(xor_c(xstring1, num1))
    print(xor_c(xstring2, num1))
    print(xor_c(xstring3, num1))