import sys


'''
    7576 토마토
    처음에 dfs로 접근함
    
'''


def dfs(k, l):
    global cnt
    if visited[k][l] == 1:
        return

    visited[k][l] = 1
    for i in range(4):
        new_y = k + dy[i]
        new_x = l + dx[i]
        if (0 <= new_y < m) and (0 <= new_x < n):
            if tomatos[new_y][new_x] == 0:
                tomatos[new_y][new_x] = 1
                cnt += 1
                dfs(new_y, new_x)



if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")

    cnt = 0
    n, m = map(int, input().split())
    tomatos = [[] for _ in range(m)]
    visited = [[0 for _ in range(n)] for _ in range(m)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(m):
        r = list(map(int, input().split()))
        tomatos[i] = r

    for i in range(m):
        for j in range(n):
            if tomatos[i][j] == 1:
                if visited[i][j] == 0:
                    cnt += 1
                    dfs(i, j)

    print(cnt)


'''
    2025.02.27
    사용한 풀이: bfs
    
'''
import sys
from collections import deque


def check(lst):
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == 0:
                return False
    return True

if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    m, n = map(int, input().split())

    tomatos = []
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    result = 0

    for i in range(n):
        lst = list(map(int, input().split()))
        tomatos.append(lst)
        for j in range(m):
            if tomatos[i][j] == 1:
                q.append((i, j))

    if check(tomatos):
        print(0)
        sys.exit()

    while q:
        y, x = q.popleft()

        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]

            if (0 <= ny < n) and (0 <= nx < m):
                if tomatos[ny][nx] == 0 and visited[ny][nx] == 0:
                    q.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
                    tomatos[ny][nx] = 1

    if check(tomatos):
        for k in visited:
            result = max(result, max(k))

        print(result)
    else:
        print(-1)
