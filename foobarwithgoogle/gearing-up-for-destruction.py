def solution(pegs):

    def is_feasible(r):
        for i in range(len(pegs) - 1):
            if pegs[i] + r >= pegs[i + 1]:
                return False
            r = pegs[i + 1] - (pegs[i] + r)
        return True

    sign, sum, l = 1, 0, len(pegs)
    for i in range(1, l):
        sum += sign * (pegs[i] - pegs[i - 1])
        sign = -sign
    if sum <= 0:
        return [-1, -1]
    denominator = 3 if sign < 0 else 1
    [numerator, denominator] = [2 * sum, denominator] if (sum % denominator) != 0 else [(2 * sum // denominator), 1]
    if is_feasible(numerator/denominator):
        return [numerator, denominator]
    else:
        return [-1, -1]


if __name__ == '__main__':
    print(solution([4, 17, 50]))
    print(solution([4, 30, 50]))
    print(solution([6, 15, 33, 51]))
    print(solution([2, 11, 12]))
    print(solution([2, 5, 8, 11]))
    print(solution([2, 4, 5]))

