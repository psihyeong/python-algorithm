# SWEA 4698번 테네스의 특별한 소수

arr = [True] * 1000001
arr[0], arr[1] = False, False
isPrimes = []
for i in range(2, 1000001):
    if arr[i] == True:
        isPrimes.append(i)
        for j in range(i + i, 1000001, i):
            arr[j] = False

TC = int(input())

for tc in range(1, TC + 1):
    N, start, end = map(int, input().split())

    cnt = 0
    for i in isPrimes:
        if start <= i <= end:
            if str(N) in list(str(i)):
                cnt += 1

    print(f'#{tc} {cnt}')
