def solution(numbers):
    answer = []
    
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            s_num = bin(num)[2:]
            idx = s_num[::-1].find('0')
            
            if idx == -1:
                s_num = '0' + s_num
                idx = s_num[::-1].find('0')
            
            idx = len(s_num) - 1 - idx
            s_num = s_num[:idx] + '1' + s_num[idx+1:]
            
            for i in range(idx+1, len(s_num)):
                if s_num[i] == '1':
                    s_num = s_num[:i] + '0' + s_num[i+1:]
                    break
                    
            answer.append(int(s_num, 2))
            
    return answer
