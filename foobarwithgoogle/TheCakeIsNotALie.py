from math import sqrt


def solution(s):
    # Your code here
    l = len(s)
    for i in range(1, l + 1):
        if l % i != 0:
            continue
        t = s[:i]
        for j in range(i, l, i):
            if t != s[j:j+i]:
                break
        else:
            return l // i


if __name__ == '__main__':
    s = "abcabcabcabc"
    print(solution(s))
    print(solution("abccbaabccba"))
    print(solution("a"))
    print(solution("aaa"))
    print(solution("aaaab"))