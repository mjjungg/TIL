from collections import deque

def solution(priorities, location):
    answer = 0
    max_value = max(priorities)
    priorities = [(priorities[i], i) for i in range(len(priorities))]
    q = deque(priorities)

    while q:
        v, idx = q.popleft()
        
        if v < max_value:
            q.append((v, idx))
            continue
        
        answer += 1
        
        if q:
            max_value = max([i[0] for i in q])
        
        if idx == location:
            break
    
    return answer
