def solution(msg):
    answer = []
    d = {}
    max_len = 1
    max_value = 27
    for i in range(65, 91):
        d[chr(i)] = i - 64

    while msg:   
        for i in range(max_len, -1, -1):
            tmp = msg[:i]
            if tmp in d:
                answer.append(d[tmp])
                if i < len(msg):
                    d[msg[:i+1]] = max_value
                    max_value += 1
                    max_len = max(max_len, len(msg[:i+1]))
                    
                msg = msg[i:]
                break
                
    return answer
