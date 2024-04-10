import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)    
    
    while scoville:
        min_val1 = heapq.heappop(scoville)
        
        if K <= min_val1:
            return answer
        
        if len(scoville) == 0:
            return -1
        
        min_val2 = heapq.heappop(scoville)
             
        s = min_val1 + (min_val2 * 2)
        heapq.heappush(scoville, s)
        answer += 1
                  
    return -1
