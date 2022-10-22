# BOJ 11053번 가장 긴 증가하는 부분 수열
# 다이나믹 프로그래망

N = int(input())
arr = list(map(int,input().split()))
# arr[i]를 마지막 원소로 가질 때 가장 긴 증가하는 부분 수열의 길이
dp = [1 for _ in range(N)]
for i in range(1,N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j]+1,dp[i])
print(dp)