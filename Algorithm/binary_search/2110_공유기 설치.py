def count(lst, case):
    cnt = 1
    end_point = lst[0]

    for i in range(1, len(lst)):
        if case <= lst[i] - end_point:
            cnt += 1
            end_point = lst[i]
    return cnt

if __name__ == '__main__':
    n, c = map(int, input().split())
    lst = []
    res = -1
    for _ in range(n):
        lst.append(int(input()))

    lst.sort()
    lt = 1
    rt = lst[-1] - lst[0] 
    
    while lt <= rt:
        mid = (lt + rt) // 2
        cnt = count(lst, mid)

        if cnt < c:    # 간격 좁히기
            rt = mid - 1
        else:   # 간격 넓히기
            lt = mid + 1
            res = mid
    print(res)
