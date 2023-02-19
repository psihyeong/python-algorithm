# BOJ 11053번 가장 긴 증가하는 부분 수열
# 다이나믹 프로그래망

N = int(input())
arr = list(map(int,input().split()))
# arr[i]를 마지막 원소로 가질 때 가장 긴 증가하는 부분 수열의 길이
dp = [1 for _ in range(N)]
for i in range(1,N):
    # i번째 수 보다 전에 있는 j번째 수에 대해서
    for j in range(i):
        # i번째 수가 j번째 수보다 크다면
        if arr[j] < arr[i]:
            # 최장 순열을 갱신
            # 모든 이전 j번째 수를 보기 때문에
            # 그 순열들 중 가장 긴 증가하는 부분 순열을 가진 순열이
            # i번째 수를 포함한 최장 순열로 갱신이 된다.
            dp[i] = max(dp[j]+1,dp[i])
print(max(dp))