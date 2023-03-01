def solution(l):
    dp = [0] * len(l)
    ret = 0
    for i in range(1, len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                dp[i] += 1
                ret += dp[j]
    # print(dp)
    return ret


if __name__ == '__main__':
    print(solution([1,2,3,4,5,6]))
    print(solution([1,1,1,1,1]))
    print(solution([5,4,7]))
    print(solution([1,2,4,8,16]))
    print(solution([1,1]))