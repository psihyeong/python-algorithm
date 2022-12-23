# BOJ 20922번 겹치는 건 싫어

import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

end = 0
dp = [0 for _ in range(max(arr)+1)]
leng, res = 0, 0

for start in range(N):
    while end < N:
        if dp[arr[end]] == K:
            break
        dp[arr[end]] += 1
        leng += 1
        end += 1

    res = max(res, leng)
    dp[arr[start]] -= 1
    leng -= 1

print(res)



# # 시간초과 코드
# end = 0
# dp = [0 for _ in range(max(arr)+1)]
# leng, res = 0, 0
#
# for start in range(N):
#
#     while end < N and max(dp) <= K:
#         dp[arr[end]] += 1
#         leng += 1
#         end += 1
#
#     res = max(res, leng-1)
#     dp[arr[start]] -= 1
#     leng -= 1
#
# print(res)