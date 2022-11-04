# BOJ 2302번 극장 좌석
# 다이나믹 프로그래밍

N = int(input())
M = int(input())
vip = [int(input()) for _ in range(M)]

# 좌석의 개수에 따른 가능한 경우의 수
dp = [0 for _ in range(N+1)]
# 초기값
dp[0] = 1
if N >= 1:
    dp[1] = 1
if N >= 2:
    dp[2] = 2

for i in range(3, N+1):
    # 점화식
    dp[i] = dp[i-1] + dp[i-2]

result = 1
# vip가 있으면
if M > 0:
    # 전 vip 좌석
    tmp = 0
    # vip 사이 좌석의 개수의 가능한 경우의 수를 곱해주기
    for j in range(M):
        result *= dp[vip[j]-1-tmp]
        tmp = vip[j]
    # 마지막 vip좌석부터 끝좌석까지 경우의 수를 곱해주기
    result *= dp[N-tmp]
# vip가 없을 경우
else:
    result = dp[N]

print(result)