# BOJ 1822번 차집합
# 자료 구조, 해시를 사용한 집합과 맵

a, b = map(int, input().split())
# 시간초과를 해결하기 위해 해시를 사용
A, B = {}, {}

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
for n in A_list:
    A[n] = 1
for n in B_list:
    B[n] = 1

C = []
for i in A:
    if i not in B:
        C += [i]

print(len(C))
print(*sorted(C))