from collections import deque

def solution(number, k):
    answer = ''
    lst = []
    number = deque(list(number))
    lst.append(number.popleft())
    
    while number:       
        if 0 < k:
            if lst[-1] < number[0]:
                while lst and lst[-1] < number[0] and 0 < k:
                    lst.pop()
                    k -=1
                lst.append(number.popleft())
            else:
                lst.append(number.popleft())               
        else:
            break

    for i in range(k):
        lst.pop()
    
    for i in lst:
        answer += str(i)
    
    for i in number:
        answer += str(i)
       
    return answer
