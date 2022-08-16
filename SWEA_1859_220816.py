# SWEA 1859번 백만 장자 프로젝트

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    price = list(map(int,input().split()))
    i = 0
    result = 0
    inventory = 0
    cnt = 0
    max_value = max(price)

    while i < len(price):

        if price[i] < max_value:
            inventory += price[i]
            cnt += 1

        if price[i] == max_value:
            result += (cnt*price[i] - inventory)
            inventory = 0
            cnt = 0
            if i+1 < len(price):
                max_value = max(price[i+1:])

        i += 1

    print(f'#{tc} {result}')
