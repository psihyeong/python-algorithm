# BOJ 1941번 소문난 칠공주
def dfs(depth, beginwith):
    global result
    if depth == 7:
        if is_S(tmp_lst) and is_Adj(tmp_lst):
            result += 1
        return
    else:
        for i in range(beginwith,len(loc_info)):
            tmp_lst.append(loc_info[i])
            dfs(depth + 1, i + 1)
            tmp_lst.pop()

def is_S(lst):
    tmp = 0
    for y,x in lst:
        if graph[y][x] == 'S':
            tmp += 1

    if tmp >= 4:
        return True
    else:
        return False

def is_Adj(lst):
    visited = [[0 for _ in range(5)] for _ in range(5)]
    q = []
    q.append(lst[0])
    visited[lst[0][0]][lst[0][1]] = True
    result = 0
    while q:
        y,x = q.pop(0)
        result += 1
        for dy,dx in [(1,0),(0,1),(-1,0),(0,-1)]:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < 5 and 0 <= nx < 5 and not visited[ny][nx]:
                if (ny,nx) in lst:
                    q.append((ny,nx))
                    visited[ny][nx] = 1

    if result == 7:
        return True
    else:
        return False

graph = [list(map(str,input())) for _ in range(5)]
loc_info = []
for i in range(5):
    for j in range(5):
        loc_info.append((i,j))
tmp_lst = []
result = 0
dfs(0,0)
print(result)
