#BOJ 1747번 소수&팰린드롬

import math
# 에라토스테네스의 체
def isPrime(n):
    arr = [True for _ in range(n+1)]
    # arr[0], arr[1]을 False로 초기화 안해주면 99퍼에서 틀림.
    arr[0], arr[1] = False, False
    for i in range(2, int(math.sqrt(n)) + 1):
        if arr[i] == True:
            j = 2
            while i * j <= n:
                arr[i * j] = False
                j += 1
    return arr

N = int(input())
# 2백만까지의 소수 판독
# 메모리를 더 줄이는 방법은 없을까???
case = 2000000
Primes = isPrime(case)

for i in range(N, len(Primes)):
    temp = str(i)
    # 소수이면서
    if Primes[i]:
        # 팰린드롬이면
        if temp == temp[::-1]:
            # 출력
            print(i)
            break
