# BOJ 1912번 연속합
# 다이나믹 프로그래밍

N = int(input())
# 인덱스 위치까지의 연속합 중 최댓값을 저장하는 리스트
dp = list(map(int,input().split()))

# 1번 인덱스부터
for i in range(1,N):
    # 점화식
    if dp[i-1]+dp[i] > dp[i]:
        dp[i] = dp[i] + dp[i-1]

print(max(dp))