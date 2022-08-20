# BOJ 2961번 도영이가 만든 맛있는 음식
from itertools import combinations

N = int(input())
tastes = [list(map(int,input().split())) for _ in range(N)]
result = []
# num개의 맛을 고름
for num in range(1,N+1):
    # num개의 맛을 고를 때 생길 수 있는 조합
    all_tastes = list(combinations(tastes, num))
    # 조합들의
    for t in all_tastes:
        # 신 맛과 쓴 맛 계산해서
        sour = 1
        ssen = 0
        for i in t:
            sour *= i[0]
            ssen += i[1]
        # 결과 리스트에 삽입
        result.append(abs(sour-ssen))

print(min(result))
