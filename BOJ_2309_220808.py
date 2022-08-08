# BOJ 2309번 일곱 난쟁이

h = [int(input()) for  in range(9)]
h.sort()
# 가짜 2명 키의 합
check = sum(h) - 100
fake = [0 for  in range(9)]
out = 0

for i in range(8):

    for j in range(i+1,9):
        # 가짜 2명 키의 합이면 해당 인덱스를 fake리스트에 표시
        if (h[i] + h[j]) == check:
            fake[i], fake[j] = 1, 1
            out = 1
            break

    if out:
        break

for v in range(9):
    # 가짜가 아니면 출력
    if not fake[v]:
        print(h[v])
