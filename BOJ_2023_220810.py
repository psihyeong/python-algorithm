# BOJ 2023번 신기한 소수

import math
N = int(input())
# 소수 판독
def isprime(x):
  # 문자열을 변수로 받기 때문에 정수형으로 변환
  x = int(x)
  if x == 0 or x == 1:
    return False
  for i in range(2, int(math.sqrt(x)) + 1):
    if x % i == 0:
      return False
  return True

def dfs(n):
  # n자리 수면 모든 테스트를 통과했다는 것이니 출력하고 함수종료
  if len(n) == N:
    print(n)
    return
  
  for i in follow:
    # 자릿수를 더하고, 소수면 계속 더해주는 재귀
    if isprime(n+i):
      dfs(n+i)
          
first = ['2','3','5','7']
follow = ['1','3','7','9']

for n in first:
  dfs(n)
