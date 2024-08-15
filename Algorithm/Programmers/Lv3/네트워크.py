from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    
    for i in range(n):
        if visited[i] == 0:
            q = deque()
            
            answer += 1
            visited[i] = 1
            q.append(i)
            
            while q:
                now = q.popleft()
                
                for j in range(len(computers[now])):
                    if j != now and computers[now][j] == 1:
                        if visited[j] == 0:
                            visited[j] = 1
                            q.append(j)
                            
    return answer
