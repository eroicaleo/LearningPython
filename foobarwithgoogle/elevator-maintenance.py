def solution(l):
    return sorted(l, key=lambda v: tuple(map(int, v.split('.'))))


if __name__ == '__main__':
    print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
    print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))