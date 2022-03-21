import sys

sys.setrecursionlimit(10**6)


'''
    11725 트리의 부모 찾기
    이중 배열에 이중으로 vertex 저장
    1 = [2, 4, 5]   # 1-2,4,5
    2 = [1, 3]
    1번부터 dfs 시작 -> 방문한 경우 pass(이미 부모 노드 설정함)
    방문하지 X 경우 부모 노드 저장 
    
    ※ [[0 for _ in range(n+1)] for _ in range(n+1)] 와
      [[] for _ in range(n+1)] 메모리 크기 차이 남!!
    
'''


def dfs(start):
    for i in board[start]:
        if visited[i] == 0:
            res[i] = start
            visited[i] = 1
            dfs(i)

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())

    board = [[] for _ in range(n+1)]
    res = [0 for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]

    visited[1] = 1
    for _ in range(n-1):
        a, b = map(int, input().split())
        board[a].append(b)
        board[b].append(a)

    dfs(1)

    for i in range(2, n+1):
        print(res[i])
