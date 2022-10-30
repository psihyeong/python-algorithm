# BOJ 9461번 파도반 수열
# 다이나믹 프로그래밍

dp = [0 for _ in range(101)]
# 초기값
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(98):
    # 점화식
    dp[i+3] = dp[i] + dp[i+1]

for _ in range(int(input())):
    N = int(input())
    print(dp[N])