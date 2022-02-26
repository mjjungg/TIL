'''
  greedy -> 값의 결과값이 최대값 or 최소값 묻는 문제가 많음 
'''





'''
    1026 보물 
    
    최대값 * 최소값이 되도록 a와 b를 정렬한다.
'''


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())
    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))
    result = 0

    a_lst.sort(reverse=True)
    b_lst.sort()

    for i in range(n):
        result += a_lst[i] * b_lst[i]
    print(result)
    
    
    
    
    
'''
    1789 수들의 합
    
    1부터 계속 더해나가다가 더한 값이 s보다 클 때 cnt-1해줌  
'''


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())
    sum = 0
    cnt = 0

    for i in range(1, n):
        sum += i
        cnt += 1

        if sum > n:
            cnt -= 1
            break

    print(cnt)
