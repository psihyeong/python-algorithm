# BOJ 9663번 N-Queen

def DFS(L, per):
    # 결과값
    global result
    # N까지 배치 조합을 완성했다면 결과값+1
    if L == N:
        result += 1
        return
    else:
        # 모든 자리 중
        able = [True] * N
        dis = L
        # 불가능한 자리는 False로 갱신
        for i in per:
            able[i] = False
            if 0 <= i - dis < N:
                able[i - dis] = False
            if 0 <= i + dis < N:
                able[i + dis] = False
            dis -= 1
        # 가능한 자리 per에 추가하고 dfs 전처리
        for i in range(N):
            if able[i]:
                per.append(i)
                DFS(L+1,per)
                # 후처리
                per.pop()

N = int(input())
result = 0
# 위에서 아래로 배치 순열
per = []
DFS(0,per)
print(result)
