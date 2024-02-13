from collections import deque

def check(s):
    stack = []
    
    for i in s:
        if i in ('[', '(', '{'):
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            
            if i == ']':
                if stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            elif i == '}':
                if stack[-1] != '{':
                    return False
                else:
                    stack.pop()
            else:
                if stack[-1] != '(':
                    return False
                else:
                    stack.pop()
    if 0 < len(stack):
        return False
    
    return True

def solution(s):
    answer = 0
    q = deque(s)
    
    for i in range(len(s)):
        q.append(q.popleft())
        if check(q):
            answer += 1
            
    return answer
