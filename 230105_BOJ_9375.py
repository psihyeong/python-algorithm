# BOJ 9375번 패션왕 신해빈

import sys

TC = int(sys.stdin.readline())      # 테스트 케이스 수
# 테스트 케이스 별
for tc in range(TC):
    n = int(sys.stdin.readline())      # 의상의 수
    res = 1         # 결과값
    hash = {}       # 의상의 종류별 갯수+1을 담는 해시
    for _ in range(n):
        name, cloth = sys.stdin.readline().split()
        # 의상의 개수 담기
        if cloth not in hash:
            hash[cloth] = 2
        else:
            hash[cloth] += 1

    # 의상별 갯수+1개를 담는 이유는 안 입는 경우까지 포함해야 하기 때문.

    # 모든 의상별 경우의 수를 곱하고
    for key, value in hash.items():
        res *= value
    # 알몸인 경우의 수 1을 빼줌.
    print(res-1)