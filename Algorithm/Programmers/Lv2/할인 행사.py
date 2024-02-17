import copy

def solution(want, number, discount):
    answer = 0
    n = len(want)
    d = dict()
    
    for i in range(n):
        d[want[i]] = number[i]
    
    
    for i in range(len(discount) - 10 + 1):
        cpy_d = copy.deepcopy(d)
        tmp = discount[i:i+10]
        flg = 0
        
        for item in tmp:
            if item in cpy_d and 0 < cpy_d[item]:
                cpy_d[item] -= 1
            else:
                flg = 1
                break

        if flg == 0:
            answer += 1
            
    return answer
