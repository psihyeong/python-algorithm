# BOJ 1595번 북쪽나라의 도로
from collections import deque

def bfs(start):
    global max_node
    visited = [False for _ in range(10001)]
    q = deque()
    q.append((start,0))
    visited[start] = True
    max_dis = 0
    while q:
        now, now_dis = q.popleft()
        for next, next_dis in worlds[now]:
            if not visited[next]:
                visited[next] = True
                total_dis = now_dis+next_dis
                q.append((next,total_dis))
                if max_dis < total_dis:
                    max_dis = total_dis
                    max_node = next
    return max_dis

worlds = [[] for _ in range(10001)]
while True:
    try:
        a, b, dis = map(int,input().split())
        worlds[a].append((b,dis))
        worlds[b].append((a,dis))
    except:
        break

max_node = 0
bfs(1)
print(bfs(max_node))
