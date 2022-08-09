# SWEA 1208 Flatten
import sys
sys.stdin = open('input1208.txt','r')

TC = 10
for tc in range(1,TC+1):
    dump = int(input())
    box = list(map(int, input().split()))

    high = [0 for _ in range(101)]

    for i in box:
        high[i] += 1

    h_id = 100
    l_id = 1
    while dump >= 0:
        # 가운데 id로 평탄화 될 수 있도록 사이드부터 검사
        if high[h_id] > 0:
            if high[l_id] > 0:
                high[h_id] -= 1
                high[h_id - 1] += 1
                high[l_id] -= 1
                high[l_id + 1] += 1
                dump -= 1

            else:
                l_id += 1

        else:
            h_id -= 1

    print(f'#{tc} {h_id - l_id}')


# TC = 10
# for tc in range(1,TC+1):
#     width = 100
#     dump = int(input())
#     box = list(map(int, input().split()))
#
#     # 덤프 1회 할 때 마다
#     for _ in range(dump):
#         maxId, minId = 0, 0
#         for idx in range(1, 100):
#             # 최댓값 구하기
#             if box[idx] > box[maxId]:
#                 maxId = idx
#             # 최솟값 구하기
#             if box[idx] < box[minId]:
#                 minId = idx
#         # +1, -1
#         box[maxId] -= 1
#         box[minId] += 1
#
#     maxV, minV = 0, 101
#
#     for i in box:
#         if i > maxV:
#             maxV = i
#         if i < minV:
#             minV = i
#     # 출력
#     print(f'#{tc} {maxV-minV}')
