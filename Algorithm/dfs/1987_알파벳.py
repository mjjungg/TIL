import sys

#sys.stdin = open("input.txt", "rt")


def DFS(y, x, cnt):
    global res

    if res < cnt:
        res = cnt

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if 0 <= new_y < n and 0 <= new_x < m:
            if lst[new_y][new_x] not in alpha:
                alpha.append(lst[new_y][new_x])
                DFS(new_y, new_x, cnt + 1)
                alpha.pop()



if __name__ == "__main__":
    n, m = map(int, input().split())
    res = 0
    lst = [list(map(str, input())) for _ in range(n)]
    dx = [0, 0, -1, 1] # 상, 하, 좌, 우
    dy = [-1, 1, 0, 0]
    alpha = list()
    alpha.append(lst[0][0])
    DFS(0, 0, 1)
    print(res)
