from collections import deque

def solution(s):
    answer = True
    s = deque(s)
    stack = []
    
    while s:
        now = s.popleft()
        if now == '(':
            stack.append(now)
        else:
            if len(stack) == 0:
                return False
            
            stack.pop()
            
    if len(stack) > 0:
        return False
    
    return True

'''
  stack에 넣고 빼지 않고 정수로 관리하면 시간복잡도 줄어듦!!
  cnt += 1
  cnt -= 1
  로 stack append, pop 대체가능!
'''
