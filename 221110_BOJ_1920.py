# BOJ 1920번 수 찾기
# 이분탐색, 정렬, 자료구조

N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
check = map(int, input().split())

# 이분탐색 함수
def binary(num, N, start, end):
    if start > end:
        return 0
    middle = (start+end)//2
    if num == N[middle]:
        return 1
    elif num < N[middle]:
        return binary(num, N, start, middle-1)
    else:
        return binary(num, N, middle+1, end)

for num in check:
    start = 0
    end = N-1
    print(binary(num, A, start, end))