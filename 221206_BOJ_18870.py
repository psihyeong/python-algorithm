# BOJ 18870번 좌표 압축
import sys

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
sorted_arr = sorted(list(set(arr)))

result = []
for n in arr:       # 모든 좌표에 대하여
    # 시간을 줄이기 위해 이분탐색, O(NlogN)
    l, r = 0, len(sorted_arr)-1
    while l <= r:
        mid = (l+r) // 2
        if sorted_arr[mid] == n:
            # mid인덱스 == 해당 값보다 작은 수의 개수 == 좌표 압축 결과
            # 값을 찾았다면 좌표 압축 결과를 result에 삽입
            result.append(mid)
            break
        elif sorted_arr[mid] < n:
            l = mid+1
        else:
            r = mid-1

# for n in arr:
#     for idx in range(len(sorted_arr)):
#         if n == sorted_arr[idx]:
#             result.append(idx)
#             break
# 시간초과 코드 O(N^2)

print(*result)