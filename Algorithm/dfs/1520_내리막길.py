import sys

sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)
m, n = map(int, input().split())
cnt = 0
board = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(m):
    board.append(list(map(int, input().split())))


def dfs(y, x):
    global cnt
    if (y == m-1) and (x == n-1):
        cnt += 1
        return

    visited[y][x] = 1
    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]

        if (0 <= new_y < m) and (0 <= new_x < n):
            #print(new_y, " ", new_x)
            if board[new_y][new_x] < board[y][x] and visited[new_y][new_x] == 0:
                dfs(new_y, new_x)
                visited[y][x] = 0


dfs(0, 0)
print(cnt)
