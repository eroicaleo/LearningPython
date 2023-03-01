def solution(x, y):
    x, y = int(x), int(y)
    a, b = max(x, y), min(x, y)
    ret = 0
    while b > 0:
        q, r = divmod(a, b)
        ret += q
        a, b = b, r
    return str(ret - 1) if a == 1 else "impossible"

if __name__ == '__main__':
    print(solution('2', '1'))
    print(solution('7', '4'))
    print(solution('2', '4'))