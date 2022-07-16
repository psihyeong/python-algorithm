T = int(input())
for tc in range(1, T + 1):
    N,M = map(int,input().split())
    wall = []
    value = []
    for i in range(N):
        temp = list(map(int,input().split()))
        wall.append(temp)
    for i in range(N+1-M):
        for j in range(N+1-M):
            fly=0
            for k in range(M):
                fly += sum(wall[i+k][j:j+M])
            value.append(fly)
    print(f"#{tc} {max(value)}")