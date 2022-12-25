# BOJ 13414번 수강신청

import sys

K, N = map(int, sys.stdin.readline().split())

hash = {}       # 학번을 key, 신청 우선순위를 value로 하는 해시
for i in range(N):
    # int(input())으로 받으면 학번 0123이 123으로 들어가버림.
    n = sys.stdin.readline().rstrip()
    # 다시 수강신청 버튼을 누른 경우 우선순위가 뒤로 밀려남
    hash[n] = i

# 신청 우선순위 오름차순 정렬
hash = sorted(hash.items(), key=lambda x:x[1])

cnt = 0
for info in hash:
    print(info[0])
    cnt += 1
    if cnt == K:
        break
'''
# 총 수강신청 인원이 K명이 안될 경우 런타임에러
for i in range(K):
    print(hash[i][0])
'''