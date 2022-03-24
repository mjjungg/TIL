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
