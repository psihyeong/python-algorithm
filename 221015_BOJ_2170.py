# BOJ 2170번 선 긋기
# 그리디, 정렬

N = int(input())
line = [list(map(int,input().split())) for _ in range(N)]
# 시작점을 기준으로 오름차순 정렬
line.sort(key = lambda x : x[0])
# 현재 그어진 선의 시작점, 끝점
# 초기값 1번째 선
min_p, max_p = line[0][0], line[0][1]

result = 0
# 두번째 선부터
for i in range(1,N):
    # 시작점과 끝점
    start , end = line[i][0], line[i][1]
    # 시작점이 지금 그어진 선의 안에 들어가면,
    if start <= max_p:
        # 끝 점이 현재 그어진 선의 끝 점보다 크면
        if end > max_p:
            # 끝 점 갱신
            max_p = end
    # 더 이상 현재 그어진 선과 겹쳐서 그어질 선이 없으므로
    else:
        # 그려진 선의 길이 더해주고, 버림
        result += max_p - min_p
        # 새로 시작할 그어진 선의 시작점, 끝점 갱신
        min_p = start
        max_p = end
    print(result)

# 마지막으로 현재 그려진 선의 길이 더해주기
result += max_p - min_p
print(result)
