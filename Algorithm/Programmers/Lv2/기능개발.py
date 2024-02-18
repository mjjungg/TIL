def solution(progresses, speeds):
    answer = []
    pre_day = 0
    cnt = 0
    
    for i in range(len(progresses)):
        rest = 100 - progresses[i]
        day = rest // speeds[i]
            
        if 0 < rest % speeds[i]:
            day += 1
        
        if day <= pre_day:
            cnt += 1
        else:
            if pre_day != 0:
                answer.append(cnt)
            cnt = 1
            pre_day = day
            
    answer.append(cnt)
    
    return answer
