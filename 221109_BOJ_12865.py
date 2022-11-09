# BOJ 12865번 평범한 배낭
# 다이나믹 프로그래밍, 냅색

N, K = map(int,input().split())
# x 개의 아이템을 골랐을 때, y 무게에서의 최대 가치
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
arr = [(0, 0)]

for _ in range(N):
    w, v = map(int,input().split())
    arr.append((w,v))

# 물건 인덱스 i
for i in range(1,N+1):
    # 무게 값 j
    for j in range(1,K+1):
        w = arr[i][0]
        v = arr[i][1]
        # 가방 무게보다 물건이 더 무거우면
        if j < w:
            # 안 담는다, 이전 무게의 가방 값을 가져온다
            dp[i][j] = dp[i-1][j]
        # 물건을 담을 수 있으면
        else:
            # 담지 않았을 때와 담았을 때를 비교
            dp[i][j] = max(dp[i-1][j],v+dp[i-1][j-w])

print(dp[N][K])