from collections import deque

def solution(queue1, queue2):
    answer = 0
    s1 = sum(queue1)
    s2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    len_q1 = len(queue1)
    
    
    while s1 != s2:
        if s1 <= s2:
            now = queue2.popleft()
            queue1.append(now)
            
            s1 += now
            s2 -= now
            
        else:
            now = queue1.popleft()
            queue2.append(now)
            
            s1 -= now
            s2 += now
    
        answer += 1
        
        if len_q1 * 3 < answer:
            return -1
        
    return answer
