from collections import deque

def solution(order):
    answer = 0
    stack = []
    now = 1
    
    for i in order:
        while now < i:
            stack.append(now)
            now += 1
            
        if stack and stack[-1] == i:
            stack.pop()
            answer += 1
            
        elif now == i:
            answer += 1
            now += 1
        
        elif i < now and i < stack[-1]:
            break
                
    return answer
