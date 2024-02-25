from itertools import permutations

def solution(k, dungeons):
    answer = 0
    cases = list(permutations([i for i in range(len(dungeons))]))
    
    for case in cases:
        cpy_k = k
        tmp = 0
        for i in range(len(case)):
            idx = case[i]
            
            if cpy_k >= dungeons[idx][0]:
                cpy_k -= dungeons[idx][1]
                tmp += 1
            
            if cpy_k <= 0:
                break
                
        answer = max(answer, tmp)
        
    return answer
