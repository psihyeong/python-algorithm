# SWEA 2105번 디저트 카페
from collections import deque

def dfs(k, y, x, d):
    global result
    # 마지막 방향인데 원점으로 돌아왔을 경우
    if d == 3 and y == ri and x == rj:
        # 최댓값 갱신
        result = max(result, k)
        return
    # 범위를 벗어나거나 중복 메뉴가 있을 경우
    if 0 > y or y >= N or x < 0 or x >= N or graph[y][x] in course:
        # 해당 방향은 그대로 종료..
        return
	# 가지치기
    if result >0:
        if d == 2 and k < result//2:
            return
    # 코스에 메뉴 추가
    course.append(graph[y][x])
    # 다음 위치
    ny, nx = y+direction[d][0], x + direction[d][1]
    # 출발
    dfs(k+1, ny, nx, d)
    # 다른 방향으로도 출발해보자
    d = (d+1)%4
    # 다음 위치
    ny, nx = y+direction[d][0], x + direction[d][1]
    # 출발
    dfs(k + 1, ny, nx, d)
    # 망한코스면 = 범위를 벗어나거나 중복 메뉴를 발견한 코스일 경우, 다른 코스 탐색을 위해 메뉴 제거
    course.pop()

TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    # 무조건 2시,4시,8시,10시 방향 순
    direction = [(-1,1),(1,1),(1,-1),(-1,-1)]
    result = 0
    for i in range(N):
        for j in range(N):
            # 디저트 코스를 담는 리스트
            course = []
            ri,rj = i, j
            dfs(0,i,j,0)

    if result == 0:
        result = -1
    print(f'#{tc} {result}')
