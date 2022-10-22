# BOJ 17136번 색종이 붙이기
# 브루트포스, 백트래킹

# 맨 왼쪽 위 좌표 y,x부터 n크기만큼이 색종이로 붙일 수 있는 지 확인
def is_n_paper(y,x,n):
    check = 1
    for i in range(y,y+n):
        for j in range(x,x+n):
            # 0이 적힌 칸에는 색종이가 있으면 안된다.
            if graph[i][j] == 0:
                check = 0
                break
        if check == 0:
            break
    if check:
        return True
    else:
        return False

# 색종이를 붙이는 함수, 모두 0으로 바꾸는 함수
def attach(y,x,n):
    for i in range(y,y+n):
        for j in range(x,x+n):
            graph[i][j] = 0

# 색종이를 떼는 함수, 모두 1로 바꾸는 함수
def detach(y,x,n):
    for i in range(y,y+n):
        for j in range(x,x+n):
            graph[i][j] = 1

# 전부 0인지, 색종이를 모든 칸에 붙였는지 확인하는 함수
def all_attach():
    check = 1
    for i in range(10):
        for j in range(10):
            if graph[i][j] != 0:
                check = 0
    if check:
        return True
    else:
        return False

# 백트래킹 dfs
def dfs():
    global result
    # 이미 최솟값보다 많은 색종이를 사용했을 경우, 가지치기
    if sum(cnt) > result:
        return

    # 색종이를 모두 붙였다면,
    if all_attach():
        tmp = sum(cnt)
        # 최솟값 갱신
        if result > tmp:
            result = tmp
        return

    else:
        # 0,0부터
        for i in range(10):
            for j in range(10):
                # 1을 찾아서
                if graph[i][j] == 1:
                    # 1부터 5 크기의 색종이를 대보기
                    for n in range(5, 0, -1):
                        # is_n_paper함수의 인덱스 에러를 방지하기 위한 조건.
                        if i+n <= 10 and j+n <= 10:
                            # 색종이를 댈 수 있으면서,
                            if is_n_paper(i,j,n):
                                # 5장을 넘지 않았으면
                                if cnt[n-1] + 1 <= 5:
                                    # 붙이고
                                    attach(i,j,n)
                                    cnt[n-1] += 1
                                    # 재귀
                                    dfs()
                                    # 후처리
                                    cnt[n-1] -= 1
                                    detach(i,j,n)

                    # 루프 탈출을 위한 return
                    # 이 return이 없으면 같은 색종이 조합을 순서만 바꿔서 여러번 탐색하게됨
                    # 색종이 5장의 모든 경우를 보기 때문에,
                    # 좌측 최상단의 최초 1만 탐색하고 함수를 종료해줘도, 모든 색종이 조합을 볼 수 있음.
                    return

graph = [list(map(int,input().split())) for _ in range(10)]
# idx 크기의 색종이 갯수
cnt = [0,0,0,0,0]
result = int(1e9)
dfs()
if result == int(1e9):
    result = -1
print(result)