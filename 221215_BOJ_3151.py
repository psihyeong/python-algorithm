# BOJ 3151번 합이 0

import sys

N = int(sys.stdin.readline())
students = list(map(int,sys.stdin.readline().split()))      # 학생들의 코딩실력을 담는 리스트
students.sort()         # 이분탐색을 위해 정렬
result = 0

# 첫번째 값을 뽑아놓고 나머지 두 값에 대한 투포인터
for first_idx in range(N-2):
    l, r = first_idx+1, N - 1   # 첫번째 값의 한 칸 왼쪽값이 최초 왼쪽값, 맨 오른쪽 값이 최초 오른쪽값
    now_r = N       # 오른쪽 값의 중복된 갯수를 알기 위해 설정한 변수
    while l < r:
        group_sum = students[first_idx] + students[l] + students[r]
        # 합이 0일때
        if group_sum == 0:
            # 왼쪽값과 오른쪽값이 같다면 그 사이는 모두 같은 사람들이기 때문에
            if students[l] == students[r]:
                # r - l 만큼 중복되지 않게 그룹을 만들 수 있음
                result += r - l
            else:
                # 오른쪽 값의 중복된 값의 개수를 판단하기 위해
                # r 값이 바뀌면
                if now_r > r:
                    # 최초 r이 max_r
                    now_r = r
                    # 중복되는 만큼 max_r 왼쪽으로 가기
                    while now_r >= 0 and students[now_r - 1] == students[r]:
                        now_r -= 1
                # 중복된 갯수만큼 그룹을 만들 수 있음
                result += (r - now_r + 1)

            # 모든 경우를 계산하고 왼쪽값 이동
            l += 1

        elif group_sum < 0:
            l += 1
        else:
            r -= 1

print(result)