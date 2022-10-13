# BOJ 17135번 캐슬 디펜스
import heapq

# 궁수의 위치를 조합하는 함수
def dfs(depth, startwith):
    # 궁수 3명이 모두 배치되었다면
    if depth == 3:
        # 해당 게임에서 사용할 배열
        pan = [row[::] for row in graph]
        # 게임 시작
        start_game(pan)
        return
    else:
        # 조합
        for i in range(startwith,W):
            archer.append(castle[i])
            dfs(depth+1, i+1)
            archer.pop()

# 배치된 궁수로 게임을 하는 함수
def start_game(pan):
    global result
    # 게임에서 낸 킬 수
    kill = 0
    while True:
        # 궁수들이 정한 타겟 정보를 담는 리스트
        decision_shoot = []
        # 1,2,3번 궁수별로
        for nth in range(3):
            archer_y, archer_x = archer[nth]
            aim = []    # 궁수별 슛이 가능한 타겟 정보를 담는 리스트
            for i in range(H):
                for j in range(W):
                    # 적이면서
                    if pan[i][j] == 1:
                        aim_dis = abs(archer_y-i)+abs(archer_x-j)
                        # 사격 거리가 닿으면
                        if aim_dis <= D:
                            # 적과의 거리, x좌표 순으로 heappush
                            heapq.heappush(aim,(aim_dis,j,i))
            # 사격 가능한 적이 있으면
            if len(aim) > 0:
                # 가장 최적의 적을 타겟으로 결정
                decision_shoot.append(aim[0])
        # 타겟별로
        for d,x,y in decision_shoot:
            # 적이면
            if pan[y][x] == 1:
                # 죽이고 kill+1
                pan[y][x] = 0
                kill += 1

        # 사격이 끝나면 적군 전진
        go(pan)
        # 게임이 종료되었으면
        if is_gameover(pan):
            # 최댓값 갱신후 반복문 종료
            if kill > result:
                result = kill
            break

# 적군을 전진시키는 함수
def go(pan):
    tmp = []
    for i in range(H):
        for j in range(W):
            if pan[i][j] == 1:
                pan[i][j] = 0
                if 0 <= i+1 < H and 0 <= j < W:
                    tmp.append((i+1,j))
    for y,x in tmp:
        pan[y][x] = 1

# 게임 종료를 판별하는 함수
def is_gameover(pan):
    tmp = 0
    for row in pan:
      tmp += sum(row)

    if tmp == 0:
        return True
    else:
        return False

H, W, D = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(H)]
castle = []     # 성의 위치 인덱스를 담은 리스트
for i in range(W):
    castle.append((H,i))
archer = []     # 궁수의 위치 인덱스를 담은 리스트
result = 0
dfs(0,0)
print(result)
