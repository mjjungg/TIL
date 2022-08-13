import sys


'''
    1967번 트리의 지름
    
    왼쪽 노드의 부모 계속 타고 올라감 + 오른쪽 노드 부모 계속 타고 올라감 => 만나는 부모 
    만나는 부모에서부터 왼쪽 타고 내려감 + 만나는 부모에서부터 오른쪽 타고 내려감 => 지름
    지름은 구할 수 있지만, 그 중에서 최대값 어떻게 구함??
    
    1. 루트 노드부터 최장 가중치 따라감 -> 최종 끝 루트 찾음
    2. 최종 끝 루트부터 최장 가중치 따라감 -> 최장 지름 도출
    
    bfs/dfs를 두 번 해야하는 문제!! 
    생각의 전환 필요한 문제
    
    부모의 왼쪽 + 부모의 오른쪽 
    -> 부모의 왼쪽 + 구한 부모의 왼쪽을 부모 노드로 설정! 
'''

# dfs 풀이
def dfs(start, weight):
    for node, w in board[start]:
        if weight[node] == 0:
            weight[node] = weight[start] + w
            dfs(node, weight)

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")

    n = int(input())
    board = [[] for _ in range(n+1)]

    for _ in range(n-1):
        p, c, w = map(int, input().split())
        board[p].append([c, w])
        board[c].append([p, w])

    weight1 = [0 for _ in range(n+1)]
    dfs(1, weight1)

    start_node = weight1.index(max(weight1))
    weight2 = [0 for _ in range(n+1)]

    dfs(start_node, weight2)
    print(max(weight2))

# bfs 풀이
from collections import deque

def bfs(start, mod):
    global n
    q = deque()
    q.append(start)
    weight = [-1 for _ in range(n+1)]
    weight[start] = 0

    while q:
        now_node = q.popleft()
        for node, w in board[now_node]:
            if weight[node] == -1:
                weight[node] = weight[now_node] + w
                q.append(node)

    if mod == 1:
        return weight.index(max(weight))
    else:
        return max(weight)

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")

    n = int(input())
    board = [[] for _ in range(n+1)]

    for _ in range(n-1):
        p, c, w = map(int, input().split())
        board[p].append([c, w])
        board[c].append([p, w])

    print(bfs(bfs(1, 1), 0))
    
    
    
    
import sys


'''
    2638 치즈 # bfs
    내부 / 외부 공기 어떻게 구분??
    
    1. 모든 치즈가 다 녹았는지 확인. 남은 치즈가 있다면 전부 녹을 때 까지 아래 과정 반복
    2. 외부 공기와 2개 변 이상 접촉한 치즈 체크
    3. 체크된 치즈 녹임
    
    # 치즈 다 녹았는지 어떻게 확인?
    이중 for문 돌면서 일일이 확인
    
    # 내부 / 외부 구문하는 로직
    1. 현재 위치가 공기이고, 상하좌우 탐색에서 치즈가 걸리면 큐에 넣음
       이때, 큐에 넣은 좌표를 다시 넣지 말아야 함
    2. 큐에 들어간 좌표를 리스트에서 -1로 업데이트함 -> -1 : 외부 공기, 0 : 내부 공기 
    -> 외부 공기만 큐에 넣기 때문에, 내부 공기와 분리 된다. 
    
'''

# 바깥 공기를 -1로 초기화
from collections import deque

def initOutSide():
    dq = deque()
    visited_out = [[0 for _ in range(m)] for _ in range(n)]
    dq.append((0, 0))   # 0, 0부터 탐색 시작
    visited_out[0][0] = 1
    board[0][0] = -1

    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < n) and (0 <= nx < m):
                if board[ny][nx] != 1:
                    if visited_out[ny][nx] == 0:
                        board[ny][nx] = -1
                        visited_out[ny][nx] = 1
                        dq.append((ny, nx))


