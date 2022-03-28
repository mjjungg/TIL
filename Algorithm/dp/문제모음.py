import sys


'''
    9251 LCS

'''

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    s1 = input()
    s2 = input()

    n = len(s1)
    m = len(s2)

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:  # 맨 끝 글자가 같을 때
                dp[i][j] = dp[i-1][j-1] + 1     # s1, s2에서 각 문자를 추가하기전 값 + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # s1에 문자를 추가하기전 값, s2에 문자를 추가하기 전 값 중 큰 값

    print(dp[-1][-1])


'''
    11054 가장 긴 바이토닉 부분 수열
    
    증가하는 수열 길이 + 리스트 반대로 감소하는 수열 길이의 합이 가장 큰 지점 
    = 바이토닉 수열이면서 가장 긴 수열의 길이
    
    바이토닉 수열 : S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN 
    한 번에 바이토닉 수열 찾을 생각X -> 증가 수열 + 감소 수열 로 쪼개서 생각하기!
'''

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())

    lst = list(map(int, input().split()))

    increase = [1 for _ in range(n)]   # 증가하는 수열의 길이가 담긴 리스트
    decrease = [1 for _ in range(n)]   # 반대로 감소하는 수열의 길이가 담긴 리스트
    res = [0 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if lst[j] < lst[i]:
                increase[i] = max(increase[i], increase[j] + 1)


    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            if lst[j] < lst[i]:
                decrease[i] = max(decrease[i], decrease[j] + 1)



    for i in range(n):
        res[i] = increase[i] + decrease[i] - 1  # 중복 숫자빼줘야 해서 -1함

    print(max(res))
