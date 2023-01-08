# BOJ 11478번 서로 다른 부분 문자열의 개수

import sys

S = sys.stdin.readline().strip()    # 문자열
N = len(S)        # 문자열 길이

hash = {}         # 부분문자열을 담는 해시

for i in range(1,N+1):      # 1자리 부터 N자리 탐색
    for j in range(N-i+1):  # i자리 부분문자열을 모두 해시에 등록
        hash[S[j:j+i]] = 1

print(len(hash))            # 개수 출력