def isAllMelt():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                return False
    return True

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")

    answer = 0
    n, m = map(int, input().split())
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    board = []

    for i in range(n):
        l = list(map(int, input().split()))
        board.append(l)

    while not isAllMelt():
        initOutSide()
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    cnt = 0  # 외부 공기와 맞닿은 변의 개수
                    for k in range(4):
                        ny = i + dy[k]
                        nx = j + dx[k]

                        if (0 <= ny < n) and (0 <= nx < m):
                            if board[ny][nx] == -1:
                                cnt += 1
                    if 2 <= cnt:
                        board[i][j] = 0

        answer += 1

    print(answer)
    
    
    import sys


'''
    7562 나이트의 이동 # bfs
    ※ while문 내부에서 pop()이 아닌 popleft() 사용해야 최소 이동 횟수 나옴!!!!!
    
'''

# 바깥 공기를 -1로 초기화
from collections import deque

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")

    t = int(input())
    for _ in range(t):
        n = int(input())
        answer = 0
        cur_y, cur_x = map(int, input().split())
        goal_y, goal_x = map(int, input().split())
        dy = [-2, -2, -1, -1, 1, 1, 2, 2]
        dx = [-1, 1, -2, 2, -2, 2, -1, 1]
        board = [[0 for _ in range(n)] for _ in range(n)]
        dq = deque()
        dq.append([cur_y, cur_x])
        board[cur_y][cur_x] = 1

        while dq:
            now_y, now_x = dq.popleft()
            if (now_y == goal_y) and (now_x == goal_x):
                print(board[now_y][now_x]-1)
                break

            for i in range(len(dy)):
                next_y = now_y + dy[i]
                next_x = now_x + dx[i]

                if (0 <= next_y < n) and (0 <= next_x < n):
                    if board[next_y][next_x] == 0:
                        board[next_y][next_x] = board[now_y][now_x] + 1
                        dq.append([next_y, next_x])


                        
 import sys


'''
    1389 케빈 베이컨의 6단계 법칙 # bfs
    ※ 자주 나오는 문제 유형이니 꼭 파악해두기!!!
    노드 간 최소 방문 횟수  
'''


from collections import deque

def bfs(s):
    ans = [0 for _ in range(n+1)]
    visited = [s]
    dq = deque()
    dq.append(s)

    while dq:
        now = dq.popleft()
        for i in board[now]:
            if i not in visited:
                ans[i] += ans[now] + 1
                visited.append(i)
                dq.append(i)

    return sum(ans)

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n, m = map(int, input().split())
    board = [[] for _ in range(n+1)]
    for _ in range(m):
       a, b = map(int, input().split())
       board[a].append(b)
       board[b].append(a)

    result = []   # res[0] : 1번 유저의 케빈 베이컨 수
    for i in range(1, n+1):
        result.append(bfs(i))

    print(result.index(min(result)) + 1)



'''
    14716 현수막 # bfs

'''


from collections import deque


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n, m = map(int, input().split())
    board = []
    visited = [[0 for _ in range(m)] for _ in range(n)]
    res = 0
    for _ in range(n):
        l = list(map(int, input().split()))
        board.append(l)
    dy = [1, -1, 0, 0, -1, 1, 1, -1]
    dx = [0, 0, 1, -1, -1, 1, -1, 1]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and visited[i][j] == 0:
                res += 1
                dq = deque()
                dq.append([i, j])
                visited[i][j] = 1
                while dq:
                    cur_y, cur_x = dq.popleft()

                    for k in range(len(dy)):
                        next_y = cur_y + dy[k]
                        next_x = cur_x + dx[k]

                        if (0 <= next_y < n) and (0 <= next_x < m):
                            if board[next_y][next_x] == 1:
                                if visited[next_y][next_x] == 0:
                                    dq.append([next_y, next_x])
                                    visited[next_y][next_x] = 1
    print(res)

    
import sys


