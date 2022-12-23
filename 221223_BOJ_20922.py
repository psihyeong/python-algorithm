# BOJ 20922번 겹치는 건 싫어

import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

end = 0         # 투포인터 변수
dp = [0 for _ in range(max(arr)+1)]     # 현재 부분 수열의 각 원소 포함 수를 저장하는 dp
leng, res = 0, 0        # 부분 수열의 길이, 결과값

# 투포인터 시작
for start in range(N):
    # end 값 이동
    while end < N:
        # 현재 수열에서 해당 원소가 들어갈 수 없는 경우 반복문 종료
        if dp[arr[end]] == K:
            break
        dp[arr[end]] += 1
        leng += 1
        end += 1

    res = max(res, leng)

    # start 값 이동
    dp[arr[start]] -= 1
    leng -= 1

print(res)


# # 시간초과 코드, max를 계속 돌리는게 문제인듯
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