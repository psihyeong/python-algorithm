# BOJ 2230번 수 고르기

import sys

N, M = map(int, sys.stdin.readline().split())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
numbers.sort()      # 투포인터를 위한 정렬

now_diff = sys.maxsize     # 최솟값을 구하기 위한 변수

s, e = 0, 0
while s < N and e < N:
    diff = numbers[e] - numbers[s]      # 두 수의 차이
    # 차이가 M보다 크거나 같으면 끝
    if diff >= M:
        s += 1
        # 최솟값 갱신
        now_diff = min(now_diff, diff)
    # M보다 작으면 차이를 더 키우기 위해 e를 증가
    # 이땐 최솟값 갱신 X
    elif diff < M:
        e += 1

print(now_diff)