# BOJ 2156번 포도주 시식
# 다이나믹 프로그래밍

N = int(input())
# 최대 배열
arr = [0] * 10000
for i in range(N):
    arr[i] = int(input())

# 초기값
dp = [0] * 10000
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[2] + arr[0], arr[2] + arr[1], dp[1])

for i in range(3,N):
    # 점화식
    dp[i] = max(arr[i] + dp[i - 2], arr[i] + arr[i - 1] + dp[i - 3], dp[i - 1])

print(max(dp))