# SWEA 1251번 하나로

def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x
 
def union(x, y):
    rep[find_set(y)] = find_set(x)
 
for tc in range(1,int(input())+1):
    N = int(input())
    adjM = [[0] * (N) for _ in range(N)]
    tmp = []
    tmpx = list(map(int,input().split()))
    tmpy = list(map(int,input().split()))
    seyul = float(input())
    E = 0
    edge = []
    for i in range(0,N):
        for j in range(i+1,N):
            E += 1
            distance = (tmpx[i] - tmpx[j])**2 + (tmpy[i] - tmpy[j])**2
            adjM[i][j] = distance
            adjM[j][i] = distance
            edge.append([i, j, distance*seyul])
  
    edge.sort(key=lambda x: x[2])
    rep = [i for i in range(N)]  # 대표원소 배열
 
    cnt = 0  # 선택한 edge의 수
    total = 0  # MST 가중치의 합
    for u, v, w in edge:
        if find_set(u) != find_set(v):
            cnt += 1
            union(u, v)
            total += w
            if cnt == N - 1:  # 간선 수
                break
    print(f'#{tc} {round(total)}')
