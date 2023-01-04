# BOJ 17219번 비밀번호 찾기

N, M = map(int,input().split())

hash = {}
for _ in range(N):
    address, password = input().split()
    hash[address] = password

for _ in range(M):
    tmp = input()
    print(hash[tmp])