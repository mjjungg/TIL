'''
        4673 셀프 넘버  
'''

def split_num(x):
    lst = []
    while x // 10 > 0:
        lst.append(x % 10)
        x = x // 10
    lst.append(x)

    return lst

if __name__ == "__main__":
    n = 10000
    self_num_lst = []

    for i in range(1, n+1):
        self_num = i
        r = split_num(i)

        for j in range(len(r)):
            self_num += r[j]

        self_num_lst.append(self_num)

    for i in range(1, n+1):
        if i not in self_num_lst:
            print(i)

        
'''
        1316 그룹단어 체커
'''
        
if __name__ == "__main__":
    n = int(input())
    res = n

    for _ in range(n):
        s = input()
        check = []

        for i in s:
            if i not in check:
                check.append(i)
            else:
                if check[-1] != i:
                    res -= 1
                    break
    print(res)

'''
        2941 크로아티아 알파벳
        
        문자열에서 for문 돌려고만 생각함 -> 크로아티아에서 for문 돎
        
'''


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    s = input()
    c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    for i in c:
        s = s.replace(i, '*')

    print(len(s))

import sys
from collections import deque
'''
        1021 회전하는 큐
        
        1. 큐에서 원소 삭제할 때마다 큐의 길이 갱신해야 하는 부분 빼먹음
        2. 문제 제대로 읽지 않아서 잘못 이해함 
        
        => 구현 문제는 문제 꼼꼼히 읽고 주어진 조건, 변할 때 마다 체크 사항 빠뜨리지 않기!!!!
        
'''

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n, m = map(int, input().split())
    targets = list(map(int, input().split()))
    res = 0
    q = deque([i for i in range(1, n+1)])

    for i in range(m):
        target = targets[i]
        getIdx = q.index(target)
        m = len(q)  # 큐의 길이가 계속 줄어드니 갱신해야 함

        if getIdx < m-getIdx:   # 왼쪽으로 이동
            while True:
                if q[0] == target:
                    q.popleft()
                    break
                else:
                    q.append(q.popleft())
                    res += 1

        else:   # 오른쪽으로 이동
            while True:
                if q[0] == target:
                    q.popleft()
                    break
                else:
                    q.appendleft(q.pop())
                    res += 1

    print(res)


import sys
from collections import deque

'''
    3190 뱀 
    
'''

def move(ny, nx, d):
    global head_y, head_x

    if board[ny][nx] == 0:
        ty, tx = snake.popleft()
        board[ty][tx] = 0

        board[ny][nx] = 1
        head_y = ny
        head_x = nx
        snake.append([head_y, head_x])

    elif board[ny][nx] == 5:
        board[ny][nx] = 1
        head_y = ny
        head_x = nx
        snake.append([head_y, head_x])
    else:
        return 

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())
    k = int(input())
    snake = deque()
    board =[[0 for _ in range(n+2)] for _ in range(n+2)]

    # 오, 아, 왼, 위
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    for i in range(n+1):
        board[0][i] = -1
        board[n+1][i] = -1
        board[i][0] = -1
        board[i][n+1] = -1

    for _ in range(k):
        l, c = map(int, input().split())
        board[l][c] = 5

    board[1][1] = 1
    now_dir = 0
    snake.append([1, 1])

    l = int(input())
    now = 0
    head_y = 1
    head_x = 1
    lst = {}
    for _ in range(l):
        t, d = input().split()
        lst[int(t)] = d

    while True:
        now += 1
        ny = head_y + dy[now_dir]
        nx = head_x + dx[now_dir]
        if board[ny][nx] == -1 or board[ny][nx] == 1:
            print(now)
            break
        move(ny, nx, now_dir)

        if now in lst:
            if lst[now] == 'D':
                now_dir = (now_dir + 1) % 4
            else:
                now_dir = (now_dir - 1) % 4

                
'''
    16236 아기 상어 
    
    최단거리: bfs로 풀기 
    
'''

# 1. 현재 위치로부터 모든 보드의 위치까지의 최단 거리 구하기
# 2. 최단 거리 구한 위치에 있는 물고기 중 잡아먹을 수 있는 것 eat 리스트에 담기
def bfs(cy, cx, size):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    dis = [[-1 for _ in range(n)] for _ in range(n)]
    eat = []
    dis[cy][cx] = 0
    q = deque()
    q.append([cy, cx])
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (0 <= ny < n) and (0 <= nx < n):
                if dis[ny][nx] == -1:   # 방문하지 않았고
                    if board[ny][nx] <= size:   # 해당 위치로 이동 가능한 경우
                        q.append([ny, nx])
                        dis[ny][nx] = dis[y][x] + 1

                        if 0 < board[ny][nx] < size:
                            eat.append([ny, nx, dis[ny][nx]])

    return sorted(eat, key=lambda x:(x[2], x[0], x[1]))


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())
    board = []
    ny, nx = 0, 0
    size = 2
    time = 0
    eating = 0

    for _ in range(n):
        board.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                ny, nx = i, j

    while True:
        fish = bfs(ny, nx, size)
        if len(fish) == 0:
            break

        y, x, dis = fish.pop(0)
        board[ny][nx] = 0
        board[y][x] = 0
        ny, nx = y, x

        time += dis
        eating += 1

        if eating == size:
            size += 1
            eating = 0

    print(time)


'''
    14500 테트로미노 
    1. 나의 풀이: 테트로미노의 위치 고정해서 완전탐색하는 방식 -> 파이썬 시간초과로 pypy 제출 
    
'''

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")

    figure = [ [[0, 0], [0, 1], [0, 2], [0, 3]],
               [[0, 0], [1, 0], [2, 0], [3, 0]],
               [[0, 0], [0, 1], [1, 0], [1, 1]],
               [[0, 0], [1, 0], [2, 0], [2, 1]],
               [[0, 0], [1, 0], [0, 1], [0, 2]],
               [[0, 0], [0, 1], [1, 1], [2, 1]],
               [[1, 0], [1, 1], [1, 2], [0, 2]],
               [[2, 0], [0, 1], [1, 1], [2, 1]],
               [[0, 0], [1, 0], [1, 1], [1, 2]],
               [[0, 0], [1, 0], [2, 0], [0, 1]],
               [[0, 0], [0, 1], [0, 2], [1, 2]],
               [[0, 0], [1, 0], [1, 1], [2, 1]],
               [[0, 0], [0, 1], [1, 1], [1, 2]],
               [[1, 0], [0, 1], [1, 1], [0, 2]],
               [[1, 0], [2, 0], [0, 1], [1, 1]],
               [[0, 0], [0, 1], [1, 1], [0, 2]],
               [[1, 0], [0, 1], [1, 1], [2, 1]],
               [[1, 0], [0, 1], [1, 1], [1, 2]],
               [[0, 0], [1, 0], [2, 0], [1, 1]]
               ]

    n, m = map(int, input().split())
    board = []
    res = 0
    for _ in range(n):
        board.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(m):
            for k in range(len(figure)):
                val = 0
                for h in range(len(figure[k])):
                    if (0 <= i + figure[k][h][0] < n) and (0 <= j + figure[k][h][1] < m):
                        val += board[i + figure[k][h][0]][j + figure[k][h][1]]
                    else:
                        break
                    if res < val:
                        res = val

    print(res)
