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
