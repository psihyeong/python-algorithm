# BOJ 11659번 구간 합 구하기 4
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
numlist = list(map(int, input().split()))

for  in range(M):
    start, end = map(int, input().split())
    result = sum(num_list[start-1:end])
    print(result) 
# 최악의 경우 연산횟수 N*M -> 시간초과
'''

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
# sum_list는 index 번호까지의 누적합인 리스트
# 0 번은 없으니 0으로 초기화
sum_list = [0]
sum = 0

for i in num_list:
    sum += i
    sumlist.append(sum)

for  in range(M):
    start, end = map(int,input().split())
    print(sum_list[end]-sum_list[start-1])
# 연산횟수 N+M
# 코드가 짧다고, for문이 적다고 시간이 짧은게 아님, 연산량을 봐야함
