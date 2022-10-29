# BOJ 11055번 가장 큰 증가 부분 수열
# 다이나믹 프로그래밍

N = int(input())

arr = list(map(int,input().split()))
# arr[i]를 마지막 원소로 가질 때 가장 큰 증가하는 부분 수열의 크기
# 합이기 때문에 초기값은 자기 자신의 수
dp = arr[::]
for i in range(1,N):
    # i번째 전의 모든 j번째 수 중
    for j in range(i):
        # 증가하는 수열이면
        if arr[i] > arr[j]:
            # 최댓값 갱신
            dp[i] = max(dp[i], dp[j]+arr[i])

print(max(dp))
