def solution(numbers):
    answer = ''
    lst = []
    
    for number in numbers:
        lst.append([number, str(str(number) * (5 - (len(str(number)))))[:4]])
    
    lst.sort(key=lambda x:x[1], reverse=True)
    
    for i in lst:
        answer += str(i[0])
    
    if answer[0] == '0':
        return '0'
    
    return answer
