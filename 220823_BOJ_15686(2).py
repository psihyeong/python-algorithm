# BOJ 15686번 치킨 배달
def dfs(n, id):
    global result
    case_value = 0

    if n == M:
        # 집마다 치킨 거리 구하기
        for h in home:
            home_chicken_distance = 9999999999
            for chic in open_store:
                tmp = abs(chic[0] - h[0]) + abs(chic[1] - h[1])
                if home_chicken_distance > tmp:
                    home_chicken_distance = tmp
            # 해당 집의 치킨 거리 구했으면 해당 케이스 결과값에 더해주기
            case_value += home_chicken_distance
            if case_value > result:
                return
        # 최솟값 갱신
        if case_value < result:
            result = case_value
            return

    for i in range(id,K):
        for j in range(i, K):
            open_store.append(store[j])
            dfs(n+1, j+1)
            open_store.pop()

N, M = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(N)]
home = []
store = []
open_store = []
for i in range(N):
    for j in range(len(city[i])):
        if city[i][j] == 2:
            store.append((i,j))
        elif city[i][j] == 1:
            home.append((i,j))

K = len(store)
visited = [False] * K
result = int(1e9)
dfs(0,0)

print(result)
