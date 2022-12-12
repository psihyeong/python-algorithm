# BOJ 18869번 멀티버스 II

import sys, heapq

M, N = map(int,sys.stdin.readline().split())

# 우주의 인덱스를 행성크기 순으로 정렬한 우주순서의 개수를 저장하는 해시
multiverse = {}

for _ in range(M):
    space = list(map(int,sys.stdin.readline().split()))
    # 행성크기와 인덱스를 담는 리스트
    space_info = []
    for i in range(N):
        space_info.append((space[i], i))
    # 행성크기로 인덱스 정렬
    space_info.sort(key=lambda x : x[0])
    # 인덱스만 담는 리스트
    space_idx = []
    for i in range(N):
        space_idx.append(space_info[i][1])

    # 해시에 개수 추가
    if ''.join(map(str,space_idx)) not in multiverse:
        multiverse[''.join(map(str, space_idx))] = 1
    else:
        multiverse[''.join(map(str, space_idx))] += 1

result = 0
for cnt in multiverse.values():
    result += cnt * (cnt-1) // 2
print(result)

