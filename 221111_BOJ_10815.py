# BOJ 10815번 숫자 카드
# 이분 탐색, 정렬, 자료 구조

N = int(input())
my_card = sorted(map(int, input().split()))
M = int(input())
check_card = list(map(int, input().split()))
answer = []

# 이분 탐색 함수
def binary(i, my_card, start, end):
    mid = (start+end) // 2
    if start > end:
        answer.append(str(0))
    elif i == my_card[mid]:
        answer.append(str(1))
    elif i > my_card[mid]:
        binary(i, my_card, mid + 1, end)
    else:
        binary(i, my_card, start, mid - 1)

# 모든 카드에 대한 이분탐색
for i in check_card:
    start = 0
    end = N-1
    binary(i, my_card, start, end)

print(' '.join(answer))