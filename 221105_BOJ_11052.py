# BOJ 11052번 카드 구매하기
# 다이나믹 프로그래밍

N = int(input())
# 인덱스 개가 들어있는 카드팩 가격
price = [0] + list(map(int, input().split()))
# 인덱스 개의 카드를 구매하는 최대 가격
dp = [0 for _ in range(N+1)]


for i in range(1,N+1):
    for k in range(1,i+1):
        # 점화식
        dp[i] = max(dp[i], dp[i-k] + price[k])

print(dp[i])