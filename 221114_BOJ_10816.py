# BOJ 10816번 숫자 카드 2
# 이분 탐색, 정렬, 해시 자료 구조

N = int(input())
# 숫자 카드 리스트
cards = sorted(list(map(int, input().split())))
M = int(input())
# 구분해야할 숫자 카드 리스트
check = list(map(int, input().split()))

# 숫자 카드의 개수를 담는 해시
count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

# 이분 탐색 함수
def binarySearch(arr, target, start, end):
    mid = (start + end) // 2
    if start > end:
        return 0

    if arr[mid] == target:
        return count.get(target)
    elif arr[mid] < target:
        return binarySearch(arr, target, mid + 1, end)
    else:
        return binarySearch(arr, target, start, mid - 1)

for target in check:
    print(binarySearch(cards, target, 0, N-1), end=" ")