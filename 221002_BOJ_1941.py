# BOJ 1941번 소문난 칠공주

from collections import deque

# 25개의 좌표중 7개의 조합을 뽑는 dfs
def dfs(depth, beginwith):
    global result
    # 7개의 좌표 조합이
    if depth == 7:
        # '이다솜파'이면서, 서로 인접해 있으면
        if is_S(tmp_lst) and is_Adj(tmp_lst):
            # '소문난 칠공주'를 결성할 수 있는 하나의 경우의 수
            result += 1
        return

    else:
        # 백트래킹을 활용한 조합을 구하는 방법
        for i in range(beginwith,len(loc_info)):
            tmp_lst.append(loc_info[i])
            dfs(depth + 1, i + 1)
            tmp_lst.pop()

# '이다솜파'인지 확인하는 함수
def is_S(lst):
    tmp = 0
    for y,x in lst:
        if graph[y][x] == 'S':
            tmp += 1

    if tmp >= 4:
        return True
    else:
        return False

# 서로 인접한 자리인지 확인하는 함수, BFS
def is_Adj(lst):
    visited = [[0 for _ in range(5)] for _ in range(5)]
    q = deque()
    q.append(lst[0])
    visited[lst[0][0]][lst[0][1]] = True
    result = 0
    while q:
        y,x = q.popleft()
        result += 1
        for dy,dx in [(1,0),(0,1),(-1,0),(0,-1)]:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < 5 and 0 <= nx < 5 and not visited[ny][nx]:
                if (ny,nx) in lst:
                    q.append((ny,nx))
                    visited[ny][nx] = 1

    if result == len(lst):
        return True
    else:
        return False


graph = [list(map(str,input())) for _ in range(5)]      # 좌표별 학생 값
loc_info = []       # 5*5의 모든 좌표정보를 담은 리스트
for i in range(5):
    for j in range(5):
        loc_info.append((i,j))
tmp_lst = []        # 좌표들의 7개 조합을 담는 리스트
result = 0          # 결과값
dfs(0,0)

print(result)
