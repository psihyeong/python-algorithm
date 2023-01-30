# BOJ 15683번 감시
# 시뮬레이션, 브루트포스

from collections import deque

# 한 방향을 감시했을 때, 감시처리를 해주고, 감시영역의 수를 반환하는 함수
def one_line_oversee(y,x,dy,dx,graph):
    watch = 0
    q = deque()
    q.append((y,x))
    while q:
        y,x = q.popleft()
        ny = dy + y
        nx = dx + x
        # 사무실 안 이면서 벽이 아니면
        if 0 <= ny < H and 0 <= nx < W and graph[ny][nx] != 6:
            # 탐색 진행
            q.append((ny, nx))
            # 빈 칸이면 감시처리해주고 +1
            if graph[ny][nx] == 0:
                watch += 1
                graph[ny][nx] = 7
    return watch


# 카메라의 번호와, 방향정보를 입력받아 방향리스트를 반환해주는 함수
def choice_line(num,dir):
    if num == 1:
        if dir == 0:
            return [(-1,0)]
        elif dir == 1:
            return [(1,0)]
        elif dir == 2:
            return [(0,1)]
        elif dir == 3:
            return [(0,-1)]
        
    elif num == 2:
        if dir == 0:
            return [(-1,0),(1,0)]
        elif dir == 1:
            return [(0,-1),(0,1)]
        
    elif num == 3:
        if dir == 0:
            return [(-1,0),(0,1)]
        elif dir == 1:
            return [(1,0),(0,1)]
        elif dir == 2:
            return [(-1,0),(0,-1)]
        elif dir == 3:
            return [(1,0),(0,-1)]
        
    elif num == 4:
        if dir == 0:
            return [(0,1),(1,0),(-1,0)]
        elif dir == 1:
            return [(0,-1),(1,0),(-1,0)]
        elif dir == 2:
            return [(0,-1),(0,1),(-1,0)]
        elif dir == 3:
            return [(0,-1),(0,1),(1,0)]
        
    elif num == 5:
        return [(0,-1),(0,1),(1,0),(-1,0)]


# 카메라 방향정보의 모든 경우의 수를 조합해 감시영역의 최댓값을 갱신하는 함수
def dfs(depth):
    global result
    # 모든 카메라의 방향정보가 정해졌을 때
    if depth == len(camera_info):
        tmp = 0
        # 사무실의 복사본
        graph = [row[::] for row in origin_graph]
        # 카메라 별로
        for i in range(depth):
            y,x = camera_info[i][0], camera_info[i][1]
            camera_num = camera_info[i][2]
            # 방향정보에 따른 방향들의
            for dy,dx in choice_line(camera_num,dir_lst[i]):
                # 감시영역의 수를 더해주고
                tmp += one_line_oversee(y,x,dy,dx,graph)
        # 모두 더했으면
        # 감시영역 최댓값 갱신
        if tmp > result:
            result = tmp

    else:
        camera_num = camera_info[depth][2]
        # 1번 카메라면
        if camera_num == 1:
            # 4방향 중 하나
            for d in range(4):
                dir_lst.append(d)
                dfs(depth+1)
                dir_lst.pop()
        # 2번 카메라면
        elif camera_num == 2:
            # 2방향 중 하나
            for d in range(2):
                dir_lst.append(d)
                dfs(depth+1)
                dir_lst.pop()
        # 3번 카메라면
        elif camera_num == 3:
            # 4방향 중 하나
            for d in range(4):
                dir_lst.append(d)
                dfs(depth+1)
                dir_lst.pop()
        # 4번 카메라면
        elif camera_num == 4:
            # 4방향 중 하나
            for d in range(4):
                dir_lst.append(d)
                dfs(depth+1)
                dir_lst.pop()
        # 5번 카메라면
        elif camera_num == 5:
            # 1방향 고정
            dir_lst.append(1)
            dfs(depth+1)
            dir_lst.pop()

H, W = map(int,input().split())
origin_graph = [list(map(int,input().split())) for _ in range(H)]
camera_info = []     # 카메라의 위치와, 카메라 번호를 담는 리스트
sagak = 0           # 최초 사각지대의 개수
for i in range(H):
    for j in range(W):
        if origin_graph[i][j] != 0 and origin_graph[i][j] != 6:
            camera_info.append((i, j, origin_graph[i][j]))
        elif origin_graph[i][j] == 0:
            sagak += 1
result = 0
dir_lst = []
dfs(0)
print(sagak-result)