'''
    14502 연구소 # bfs
    
    바이러스 퍼짐 - bfs로 처리
    벽은 어디다 세워야 함??? -> 최대한 바이러스 근처
    
    ## 풀이
    벽을 세울 수 있는 모든 경우의 수에 대해서 수행해봐야 함 (백트래킹) 
    -> 최댓값 저장해야 함 
    
    
'''
from collections import deque
import copy

# 바이러스 퍼지는 알고리즘 >> 시간초과 발생 
def bfs():
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    q = deque()
    tmp_boarad = copy.deepcopy(board)   # 매번 바이러스 퍼지는 계산해줘야 하기 때문에 copy
    for i in range(n):
        for j in range(m):
            if tmp_boarad[i][j] == 2:
                q.append([i, j])

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (0 <= ny < n) and (0 <= nx < m):
                if tmp_boarad[ny][nx] == 0:
                    tmp_boarad[ny][nx] = 2
                    q.append([ny, nx])
    return countSafeZone(tmp_boarad)

def countSafeZone(board):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt += 1
    return cnt

def makeWall(cnt):
    global answer
    if cnt == 3:
        res = bfs()
        if answer < res:
            answer = res
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1    # 벽 세움
                makeWall(cnt+1)
                board[i][j] = 0     # 벽 X

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n, m = map(int, input().split())

    board = []
    answer = 0
    for _ in range(n):
        board.append(list(map(int, input().split())))

    makeWall(0)

    print(answer)


    
'''
    7576 토마토    # bfs
    
    정답을 무조건 하나의 변수에만 저장하려하지 말자!
    정답의 후보들을 리스트에 담아두고 리스트의 최소/최대값이 답이 될 수 있다.
    
    ## 첫 시도로 최소 일수를 cnt 변수에 넣으려 했다.
    cnt를 도대체 어디에 해야 할지 막막 
    
    => visited라는 이중 리스트에 해당 위치에 있는 토마토가 익은 날짜를 저장해둠
    이중 리스트에서 최대값이 바로 모든 토마토가 익는 최소 일수가 됨
    
'''


def checkAllTomatos():
    for i in range(n):
        for j in range(m):
            if tomatos[i][j] == 0:
                return False
    return True

from collections import deque

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    m, n = map(int, input().split())
    tomatos = []
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(n):
        tomatos.append(list(map(int, input().split())))

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    q = deque()
    cnt = 0

    if checkAllTomatos():
        print(0)
        sys.exit(0)

    for i in range(n):
        for j in range(m):
            if tomatos[i][j] == 1:
                q.append([i, j])

    while q:
        y, x = q.popleft()
        cnt += 1

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (0 <= ny < n) and (0 <= nx < m):
                if tomatos[ny][nx] == 0:
                    if visited[ny][nx] == 0:
                        tomatos[ny][nx] = 1
                        q.append([ny, nx])
                        visited[ny][nx] = visited[y][x] + 1



    if checkAllTomatos():
        ans = 0
        for i in visited:
            ans = max(ans, max(i))
        print(ans)
    else:
        print(-1)

        
  '''
    2665 미로만들기 
    
    검은 방을 흰 방으로 바꾸려는 생각 -> 흰 방부터 탐색하면서 검은 방일 때 +1씩 늘려주기 
    bfs
    이동거리 이중 리스트 -1로 초기화 
    흰 방 : 이동거리 이전과 같음
    검은 방 : 이동거리 이전 + 1
   
'''

from collections import deque


def bfs():
    q = deque()
    q.append([0, 0])

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    visited[0][0] = 0

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (0 <= ny < n) and (0 <= nx < n) and visited[ny][nx] == -1:
                    if board[ny][nx] == 1:  # 흰 방
                        visited[ny][nx] = visited[y][x]
                        q.appendleft([ny, nx])  # 먼저 deque에 넣음
                    elif board[ny][nx] == 0:   # 검은방
                        visited[ny][nx] = visited[y][x] + 1
                        q.append([ny, nx])


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())
    board = []
    visited = [[-1 for _ in range(n)] for _ in range(n)]

    for _ in range(n):
        l = list(map(int, input()))
        board.append(l)

    bfs()
    print(visited[n-1][n-1])

