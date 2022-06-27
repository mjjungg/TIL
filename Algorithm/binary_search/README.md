# binary search

## **이분 탐색이란?**

오름차순 또는 내림차순으로 정렬된 수열에서 **특정 값의 위치를 찾는 알고리즘**이다. 탐색 대상을 반으로 줄여나가므로 선형 탐색보다 빠르게 검색할 수 있다.  시간복잡도는 ***O(logn)***이다.

*예) 숫자 M이 정렬된 상태에서 몇 번째에 위치하는 지를 묻는 문제*

수열의 중간 위치에서부터 탐색을 시작한다.

```python
lower = 0
upper = N-1

while lower <= upper:
    mid = (lower + upper) // 2
    if lst[mid] == M:
        print(mid + 1)
        break
    elif lst[mid] < M:
        lower = mid + 1
    else:
        upper = mid - 1
```

> 💡 **답이 어떤 범위 내에 존재할 때 이분 탐색을 사용한다**.
> 

1. 탐색할 데이터가 1,000만을 넘어가면 이진 탐색 고려! 
2. 탐색할 데이터가 정렬되어 있어야 함 

## 최장수열 공식

```python
def search(lst, target):
    start, end = 0, len(lst)-1

    while start <= end:
        mid = (start + end) // 2

        if lst[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())
    num_lst = list(map(int, input().split()))

    results = [num_lst[0]]
    for i in range(1, len(num_lst)):
        if results[-1] < num_lst[i]:
            results.append(num_lst[i])
        else:
            k = search(results, num_lst[i])
            results[k] = num_lst[i]

    print(len(results))
```

results 라는 리스트 하나 생성하고, 0번째값을 입력받은 리스트의 첫 번째값으로 초기화한다.

for문을 돌면서 만일, 입력받은 리스트의 현재 값이 result의 마지막 값보다 크다면 조건을 만족한 것이므로 바로 result에 리스트의 현재값을 추가한다.

작다면, binary search를 통해 들어갈 자리를 구하고, results[결과값]에 현재 리스트의 값을 채운다.
