# BOJ 13913번 숨바꼭질 4
# BFS

from collections import deque

def getPath():
    tmp = [K]
    i = 0
    posi = K
    while i < move:
        tmp.append(moving[posi])
        posi = moving[posi]
        i += 1

    return tmp[::-1]

def bfs():
    dq = deque()

    dq.append(N)
    visited[N] = 1

    while dq:
        now = dq.popleft()

        if now == K:
            return

        for i in [now+1, now-1, 2*now]:
            if 0 <= i <= 100000 and visited[i] == 0:
                dq.append(i)
                visited[i] = visited[now] + 1
                moving[i] = now
    return

# 수빈이의 위치 N, 동생이 있는 위치 K
N, K = map(int, input().split())

# 지나온 경로를 넣을 배열
moving = [0] * 100001
visited = [0] * 100001
bfs()
# 움직인 횟수
move = visited[K]-1
path = getPath()

print(move)
for p in path:
    print(p, end=' ')