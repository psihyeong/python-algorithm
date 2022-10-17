# BOJ 1932번 정수 삼각형
# 다이나믹 프로그래밍

N = int(input())
# 해당 위치에 최대가 되는 경로
dp = [list(map(int,input().split())) for _ in range(N)]

# 2층부터
for i in range(1,N):
    for j in range(len(dp[i])):
        # 맨 왼쪽 수는 하나의 경로
        if j == 0:
            dp[i][j] += dp[i-1][j]
        # 맨 오른쪽 수도 마찬가지
        elif j == len(dp[i])-1:
            dp[i][j] += dp[i-1][j-1]
        # 그 외의 수는 두가지 경로 중 최댓값을 선택
        else:
            dp[i][j] = max(dp[i-1][j-1]+dp[i][j], dp[i-1][j]+dp[i][j])

# 마지막 층의 최댓값 출력
print(max(dp[N-1]))
