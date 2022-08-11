# SWEA 4880번 토너먼트 카드게임

TC = int(input())
def rsp(left,right,arr):
    if arr[right] == 1:
        if arr[left] == 3:
            return right
        else:
            return left
    elif arr[right] == 2:
        if arr[left] == 1:
            return right
        else:
            return left
    else:
        if arr[left] == 2:
            return right
        else:
            return left

def divide(i,j):
    if i == j:
        return i

    a = divide(i,(i+j)//2)
    b = divide(((i+j)//2)+1, j)
    return rsp(a,b,cards)


for tc in range(1,TC+1):
    N = int(input())
    cards = list(map(int,input().split()))
    cards = [0] + cards
    print(f'#{tc} {divide(1,N)}')
