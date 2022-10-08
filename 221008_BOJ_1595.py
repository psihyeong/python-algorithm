# BOJ 1595번 북쪽나라의 도로
from collections import deque

# start 노드에서 가장 거리가 먼 노드 번호를 갱신하고, 거리를 리턴하는 함수
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
                # 다음 노드로 가는 총 거리가, 최대 거리보다 높으면
                if max_dis < total_dis:
                    # 최대 거리 갱신,
                    max_dis = total_dis
                    # 해당 노드가 max_node
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
# 임의의 노드 = 1에서 가장 먼 max_node를 구해서
bfs(1)
# max_node에서 가장 먼 노드의 거리를 출력
print(bfs(max_node))
