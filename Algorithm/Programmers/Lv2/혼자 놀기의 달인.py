def solution(cards):
    answer = 0
    visited = [0 for _ in range(len(cards)+1)]
    result = []
    
    for i in range(len(cards)):
        if visited[cards[i]] == 0:
            card = cards[i]
            idx = i
            cnt = 1
            visited[card] = 1
            
            while True:   
                idx = card - 1
                card = cards[idx]   
                
                if visited[card] == 0:
                    cnt += 1
                    visited[card] = 1
                else:
                    break
                    
            result.append(cnt)
    result.sort()

    if len(result) < 2:
        return 0
    else:
        return result[-1] * result[-2]
