# BOJ 2293번 동전 1
# 다이나믹 프로그래밍

n, k = map(int, input().split())
# 동전의 종류 리스트
coins = [int(input()) for _ in range(n)]
# 인덱스 가치를 만드는 데 가능한 경우의 수 리스트
dp = [1] + [0 for _ in range(k)]

# 동전들
for i in coins:
    # k의 가치까지
    for j in range(1, k+1):
        # 해당 동전을 더해도 k를 초과하지 않으면
        if j - i >= 0:
            # 경우의 수 추가
            dp[j] += dp[j-i]
print(dp[k])