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

