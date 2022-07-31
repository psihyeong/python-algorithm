# BOJ 4883번 삼각 그래프
# 보텀업 DP 풀이

tc = 0
while True:
    tc += 1
    N = int(input())
    if N == 0:
        break
    # 2차원 그래프 만들기    
    graph = []
    for i in range(N):
        K = list(map(int,input().split()))
        graph.append(K)

    # 시작점 왼쪽(graph[0][0])은 제외, 시작점도 제외한 나머지 갯수만큼 dp 초기화
    # dp는 해당 지점까지 가는데 드는 비용들의 최솟값
    # 그래프의 3번째 줄부터 for문을 돌리기 때문에 dp[0]부터 dp[3]까지는 값을 직접 입력
    dp = [0 for i in range((N*3-2))]
    start = graph[0][1]
    dp[0] = graph[0][2]+start
    dp[1] = graph[1][0]+start
    dp[2] = min(dp[1]+graph[1][1],start+graph[1][1],dp[0]+graph[1][1])
    dp[3] = min(dp[0]+graph[1][2],start+graph[1][2],dp[2]+graph[1][2])

    # 세번째 줄 부터 마지막 줄까지의
    for i in range(1,N-1):
        # 2,3번은 바로 직전의 1번을 참조하기 때문에
        # 1,2,3번 순서 
        for j in range(1,4):
            np = i*3+j
            # 1번 위치
            if (np % 3) == 1:
                dp[np] = min(dp[np-3]+graph[i+1][j-1], dp[np-2]+graph[i+1][j-1])
            # 2번 위치
            elif (np % 3) == 2:
                dp[np] = min(dp[np-4]+graph[i+1][j-1], dp[np-3]+graph[i+1][j-1], dp[np-2]+graph[i+1][j-1], dp[np-1]+graph[i+1][j-1])
            # 3번 위치
            else:
                dp[np] = min(dp[np-4]+graph[i+1][j-1], dp[np-3]+graph[i+1][j-1], dp[np-1]+graph[i+1][j-1])

    print(f'{tc}. {dp[3*N-4]}')
