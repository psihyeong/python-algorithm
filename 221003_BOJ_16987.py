# BOJ 16987번 계란으로 계란치기

# 맨 왼쪽(인덱스 0번) 계란부터 맨 오른쪽 계란까지 한 번 집고, 계란치기를 수행하는 함수
def dfs(depth):
    global result
    # 맨 오른쪽 계란까지 계란치기를 다했다면
    if depth == N:
        tmp = 0
        # 깨진 계란의 개수를 세서
        for egg in egg_lst:
            if egg[0] <= 0:
                tmp += 1
        # 최댓값 갱신
        if tmp > result:
            result = tmp
        return

    else:
        now_egg = egg_lst[depth]
        damage = now_egg[1]
        # 만약 현재 계란이 깨져있다면
        if now_egg[0] <= 0:
            # 다음 오른쪽 계란으로 스킵
            dfs(depth+1)
        else:
            is_hit = 0  # 하나의 계란이라도 쳤는지
            # 모든 계란중에
            for i in range(0,N):
                next_egg = egg_lst[i]
                # 자기 자신을 제외하고, 안 깨진 계란이 있다면
                if i != depth and next_egg[0] >= 1:
                    # 계란치기 전처리
                    next_egg[0] -= damage
                    now_egg[0] -= next_egg[1]
                    dfs(depth+1)
                    # 계란치기 후처리
                    next_egg[0] += damage
                    now_egg[0] += next_egg[1]
                    is_hit = 1      # 난 계란을 쳤다
            # 계란을 하나도 칠게 없다면
            if not is_hit:
                # 바로 마지막 분기로 스킵
                dfs(N)

N = int(input())
egg_lst = [list(map(int,input().split())) for _ in range(N)]
result = 0
dfs(0)
print(result)
