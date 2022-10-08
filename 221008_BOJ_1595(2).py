# BOJ 1595번 북쪽나라의 도로

# 출발 노드에서 가장 거리가 먼 노드까지의 거리를 갱신하는 함수
def dfs(start,now_dis):
    global max_dis
    for next, next_dis in info[start]:
        if not visited[next]:
            visited[next] = True
            total_dis = now_dis+next_dis
            # 다음 노드로 가는 총 거리가, 최대 거리보다 높으면
            if max_dis < total_dis:
                # 최대 거리 갱신,
                max_dis = total_dis
            dfs(next,total_dis)

info = [[] for _ in range(10001)]
world = set()
while True:
    try:
        a, b, dis = map(int,input().split())
        info[a].append((b,dis))
        info[b].append((a,dis))
        world.add(a)
        world.add(b)
    except:
        break

max_dis = 0
# 모든 노드의 최대 거리 중 최댓값
for start in world:
    visited = [0 for _ in range(10001)]
    visited[start] = True
    dfs(start,0)
print(max_dis)
