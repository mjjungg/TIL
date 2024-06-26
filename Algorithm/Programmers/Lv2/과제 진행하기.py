from collections import deque

def time_diff(t1, t2):
    h1 = int(t1.split(":")[0])
    m1 = int(t1.split(":")[1])
    
    h2 = int(t2.split(":")[0])
    m2 = int(t2.split(":")[1])
    
    return (h2 * 60 + m2)  - (h1 * 60 + m1)

def solution(plans):
    answer = []
    rest = deque()
    plans.sort(key=lambda x:x[1])
    
    for i in range(len(plans)-1):
        name, start, play = plans[i]
        nxt_name, nxt_start, nxt_play = plans[i+1]
        d = time_diff(start, nxt_start)
        
        if int(play) <= d:
            answer.append(name)
            d -= int(play)
            
            while 0 < d and rest:
                n, r = rest[0]
                
                if 0 <= d - r:
                    rest.popleft()
                    d -= r
                    answer.append(n)
                else:
                    rest[0][1] -= d
                    break
        else:
            rest.appendleft([name, int(play)-d])

    answer.append(plans[-1][0])
    for n, s in rest:
        answer.append(n)
        
           
    return answer
