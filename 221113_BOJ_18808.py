# BOJ 18808번 스티커 붙이기
# 시뮬레이션, 브루트포스

from collections import deque

# 스티커를 돌리는 함수
def rotate(graph):
    tmp_graph = []
    for x in range(S_W):
        tmp_row = []
        for y in range(S_H-1,-1,-1):
            tmp_row.append(graph[y][x])
        tmp_graph.append(tmp_row)
    return tmp_graph

# 스티커를 붙일 수 있는지 확인하는 함수
def find(i,j,sticker,si,sj):
    q = deque()
    visited = [[0 for _ in range(S_W)] for _ in range(S_H)]
    # 스티커 좌표와, 노트북 좌표
    q.append((si,sj,i,j))
    visited[si][sj] = 1
    large = 1
    while q:
        s_y,s_x,n_y,n_x = q.popleft()
        for dy,dx in [(1,0),(0,1),(-1,0),(0,-1)]:
            ns_y = s_y+dy
            ns_x = s_x+dx
            nn_y = n_y+dy
            nn_x = n_x+dx
            # 스티커 bfs
            if 0 <= ns_y < S_H and 0 <= ns_x < S_W and not visited[ns_y][ns_x]:
                if sticker[ns_y][ns_x] == 1:
                    # 노트북 bfs
                    if 0 <= nn_y < H and 0 <= nn_x < W:
                        if notebook[nn_y][nn_x] == 0:
                            # 일치하면 탐색 계속
                            visited[ns_y][ns_x] = 1
                            q.append((ns_y,ns_x,nn_y,nn_x))
                            large += 1
    # 스티커를 모두 탐색했다면 붙일 수 있다는 말
    if large == l_sticker:
        return True
    else:
        return False

# 스티커를 노트북에 붙이는 함수
def paste(y,x,graph,sy,sx):
    for i in range(S_H):
        for j in range(S_W):
            if graph[i][j] == 1:
                notebook[y+i-sy][x+j-sx] = 1

# 스티커 시작 위치 찾기
def sticker_index(sticker):
    for i in range(S_H):
        for j in range(S_W):
            if sticker[i][j] == 1:
                return (i,j)

H, W, K = map(int,input().split())
notebook = [[0 for _ in range(W)] for _ in range(H)]
# 스티커 리스트
sticker_lst = []
for s in range(K):
    sh, sw = map(int,input().split())
    tmp = [list(map(int,input().split())) for _ in range(sh)]
    sticker_lst.append(tmp)

# 스티커별로
for n in range(K):
    sticker = sticker_lst[n]
    # 스티커 크기
    l_sticker = 0
    for row in sticker:
        l_sticker += sum(row)
    # 스티커를 붙였는 지 확인하는 변수
    not_paste = 1
    # 스티커를 돌린 횟수
    cnt_rotate = 0

    # 스티커를 아직 못 붙였으면서, 4번 이상 돌리지 않았을 때
    while not_paste and cnt_rotate < 4:
        # 스티커의 높이, 너비 갱신
        S_H = len(sticker)
        S_W = len(sticker[0])
        # 스티커 시작 좌표 갱신
        sy,sx = sticker_index(sticker)

        # 가장 위쪽 부터
        for y in range(H):
            # 가장 왼쪽 순으로
            for x in range(W):
                # 스티커를 붙일 빈 공간을 발견하면
                if not notebook[y][x]:
                    # 그 공간부터 스티커를 붙일 수 있는지 확인
                    if find(y,x,sticker,sy,sx):
                        # 가능하면 붙이기
                        paste(y,x,sticker,sy,sx)
                        not_paste = 0
                if not not_paste:
                    break
            if not not_paste:
                break

        # 못 붙이고 반복문을 통과하면
        # 스티커 돌리기
        sticker = rotate(sticker)
        # 돌린 횟수 갱신
        cnt_rotate += 1

result = 0
for row in notebook:
    result += sum(row)
print(result)