'''
        18405 경쟁적 전염

    '''


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")

    n, k = map(int, input().split())
    virus = []
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    data = []

    for i in range(n):
        virus.append(list(map(int, input().split())))

    s, x, y = map(int, input().split())

    for i in range(n):
        for j in range(n):
            if virus[i][j] != 0:
                data.append([i, j, virus[i][j], 0])

    data.sort(key=lambda x:x[2])
    q = deque(data)

    while q:
        cur_y, cur_x, cur_v, cur_s = q.popleft()

        if cur_s == s:
            print(virus[x-1][y-1])
            break

        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if (0 <= ny < n) and (0 <= nx < n):
                if virus[ny][nx] == 0:
                    virus[ny][nx] = cur_v
                    q.append([ny, nx, cur_v, cur_s+1])
                    
                    
'''
        18428 감시 피하기 - 연구소 문제와 비슷한 문제 

'''


# 벽 세우는 메서드
def make(cnt):
    global res
    if cnt == 3:
        if search():
            res = "YES"
        return

    for i in range(n):
        for j in range(n):
            if board[i][j] == 'X':
                board[i][j] = 'O'
                make(cnt+1)
                board[i][j] = 'X'

def search():
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'T':
                if check(i, j) == False:
                    return False
    return True

def check(i, j):
    for k in range(i, n):
        if board[k][j] == 'O':
            break
        elif board[k][j] == 'S':
            return False

    for k in range(i, -1, -1):
        if board[k][j] == 'O':
            break
        elif board[k][j] == 'S':
            return False

    for k in range(j, n):
        if board[i][k] == 'O':
            break
        elif board[i][k] == 'S':
            return False

    for k in range(j, -1, -1):
        if board[i][k] == 'O':
            break
        elif board[i][k] == 'S':
            return False
    return True

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")

    n = int(input())
    board = []
    for _ in range(n):
        board.append(input().split())
    res = ""

    make(0)
    if res == "YES":
        print("YES")
    else:
        print("NO")

        
'''
        1926 그림

'''

if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    board = []
    max_cnt = 0
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(n):
        board.append(list(map(int, input().split())))

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                if visited[i][j] == 0:
                    cnt_one = 1
                    q = deque()
                    q.append([i, j])
                    visited[i][j] = 1
                    while q:
                        y, x = q.popleft()
                        for k in range(4):
                            ny = y + dy[k]
                            nx = x + dx[k]
                            if (0 <= ny < n) and (0 <= nx < m):
                                if board[ny][nx] == 1:
                                    if visited[ny][nx] == 0:
                                        q.append([ny, nx])
                                        visited[ny][nx] = 1
                                        cnt_one += 1
                    cnt += 1
                    if max_cnt < cnt_one:
                        max_cnt = cnt_one



    print(cnt)
    print(max_cnt)
    
    
import sys
from collections import deque
'''
        1963 소수 경로 
        
        아이디어 아예 생각 안 남..
        
        1. 네 자리 수의 모든 소수 구함 
        2. 첫 숫자부터 각 자리수(4자리)에 0부터 9까지 넣어보면서 소수이면서 1000이상의 숫자를 찾는다. 
        3. 이 숫자가 타겟 넘버라면 리턴 
        => 완전탐색 + bfs 
        
'''

# 에라토스테네스의 체
def findPrimeNums():
    prime[0], prime[1] = False, False

    for i in range(2, 10000):
        if prime[i]:
            for j in range(2*i, 10000, i):
                prime[j] = False


