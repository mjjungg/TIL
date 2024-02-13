from collections import Counter

def solution(k, tangerine):
    answer = 0
    c = Counter(tangerine)
    c = sorted(c.items(), key=lambda x:x[1], reverse=True)
    
    for key, val in c:
        k -= val
        answer += 1
        if k <= 0:
            break
            
    return answer
