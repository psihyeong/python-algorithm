# BOJ 2295번 세 수의 합

import sys

# 이분탐색 함수
def binary_search(num):
    l, r = 0, len(sum_arr)
    while l <= r:
        mid = (l + r) // 2
        if sum_arr[mid] == num:
            return True
        elif sum_arr[mid] < num:
            l = mid + 1
        else:
            r = mid - 1
    return False


N = int(sys.stdin.readline())
U = [int(sys.stdin.readline()) for _ in range(N)]

sum_arr = set()     # 모든 두 수의 합을 담는 변수
for x in U:
    for y in U:
        sum_arr.add(x+y)

# 이분탐색을 위해 리스트로 변환, 정렬
sum_arr = list(sum_arr)
sum_arr.sort()


# 세 수의 합을 구하고(O(N^3)), 해당 값이 U안에 포함된 경우를 찾을 때 걸리는 시간복잡도 O(N^3logN)
# O(N^2logN)으로 시간을 줄이기 위해, x번째 수 + y번째 수 = k번째 수 - z번째 수 식을 사용.
result = 0
for k in range(N-1,-1,-1):
    for z in range(k):
        # k번째 수 - z번째 수가
        num = U[k]-U[z]
        # x번째 수 + y번째 수를 담은 배열 안에 있으면,
        if binary_search(num):
            # 최댓값 갱신
            if U[k] >= result:
                result = U[k]

print(result)

