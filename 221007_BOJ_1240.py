# BOJ 1240번 노드사이의 거리

from collections import deque

# 목표노드 까지의 거리를 구하는 DFS
def dfs(now, goal,val):
    global result

    if now == goal:
        result = val
        return
    else:
        for i in range(N+1):
            if tree[now][i] > 0:
                if not visited[i]:
                    visited[i] = True
                    new_val = val + tree[now][i]
                    dfs(i,goal,new_val)

N, M = map(int,input().split())
tree = [[0 for _ in range(N+1)] for _ in range(N+1)]

# 양방향 트리 인접행렬 만들기
for _ in range(N-1):
    s,d,dis = map(int,input().split())
    tree[s][d] = dis
    tree[d][s] = dis


for _ in range(M):
    result = 0
    visited = [0 for _ in range(N+1)]
    a,b = map(int,input().split())
    visited[a] = True
    dfs(a,b,0)
    print(result)
