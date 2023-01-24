from itertools import combinations

N, M = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(N)]
home = []
store = []
for i in range(N):
    for j in range(len(city[i])):
        if city[i][j] == 2:
            store.append([i,j])
        elif city[i][j] == 1:
            home.append([i,j])

# 폐업시키지 않을 치킨집의 M개가 될 수 있는 경우의수
open_store = list(combinations(store,M))
result = 9999999999
# 모든 경우의 수
for case in open_store:
    case_value = 0
    # 집마다 치킨 거리 구하기
    for h in home:
        home_chicken_distance = 9999999999
        for chic in case:
            tmp = abs(chic[0]-h[0]) + abs(chic[1]-h[1])
            if home_chicken_distance > tmp:
                home_chicken_distance = tmp
        # 집의 치킨 거리 구했으면 해당 케이스 결과값에 더해주기
        case_value += home_chicken_distance
        # 케이스 결과값이 최솟값을 넘어버리면, 가망이 없는 케이스라 판단하고, 탐색 종료
        if case_value > result:
            break
    # 최솟값 갱신
    if case_value < result:
        result = case_value
        
print(result)
