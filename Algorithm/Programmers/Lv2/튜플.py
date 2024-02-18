def solution(s):
    answer = []
    s = s.split('},{')
    s[0] = s[0][2:]
    s[-1] = s[-1][:-2]
    s.sort(key=len)
    
    for i in range(len(s)):
        s[i] = s[i].split(',')
    
    for numbers in s:
        for i in range(len(numbers)):
            if int(numbers[i]) not in answer:
                answer.append(int(numbers[i]))
                
    return answer
