# BOJ 2531번 회전 초밥

import sys

n, d, k, c = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]

res = 0

for start in range(n):
    eat_lst = set()     # 먹은 초밥을 담는 집합
    is_c = 1
    for end in range(start, start+k):
        end %= n        # 인덱스가 n을 넘어도 첫번째로 == 회전초밥이 될 수 있게 나머지 연산
        eat_lst.add(arr[end])
        # 쿠폰 초밥이면
        if arr[end] == c:
            # 사용
            is_c = False

    cnt = len(eat_lst)
    # 쿠폰이 있으면
    if is_c:
        # 하나 더 드세요
        cnt += 1
    res = max(res,cnt)

print(res)

