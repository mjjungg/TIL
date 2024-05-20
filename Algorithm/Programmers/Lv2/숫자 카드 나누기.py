import math

def solution(arrayA, arrayB):
    answer = 0
    
    gcd_a = arrayA[0]
    
    for i in range(1, len(arrayA)):
        gcd_a = math.gcd(gcd_a, arrayA[i])
    
    tmp_a = set()
    
    for i in range(1, int(gcd_a ** 0.5) + 1):
        if gcd_a % i == 0:
            tmp_a.add(gcd_a // i)
    
    for i in tmp_a:
        for j in arrayB:
            if j % i == 0:
                break
        else:
            answer = max(answer, i)
    
    gcd_b = arrayB[0]
    
    for i in range(1, len(arrayB)):
        gcd_b = math.gcd(gcd_b, arrayB[i])
    
    tmp_b = set()
    
    for i in range(1, int(gcd_b ** 0.5) + 1):
        if gcd_b % i == 0:
            tmp_b.add(gcd_b // i)
    
    for i in tmp_b:
        for j in arrayA:
            if j % i == 0:
                break
        else:
            answer = max(answer, i)
            
    return answer
