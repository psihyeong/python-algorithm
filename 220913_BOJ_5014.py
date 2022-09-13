# BOJ 5014번 스타트링크
from collections import deque

def pushbutton(s,g):
    que = deque()
    que.append(s)
    visited[s] = 0
    # 층 bfs
    while que:
        # 현재 층에서
        now_stair = que.popleft()
        # 목표 층이라면 버튼수 return
        if now_stair == g:
            return visited[g]
        # 위 또는 아래로
        for move in (up,-down):
            # 움직였을 때
            next_stair = now_stair + move
            # 유효한 층이고, 방문한 적 없는 층이라면
            if 1 <= next_stair <= total_stair and visited[next_stair] == -1:
                # 이동, 해당 층까지 가는데 누른 버튼 수 갱신
                visited[next_stair] = visited[now_stair] + 1
                que.append(next_stair)

    # 목표 층에 도달 못한 경우
    return 'use the stairs'

total_stair, start, goal, up, down = map(int,input().split())

# 버튼을 누른 횟수
visited = [-1 for _ in range(total_stair+1)]

print(pushbutton(start,goal))
