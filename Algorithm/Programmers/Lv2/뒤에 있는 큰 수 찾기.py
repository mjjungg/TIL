from collections import deque

def solution(numbers):
    answer = [0 for _ in range(len(numbers))]
    numbers = [[i, numbers[i]] for i in range(len(numbers))]
    stack = []
    numbers = deque(numbers)
    stack.append(numbers.popleft())

    while numbers:
        idx, val = numbers.popleft()

        while stack and stack[-1][1] < val:
            answer[stack[-1][0]] = val
            stack.pop()
                
        stack.append([idx, val])    
            
    for i in range(len(stack)):
        answer[stack[i][0]] = -1
        
    return answer
