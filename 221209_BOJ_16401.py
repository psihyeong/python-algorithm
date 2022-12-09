# BOJ 16401번 과자 나눠주기

import sys

M, N = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

result = 0
# 과자의 길이가 될 수 있는 모든 경우의 수를 이분탐색
l, r = 1, max(arr)
while l <= r:
    mid = (l + r) // 2
    # mid 길이의 과자를 만들 수 있는 개수
    cookie_cnt = 0
    for num in arr:
        cookie_cnt += num // mid
    # 과자 개수가 M개 보다 크거나 같으면
    if cookie_cnt >= M:
        result = max(result, mid)
        # 더 큰 길이를 봐야지
        l = mid + 1
    else:
        # 더 작은 길이를 봐야지
        r = mid - 1

print(result)