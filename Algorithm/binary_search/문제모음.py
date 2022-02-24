import sys
import math


''' 1072 게임
    처음 아이디어 : 
    lt = 1, rt = x로 초기화하고 
    승률을 계산한 값이 처음 승률과 다르다면 mid 값을 줄임 (간격을 줄임)
    ?? 승률은 계속 증가한다(계속 이기만 하기 때문) 그러면 간격은 대체 언제 넓힘 ??
    ?? rt 값을 어떻게 초기화할지도 모르겠음 ??
'''
def calculate(x, y):
    return math.trunc((y / x) * 100)


if __name__ == '__main__':
    sys.stdin = open("input.txt", "rt")
    x, y = map(int, input().split())
    res = -1
    now = calculate(x, y)

    lt = 1
    rt = x

    while lt <= rt:
        mid = (lt + rt) // 2

        if calculate != now:
            rt = mid - 1
            res = mid

    print(res)


########### 정답 #################

sys.stdin = open("input.txt", "rt")
x, y = map(int, input().split())
res = float('inf')
fir_rate = math.trunc((y / x) * 100)

lt = 1
rt = x

if 99 <= fir_rate or x == y:
    print(-1)
    exit()

while lt <= rt:
    mid = (lt + rt) // 2
    rate = math.trunc(((y+mid) / (x+mid)) * 100)

    # 승률이 오르지 않으면 게임 판 수를 늘린다
    if rate == fir_rate:
        lt = mid + 1
    # 승률이 오르면, 게임 판 수를 줄여보자 -> 최소 판 수를 구해야 하기 때문!
    else:
        res = mid
        rt = mid - 1

print(res)


'''
    1939 중량제한 
    처음 아이디어 : lt = c의 최소값, rt = c의 합으로 초기화
    search 함수 -> s에서 e으로 가는 중량의 최대값 구함 ?? --> 좀 이상함 
    search 함수의 결과값이 mid보다 작으면 lt 값 올림, 크면 rt 값 내리고 mid의 max값 답
    mid값과 뭘 비교해야할 지 모름 
    
    ---> bfs + binary search 문제 
    bfs : start -> end 로 이동하는 모든 경로에 weight 제한 통과하는지 검사
    binary : 해당 무게로 이동할 때 start -> end 까지 도착 가능한지 
'''

from collections import deque

def bfs(start, end, weight_case):
    queue = deque()
    queue.append(start)
    visited = [0 for _ in range(n+1)]

    visited[start] = 1

    while queue:
        y = queue.popleft()
        if y == end:
            return True
        for x, w in board[y]:
            if not visited[x] and weight_case <= w:
                visited[x] = 1
                queue.append(x)

    return False


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n, m = map(int, input().split())
    board = [[] for _ in range(n+1)]
    result = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        board[a].append([b, c])
        board[b].append([a, c])


    s, e = map(int, input().split())

    lt = 1
    rt = 1000000000

    while lt <= rt:
        mid = (lt + rt) // 2
        if bfs(s, e, mid):
            result = mid
            lt = mid + 1
        else:
            rt = mid - 1

    print(result)

    
    
import sys


'''
    2467 용액 
    처음 아이디어 : lt = 제일 작은 두 입력값의 합, rt = 제일 큰 두 입력값의 합
    mid값과 뭘 비교해야할 지 모름 
    
    lt, rt를 포인터로 생각하는 문제! 
    lt = 처음 인덱스 
    rt = 마지막 인덱스 라고 정의
    둘이 더한 값이 0보다 작다 -> lt + 1
    둘이 더한 값이 0ㅂ다 크다 -> rt - 1
    
'''


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())
    lst = list(map(int, input().split()))

    lt = 0
    rt = len(lst) - 1

    result = abs(lst[lt] + lst[rt])
    res_lt = lst[lt]
    res_rt = lst[rt]

    while lt < rt:
        mix = lst[lt] + lst[rt]

        if abs(mix) < result:
            result = abs(mix)
            res_lt = lst[lt]
            res_rt = lst[rt]

        if mix < 0:
            lt += 1
        else:
            rt -= 1

    print(res_lt, res_rt)


