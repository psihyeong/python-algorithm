# BOJ 2012번 등수 매기기
# 그리디, 정렬

N = int(input())
expect_rank = [int(input()) for _ in range(N)]
# 예상순위 내림차순 정렬
expect_rank.sort()
result = 0

# 예상순위가 내림차순 정렬이므로, 1등부터
for i in range(N):
    real_rank = i+1
    # 불만도 더하기
    result += abs(expect_rank[i] - real_rank)

print(result)
