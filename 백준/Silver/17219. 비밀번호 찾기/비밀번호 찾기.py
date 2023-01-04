# BOJ 17219번 비밀번호 찾기

import sys

N, M = map(int,sys.stdin.readline().split())

hash = {}
for _ in range(N):
    address, password = sys.stdin.readline().split()
    hash[address] = password

for _ in range(M):
    tmp = sys.stdin.readline().strip()
    print(hash[tmp])