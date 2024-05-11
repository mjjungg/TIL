from itertools import permutations

def check(n):
    if n in (0, 1):
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True

def solution(numbers):
    numbers = [i for i in numbers]
    s = set()
    
    for i in range(1, len(numbers)+1):
        lst = list(permutations(numbers, i))
        
        for j in lst:
            if check(int(''.join(j))):
                s.add(int(''.join(j)))
                
    return len(s)
