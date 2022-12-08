# BOJ 1654번 랜선 자르기

import sys

N, K = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
result = 0

# 랜선의 길이가 될 수 있는 모든 경우를 이분탐색
l, r = 1, max(arr)
while l <= r:
    # mid 길이로
    mid = (l + r) // 2
    # 만들 수 있는 랜선의 개수가
    line_cnt = 0
    for num in arr:
        line_cnt += num//mid

    # K개 보다 크거나 같으면
    if line_cnt >= K:
        result = max(result, mid)
        # 더 큰 길이를 봐야지
        l = mid + 1
    else:
        # 더 작은 길이를 봐야지
        r = mid - 1

print(result)