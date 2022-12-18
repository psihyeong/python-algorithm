# BOJ 1806번 부분합

import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

result = sys.maxsize
interval_sum = 0        # 부분합
end = 0                 # 투포인터 변수

for start in range(N):
    # 부분합이 S 이상이 될 때까지 end 값 증가
    while interval_sum < S and end < N:
        interval_sum += arr[end]
        end += 1
    # 부분합이 S이상이면 수열 길이 최신화
    if interval_sum >= S:
        result = min(result, end-start)

    # 다음 수열을 찾기 위해 start 값 증가
    interval_sum -= arr[start]

if result == sys.maxsize:
    result = 0

print(result)
