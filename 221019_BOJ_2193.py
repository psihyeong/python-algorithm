# BOJ 2193번 이친수
# 다이나믹 프로그래밍

N = int(input())
# 인덱스 자리수 중 끝자리가 [0,1]로 끝나는 이친수의 개수
dp = [[0,0] for _ in range(N)]
# 이친수 '1'의 경우
dp[0][1] = 1

# 점화식
for i in range(1,N):
    dp[i][0] = dp[i-1][0]+dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(sum(dp[N-1]))