from collections import Counter

def solution(topping):
    answer = 0
    s = set()
    c = Counter(topping)
    
    for i in topping:
        c[i] -= 1
        s.add(i)
        
        if c[i] == 0:
            c.pop(i)
        
        if len(c) == len(s):
            answer += 1
        
    return answer
