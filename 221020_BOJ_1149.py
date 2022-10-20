# BOJ 1149번 RGB거리
# 다이나믹 프로그래밍

N = int(input())
# 규칙을 만족하는 집을 칠할 때 드는 최소 비용
dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(1,N):
    # i 번째 집을
    # 빨간색을 칠할 때 최소 비용
    dp[i][0] += min(dp[i - 1][1], dp[i - 1][2])
    # 초록색,
    dp[i][1] += min(dp[i - 1][0], dp[i - 1][2])
    # 파란색,
    dp[i][2] += min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[N-1]))