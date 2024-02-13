def solution(elements):
    n = len(elements)
    sums = set(elements)    
    elements *= 2
    
    for i in range(2, n+1):
        for j in range(n):
            tmp = tuple(elements[j:j+i])
            sums.add(sum(tmp))
        
    return len(sums)
