# BOJ 11501 주식
# 그리디

for _ in range(int(input())):
    N = int(input())
    nasdaq = list(map(int,input().split()))

    max_price = 0
    result = 0
    # 뒤에서부터 접근
    for i in range(N-1,-1,-1):
        # 현재 max값 갱신
        if nasdaq[i] > max_price:
            max_price = nasdaq[i]
        # 이익 추가
        else:
            result += (max_price - nasdaq[i])

    print(result)
