from itertools import product

def solution(word):
    answer = 0
    cases = []
    
    for i in range(1, 6):
        for case in product(['A', 'E', 'I', 'O', 'U'], repeat = i):
            cases.append(''.join(case))
    cases.sort()
    
    return cases.index(word) + 1
