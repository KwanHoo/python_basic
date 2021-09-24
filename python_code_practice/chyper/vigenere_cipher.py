# 비즈네르 암호화 프로그램
def encipher(p, k):
    c = ''
    n = len(k)
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32: a = 64
        b = ord(k[i % n]) - 64
        t = a + b
        if t > 90: t -= 27
        if t == 64: t = 32
        c += chr(t)
    return c

def encipher1(s, k):
    s = list(s)
    k = list(k)

    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr(((ord(s[i]) - ord('A')) + (ord(k[i])-ord('A')))% 26 + ord('A'))
        elif s[i].islower():
            # s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
            # s[i] = chr((ord(s[i]) + (ord(k[i])-ord('a'))))
            s[i] = chr(((ord(s[i]) - ord('a')) + (ord(k[i])-ord('a'))) % 26 + ord('a'))

    return "".join(s)



if __name__ == "__main__":
    vstring1 = input()
    vstring2 = input()
    vstring3 = input()
    vstring4 = input()
    vstring5 = input()
    cstring1 = input()

    print(encipher(vstring1,cstring1))
    print(encipher(vstring2,cstring1))
    print(encipher(vstring3,cstring1))
    print(encipher(vstring4,cstring1))
    print(encipher(vstring5,cstring1))

