import math
from collections import defaultdict

def solution(fees, records):
    answer = []
    d = defaultdict(int)
    stack = []
    
    for record in records:
        l = record.split(" ")
        
        if l[2] == 'IN':
            stack.append([l[0], l[1]])
        else:            
            for i in range(len(stack)):
                if stack[i][1] == l[1]:
                    time_in = stack[i][0].split(":")
                    time_out = l[0].split(":")
                        
                    hour = int(time_out[0]) - int(time_in[0])
                    minute = int(time_out[1]) - int(time_in[1])
                    
                    diff = hour * 60 + minute
                    
                    d[stack[i][1]] += diff
                    stack.pop(i)
                    break
                    
    for i in stack:
        l = "23:59"
        cost = 0
        time_in = i[0].split(":")
        time_out = l.split(":")
            
        hour = int(time_out[0]) - int(time_in[0])
        minute = int(time_out[1]) - int(time_in[1])

        diff = hour * 60 + minute
            
        d[i[1]] += diff
        
    d = sorted(d.items(), key=lambda x:x[0])
    
    for k, v in d:
        cost = 0
        
        if v <= fees[0]:
            cost += fees[1]
        else:
            cost = fees[1] + math.ceil((v - fees[0]) / fees[2]) * fees[3]
            
        answer.append(cost)
    
    return answer
