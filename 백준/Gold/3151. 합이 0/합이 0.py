# BOJ 3151번 합이 0

import sys

N = int(sys.stdin.readline())
students = list(map(int,sys.stdin.readline().split()))
students.sort()
result = 0

for first_idx in range(N-2):
    l, r = first_idx+1, N - 1
    max_r = N
    while l < r:
        group_sum = students[first_idx] + students[l] + students[r]

        if group_sum == 0:
            if students[l] == students[r]:
                result += r - l
            else:
                if max_r > r:
                    max_r = r
                    while max_r >= 0 and students[max_r - 1] == students[r]:
                        max_r -= 1
                result += (r - max_r + 1)
            l += 1

        elif group_sum < 0:
            l += 1
        else:
            r -= 1

print(result)