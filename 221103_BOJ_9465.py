# BOJ 9465번 스티커
# 다이나믹 프로그래밍

for _ in range(int(input())):
    N = int(input())
    # 해당 좌표의 스티커 점수 최댓값
    dp = [list(map(int,input().split())) for _ in range(2)]
    # 초기값
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]

    for i in range(2,N):
        # 가능한 경우의 수 중
        # 최댓값 갱신
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][N-1], dp[1][N-1]))