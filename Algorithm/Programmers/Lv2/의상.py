from collections import defaultdict

def solution(clothes):
    answer = 1
    d = defaultdict(int)
    
    for value, key in clothes:
        d[key] += 1
    
    for i in d:
        d[i] += 1
        answer *= d[i]
        
    return answer - 1
