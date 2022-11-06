# BOJ 1495번 기타리스트
# 다이나믹 프로그래밍

N, S, M = map(int, input().split())
V = list(map(int, input().split()))
# 곡별 볼륨값 리스트
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
# 초기값
dp[0][S] = 1

# 곡의 개수 만큼
for i in range(1,N+1):
    for j in range(M+1):
        # 볼륨 조절 가능하면
        if dp[i-1][j] != 0:
            if 0 <= j+V[i-1] <= M:
                dp[i][j+V[i-1]] = 1
            if 0 <= j-V[i-1] <= M:
                dp[i][j-V[i-1]] = 1

result = -1
# 최댓값 찾기
for i in range(M,-1,-1):
    if dp[N][i] == 1:
        result = i
        break

print(result)