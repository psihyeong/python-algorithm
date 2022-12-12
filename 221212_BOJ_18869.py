# BOJ 18869번 멀티버스 II

import sys

M, N = map(int,sys.stdin.readline().split())

multiverse = []     # 우주별 행성의 사이즈 순으로 정렬된 튜플을 담는 리스트

for _ in range(M):
    # space = list(map(int, sys.stdin.readline().split()))
    # 위 리스트에서 순서를 유지하면서 중복을 제거하는 해시를 만드는 코드
    # 행성의 중복을 제거한 초기 우주 해시, 키 값만 사용하기위해 (x,True) 이런식으로 사용
    space = dict((x, True) for x in map(int, sys.stdin.readline().split())).keys()
    universe = {i: size for i, size in enumerate(space)}        # 행성의 인덱스를 키, 사이즈를 값으로 갖는 해시
    universe = sorted(universe, key=universe.get)               # 사이즈순으로 정렬
    multiverse.append(tuple(universe))      # 튜플 담기

# 우주 쌍 개수 찾기
result = 0
for i in range(len(multiverse)):
    for j in range(i+1, len(multiverse)):
        if multiverse[i] == multiverse[j]:
            result += 1

print(result)
# Reference : https://velog.io/@delicate1290/%EB%B0%B1%EC%A4%80-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4-%EB%A9%80%ED%8B%B0%EB%B2%84%EC%8A%A4-18869%EB%B2%88



# import sys, heapq

# M, N = map(int,sys.stdin.readline().split())

# # 우주의 인덱스를 행성크기 순으로 정렬한 우주순서의 개수를 저장하는 해시
# multiverse = {}

# for _ in range(M):
#     space = list(map(int,sys.stdin.readline().split()))
#     # 행성크기와 인덱스를 담는 리스트
#     space_info = []
#     for i in range(N):
#         space_info.append((space[i], i))
#     # 행성크기로 인덱스 정렬
#     space_info.sort(key=lambda x : x[0])
#     # 인덱스만 담는 리스트
#     space_idx = []
#     for i in range(N):
#         space_idx.append(space_info[i][1])

#     # 해시에 개수 추가
#     if ''.join(map(str,space_idx)) not in multiverse:
#         multiverse[''.join(map(str, space_idx))] = 1
#     else:
#         multiverse[''.join(map(str, space_idx))] += 1

# result = 0
# for cnt in multiverse.values():
#     result += cnt * (cnt-1) // 2
# print(result)

# 행성의 중복을 처리하지 못함, 해시를 깔끔하게 사용하지 못한 실패한 코드
