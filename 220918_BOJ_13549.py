# BOJ 13549번 숨바꼭질3

from collections import deque
# 해당 거리까지 걸린 시간을 구해주는 bfs
def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 0
    while q:
        now = q.popleft()
        # 걷거나 순간이동
        for n in [-1,1,now]:
            next = n + now
            if 0 <= next < 100001 and visited[next] == -1:
                # 순간이동일경우
                if n == now:
                    visited[next] = visited[now]
                    # 우선순위(가중치)를 높게하기 위해 appendleft
                    q.appendleft(next)
                # 걷는 경우
                else:
                    visited[next] = visited[now] + 1
                    q.append(next)
                # 목표지점 값이 정해지면 함수종료
                if visited[K] != -1:
                    return

N, K = map(int,input().split())
visited = [-1 for _ in range(100001)]
bfs(N)
print(visited[K])

