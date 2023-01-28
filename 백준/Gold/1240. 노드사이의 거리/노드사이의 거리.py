from collections import deque

N, M = map(int,input().split())
tree = [[0 for _ in range(N+1)] for _ in range(N+1)]

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
                    visited[i] = False

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
