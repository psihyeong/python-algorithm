# BOJ 15486번 퇴사 2
# 다이나믹 프로그래밍

N = int(input())
schedule =[[0,0]] + [list(map(int,input().split())) for _ in range(N)]
# 인덱스 날짜에 상담이 끝나고 받는 최대 금액
dp = [0 for _ in range(N+51)]
for i in range(1,N+1):
    length = schedule[i][0] - 1
    # i일의 기대수익과 현재수입을 비교해서 최댓값 갱신
    dp[i] = max(dp[i-1],dp[i])
    # i일의 상담을 수주했을 때,
    # 상담이 끝난 날의 기존 최대금액과 전날까지의 최대금액 + 수임료와 비교해서 최댓값 갱신
    dp[i+length] = max(dp[i-1] + schedule[i][1], dp[i+length])
print(dp[N])