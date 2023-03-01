from collections import deque


def print_visited(visited):
    for row in visited:
        print(row)
    print()


def solution(map):
    nr, nc = len(map), len(map[0])
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = [[[float("inf"), float("inf")] for _ in range(nc)] for _ in range(nr)]
    visited[0][0] = [1, 0]
    queue = deque([(0, 0, 1, 0)])
    while len(queue) > 0:
        i, j, s, r = queue.popleft()
        print(f'i = {i}, j = {j}, s = {s}, r = {r}')
        if i == nr - 1 and j == nc - 1:
            return s
        for dx, dy in delta:
            x, y = i + dx, j + dy
            if 0 <= x < nr and 0 <= y < nc and max(visited[x][y]) == float("inf"):
                s1 = s + 1
                r1 = r + 1 if map[x][y] == 1 else r
                if r1 > 1: continue
                if s1 >= visited[x][y][r1]: continue
                visited[x][y][r1] = s1
                queue.append([x, y, s1, r1])
        print_visited(visited)
    return -1


if __name__ == '__main__':
    # map = [[0, 1, 1, 0],
    #        [0, 0, 0, 1],
    #        [1, 1, 0, 0],
    #        [1, 1, 1, 0]]
    # print(solution(map))
    # map = [[0, 0, 0, 0, 0, 0],
    #        [1, 1, 1, 1, 1, 0],
    #        [0, 0, 0, 0, 0, 0],
    #        [0, 1, 1, 1, 1, 1],
    #        [0, 1, 1, 1, 1, 1],
    #        [0, 0, 0, 0, 0, 0]]
    # print(solution(map))
    # map = [[0, 1, 0, 0, 0, 0],
    #        [0, 0, 0, 1, 1, 0],
    #        [1, 1, 1, 0, 0, 0],
    #        [1, 1, 1, 1, 1, 1],
    #        [1, 1, 1, 1, 1, 0],
    #        [1, 0, 0, 0, 0, 0]]
    # print(solution(map))

    map = [[0, 1],
           [0, 0],
           [1, 0],
           [1, 0],
           [1, 1],
           [1, 0]]
    print(solution(map))