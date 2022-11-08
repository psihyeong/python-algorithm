# BOJ 2579번 계단 오르기
# 다이나믹 프로그래밍

N = int(input())
stair = [int(input()) for _ in range(N)]
# 인덱스 번 계단에서 얻을 수 있는 최대 점수
dp = [0 for _ in range(N)]
# 초기값
dp[0] = stair[0]
if N >= 2:
    dp[1] = stair[0]+stair[1]
if N >= 3:
    dp[2] = max(stair[0]+stair[2], stair[1]+stair[2])

for i in range(3, N):
    # 점화식
    dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])

print(dp[N-1])