def solution(brown, yellow):
    answer = [0, 0]
    total = brown + yellow
    
    for i in range(3, total // 2 + 1):
        if total % i == 0:
            w = i
            h = total // w
            
            if yellow == (w - 2) * (h - 2):
                answer[0] = max(w, h)
                answer[1] = min(w, h)
                break
                
    return answer
