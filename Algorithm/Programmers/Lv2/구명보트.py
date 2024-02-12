from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    
    while people:
        start = people[0]
        end = people[-1]
        
        if start + end <= limit:
            people.popleft()
            
        people.pop()
        answer += 1
        
        if len(people) == 1:
            answer += 1
            break
            
    return answer
