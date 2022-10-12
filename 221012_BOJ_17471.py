# BOJ 17471번 게리맨더링
# 시뮬레이션, 브루트포스, DFS, BFS

from collections import deque
# 한쪽 선거구가 구역이 1개부터 N-1개까지,
# 어떤 구역이든 고를 수 있는 모든 조합의 경우의 수를 따져서 최솟값을 갱신하는 함수
def dfs(depth, startwith):
    global result
    # 한쪽 선거구 구역이 1개 이상, N-1개 이하면
    if 0 < len(one_side) < N:
        # 반대쪽 선거구 리스트 생성
        another_side = []
        for i in range(1, N + 1):
            if i not in one_side:
                another_side.append(i)
        # 양쪽 선거구가 인접 트리이면, 선거구를 나눌 수 있는 가능한 방법이면
        if bfs(another_side) and bfs(one_side):
            # 두 선거구에 포함된 인구의 차이를 구해서
            tmp = cal_diff(another_side, one_side)
            # 최솟값 갱신
            if tmp < result:
                result = tmp

    # 재귀 종료 조건
    if depth == N:
        return

    else:
        # 백트래킹으로 조합을 구하는 방법
        for i in range(startwith, N + 1):
            one_side.append(i)
            dfs(depth + 1, i + 1)
            one_side.pop()

# 한쪽 선거구 리스트가 인접한 선거구인지를 확인해주는 함수
def bfs(lst):
    # 모든 구역이 방문된 리스트
    visited = [1 for _ in range(N + 1)]
    # 선거구 리스트는 방문하지 않았다고 처리해주고
    for i in lst:
        visited[i] = 0
    # 탐색 시작
    q = deque()
    q.append(lst[0])
    visited[lst[0]] = 1
    while q:
        now = q.popleft()
        # 인접한 선거구 중
        for next in adj[now]:
            # 방문하지 않았고, 선거구 리스트에 들어있으면
            if next in lst and not visited[next]:
                # 계속 탐색
                q.append(next)
                # 방문처리
                visited[next] = 1

    # 전부 방문됐으면, 모두 인접하면
    if sum(visited) == N + 1:
        return True
    else:
        return False

# 두 선거구에 포함된 인구의 차이를 구하는 함수
def cal_diff(lst_a, lst_b):
    tmp_a, tmp_b = 0, 0
    for i in lst_a:
        tmp_a += zone_people[i]

    for i in lst_b:
        tmp_b += zone_people[i]

    return abs(tmp_a - tmp_b)

N = int(input())
# 구역별 인구수
zone_people = [0] + list(map(int,input().split()))
# 인접한 구역 트리 구현
adj = [[] for _ in range(N+1)]
for i in range(1,N+1):
    tmp = list(map(int,input().split()))
    adj_num = tmp[0]
    for j in range(1,adj_num+1):
        if i != tmp[j]:
            if tmp[j] not in adj[i]:
                adj[i].append(tmp[j])
            if i not in adj[tmp[j]]:
                adj[tmp[j]].append(i)

result = int(1e9)
# 두 선거구 중 한쪽 선거구
one_side = []
# 선거구는 1번부터 시작하므로 0,1
dfs(0,1)
# 두 선거구로 나눌 수 있는 방법이 없는 경우
if result == int(1e9):
    result = -1
print(result)