def bfs(start, target):
    q = deque()
    q.append([start, 0])

    visited = [0 for _ in range(10000)]
    visited[start] = 1

    while q:
        now, cnt = q.popleft()

        if now == target:
            return cnt

        strNow = str(now)

        # 각 자리마다 0~9 숫자 넣어가면서 소수인지 확인
        for i in range(4):
            for j in range(10):
                tmp = int(strNow[:i] + str(j) + strNow[i+1:])

                if visited[tmp] == 0 and prime[tmp] and 1000 <= tmp:
                    q.append([tmp, cnt+1])
                    visited[tmp] = 1



if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())

    prime = [True] * 10000
    findPrimeNums()

    for _ in range(n):
        start, target = map(int, input().split())
        res = bfs(start, target)

        if res != None:
            print(res)
        else:
            print("Impossible")

            
import sys
from collections import deque
'''
        2251 물통
        
'''

def pour(x, y):
    if visited[x][y] == 0:
        visited[x][y] = 1
        q.append([x, y])

def bfs():
    while q:
        curA, curB = q.popleft()
        curC = c - curA - curB

        if curA == 0:
            res.append(curC)

        # a -> b
        water = min(curA, b-curB)
        pour(curA-water, curB+water)

        # a -> c
        water = min(curA, c-curC)
        pour(curA-water, curB)

        # b -> a
        water = min(curB, a-curA)
        pour(curA+water, curB-water)

        # b -> c
        water = min(curB, c-curC)
        pour(curA, curB-water)

        # c -> a
        water = min(curC, a-curA)
        pour(curA+water, curB)

        # c -> b
        water = min(curC, b-curB)
        pour(curA, curB+water)

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    a, b, c = map(int, input().split())
    visited = [[0 for _ in range(b+1)] for _ in range(a+1)]
    q = deque()
    res = []

    visited[0][0] = 1
    q.append([0, 0])
    bfs()

    res.sort()

    for i in res:
        print(i, end=' ')

'''
        9663 N-Queen 
        
        1. 퀸을 행을 기준으로 놓을지, 열을 기준으로 높을지 정하기 -> 행을 기준으로! 
        2. 행을 기준으로 놓는다고 정했기 때문에 같은 열에 퀸이 있는지 체크 
        3. 대각선에 퀸이 있는지 체크 
         - 퀸을 맨 윗 행부터 놓기 때문에 현재 행보다 윗 대각선만 체크 
         - 규칙 찾아내기: 퀸이 [3, 3]에 있다고 가정 (i, j)
           왼쪽 위 대각선: [0, 0], [1, 1], [2, 2] // 오른쪽 위 대각선: [2, 4], [1, 5] (x, y)
           abs(x-i) == abs(y-j)
        4. 퀸의 위치 1차원 배열에 저장: queen[i] = j -> i행 j열에 퀸 위치 
        => 시간초과
'''
def check(x):
    for i in range(x):
        if (queen[x] == queen[i]) or (abs(x - i) == abs(queen[x] - queen[i])):
            return False
    return True

def dfs(p):
    global cnt
    if p == n:
        cnt += 1
        return

    for i in range(n):  # [p][모든 열]에 퀸 위치시킴
        queen[p] = i
        if check(p):    # 현재 놓은 퀸의 위치가 가능하다면
            dfs(p+1)    # 다음 행에 퀸을 놓음


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())
    queen = [0 for _ in range(n)]
    cnt = 0

    dfs(0)
    print(cnt)
    
'''
        2589 보물섬 
        
'''



if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n, m = map(int, input().split())
    res = 0
    board = []
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    for _ in range(n):
        board.append(list(input()))

    for i in range(n):
        for j in range(m):
            tmp = 0
            if board[i][j] == 'L':
                q = deque()
                visited = [[0 for _ in range(m)] for _ in range(n)]
                visited[i][j] = 1
                q.append([i, j])

                while q:
                    y, x = q.popleft()
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if (0 <= ny < n) and (0 <= nx < m):
                            if board[ny][nx] == 'L':
                                if visited[ny][nx] == 0:
                                    visited[ny][nx] = visited[y][x] + 1
                                    q.append([ny, nx])
                                    res = max(res, visited[ny][nx])
    print(res-1)
