from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    s = 0
    
    while q:
        now = bridge.popleft()
        s -= now
        
        if len(bridge) + 1 <= bridge_length and s+ q[0] <= weight:
            n = q.popleft()
            bridge.append(n)
            s += n
        else:
            bridge.append(0)
    
        answer += 1
    
    for i in range(len(bridge)-1, -1, -1):
        if bridge[i] != 0:
            answer += i + 1
            break
            
    return answer
