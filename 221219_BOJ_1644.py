# BOJ 1644번 소수의 연속합

import sys, math

# n까지 소수의 배열을 반환하는 에라토스테네스의 체
def isPrime(n):
    arr = [True for _ in range(n+1)]
    arr[0], arr[1] = False, False
    for i in range(2, int(math.sqrt(n)) + 1):
        if arr[i] == True:
            j = 2
            while i * j <= n:
                arr[i * j] = False
                j += 1
    return [i for i in range(2,n+1) if arr[i] == True]

N = int(sys.stdin.readline())
primes = isPrime(N)     # N까지 소수를 담는 리스트
num = len(primes)
end = 0
seq_primes_sum = 0      # 연속된 소수의 합
result = 0

for start in range(num):
    # 합이 S 이상이 될 때까지 end 값 증가
    while seq_primes_sum < N and end < num:
        seq_primes_sum += primes[end]
        end += 1
    # 합이 S면 소수의 합으로 나타낼 수 있는 수열의 경우의 수
    if seq_primes_sum == N:
        result += 1
    # 다음 수열을 찾기 위해 start 값 증가
    seq_primes_sum -= primes[start]

print(result)