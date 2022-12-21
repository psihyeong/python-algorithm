# BOJ 22862번 가장 긴 짝수 연속한 부분 수열 (large)

import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

res = 0
end = 0
even, odd = 0, 0

for start in range(N):
    while end < N and K >= odd:
        if arr[end] % 2:
            odd += 1
        else:
            even += 1
        end += 1

    if odd == K+1:
        odd -= 1
        end -= 1

    res = max(res, even)

    if arr[start] % 2:
        odd -= 1
    else:
        even -= 1


print(res)
