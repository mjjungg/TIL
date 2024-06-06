def cal(t, m):
    res = 0
    
    if t == 0:  #다이아몬트로 캤을 때
        if m == 'diamond':
            res += 1
        elif m == 'iron':
            res += 1
        else:
            res += 1
    
    elif t == 1: # 철로 캤을 때
        if m == 'diamond':
            res += 5
        elif m == 'iron':
            res += 1
        else:
            res += 1
    else:   # 돌로 캤을 때
        if m == 'diamond':
            res += 25        
        elif m == 'iron':
            res += 5
        else:
            res += 1
            
    return res
       
def solution(picks, minerals):
    answer = 0
    minerals = minerals[:sum(picks)*5]
    infos = []  # infos = [[a, b, c], [d, e, f]]
                # [a, b, c] = 다이아몬드로 캤을 때 피로도, 철로 캤을 때 피로도, 돌로 캤을 때 피로도
    
    start = 0
    
    while True:
        tmp = [0, 0, 0]
        
        if start + 5 <= len(minerals):
            five_minerals = minerals[start:start+5]
            
            for i in range(3):
                for j in range(5):
                    tmp[i] += cal(i, five_minerals[j])
                    
            infos.append(tmp)
            start += 5
        
        else:
            last_minerals = minerals[start:len(minerals)]
            
            for i in range(3):
                for j in range(len(last_minerals)):
                    tmp[i] += cal(i, last_minerals[j])
            
            infos.append(tmp)
            break
    
    # 피로도 정렬 -> 돌로 깼을 때 피로도가 가장 높은 광물을 다이아몬트로 캐기
    infos.sort(key=lambda x:(x[2], x[1], x[0]))
    
    for i in range(3):
        for _ in range(picks[i]):
            if infos:
                answer += infos.pop()[i]
            else:
                break
                
    return answer
