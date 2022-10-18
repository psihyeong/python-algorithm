# SWEA 14510번 나무 높이
# 그리디

for tc in range(1,int(input())+1):
    N = int(input())
    trees = list(map(int,input().split()))
    max_tree = max(trees)
    # 최대나무 높이까지 크기위해 필요한 높이
    need = []
    for i in range(N):
        if max_tree - trees[i]:
            need.append(max_tree - trees[i])
    day = 0

    while True:
        # 종료조건
        if sum(need) == 0:
            break
        # 날짜별 주는 물 양
        day += 1
        if day % 2:
            water = 1
        else:
            water = 2

        for i in range(len(need)):
            # 성장에 남은 높이가 1이나 2인 경우
            if need[i] == 1:
                # 물 양과 맞으면 그 나무를 자라게 해줌
                if water == 1:
                    need[i] -= 1
                    break
            elif need[i] == 2:
                if water == 2:
                    need[i] -= 2
                    break
            # 1 또는 2인 경우가 없을경우 아무거나 자라게 해줌
            else:
                # 음수 방지
                if need[i] - water >= 0:
                    need[i] -= water
                    break
        # 정렬
        need.sort()
    print(f'#{tc} {day}')