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

