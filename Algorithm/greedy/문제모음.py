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

    
    
'''
    10610 30 
    
    아이디어 : 받은 수를 스트링으로 쪼갠 후 나올 수 있는 모든 순서의 조합(순열) 구함
    이것 중에서 30으로 나눠지는 가장 큰 수 구하려 함..
    -> 알 수 없는 런타임에러 발생..
    
    ###########정답###########
    30의 배수가 되는 조건 살펴보기
    
    !! 애초부터 스트링값으로 받아라 
    0. 수를 내림차순으로 정렬 -> 최대값 
    1. 0이 없다면 탈락
    2. 각 자리 숫자 합이 3으로 나눠떨어지지 않으면 탈락
    
'''
    
if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = input()
    n = sorted(n, reverse=True)

    if '0' not in n:
        print(-1)
    else:
        sum = 0
        for i in n:
            sum += int(i)

        if sum % 3 != 0:
            print(1)
        else:
            print(''.join(n))
