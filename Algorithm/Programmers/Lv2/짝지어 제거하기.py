from collections import deque

def solution(s):
    answer = -1
    s = deque(s)
    p = []
    
    if len(s) % 2 == 1:
        return 0
    
    else:
        while s:
            now = s.pop()
            if len(p) == 0:
                p.append(now)
            else:
                if p[-1] == now:
                    p.pop()
                else:
                    p.append(now)

        if len(p) == 0:
            return 1
        else:
            return 0
