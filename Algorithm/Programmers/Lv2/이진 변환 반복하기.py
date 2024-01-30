def solution(s):
    answer = [0, 0]

    while s != '1':
        new_s = ''
        
        for i in s:
            if i != '0':
                new_s += i
            else:
                answer[1] += 1
                
        n = len(new_s)
        s = bin(n)[2:]
        answer[0] += 1
        
    return answer
