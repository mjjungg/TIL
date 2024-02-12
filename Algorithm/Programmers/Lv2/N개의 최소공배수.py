import math

def solution(arr):
    answer = 0
    
    arr.sort()
    a = arr[0]
    
    for i in range(1, len(arr)):
        gcd = math.gcd(a, arr[i])
        answer = gcd * (a // gcd) * (arr[i] // gcd)
        a = answer
    
    return answer
