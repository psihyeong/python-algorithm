# BOJ 15988번 1,2,3 더하기 3
# 다이나믹 프로그래밍

# 정수 n을 1,2,3의 합으로 나타내는 방법의 수
dp = [0 for _ in range(1000001)]
# 초기값
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3,1000001):
    # 점화식
    dp[i] = dp[i-1]%1000000009 + dp[i-2]%1000000009 + dp[i-3]%1000000009

N = int(input())
for _ in range(N):
    print(dp[int(input())]%1000000009)