from collections import defaultdict

def solution(record):
    answer = []
    d = defaultdict(str)
    
    for i in range(len(record)):
        s = record[i].split(" ")
        
        if s[0] == "Enter":
            d[s[1]] = s[2]
            
        elif s[0] == "Change":
            d[s[1]] = s[2]
    
    for i in record:
        s = i.split(" ")
        
        if s[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(d[s[1]]))
        elif s[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(d[s[1]]))
        
    return answer
