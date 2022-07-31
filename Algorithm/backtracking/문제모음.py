import sys
from collections import deque
'''
        15649 N과 M
'''

def dfs():
    if len(res) == m:
        print(' '.join(map(str, res)))
        return

    for i in range(1, n+1):
        if i not in res:
            res.append(i)
            dfs()
            res.pop()


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n, m = map(int, input().split())
    res = []
    dfs()


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

